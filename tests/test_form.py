from html.parser import HTMLParser
from pathlib import Path
import unittest


HTML_FILE = Path(__file__).resolve().parents[1] / "index.html"


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.form_depth = 0
        self.forms = 0
        self.inputs = {}
        self.labels = set()
        self.submit_buttons = 0

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "form":
            self.forms += 1
            self.form_depth += 1
        elif self.form_depth and tag == "input":
            self.inputs[attributes.get("name")] = attributes
        elif self.form_depth and tag == "label":
            self.labels.add(attributes.get("for"))
        elif self.form_depth and tag == "button" and attributes.get("type") == "submit":
            self.submit_buttons += 1

    def handle_endtag(self, tag):
        if tag == "form":
            self.form_depth -= 1


class FormTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = FormParser()
        cls.parser.feed(HTML_FILE.read_text(encoding="utf-8"))

    def test_form_exists(self):
        self.assertEqual(self.parser.forms, 1)

    def test_required_fields_have_correct_types_and_labels(self):
        for name, expected_type in (
            ("name", "text"),
            ("email", "email"),
            ("contactNumber", "tel"),
        ):
            with self.subTest(name=name):
                field = self.parser.inputs.get(name)
                self.assertIsNotNone(field)
                self.assertEqual(field.get("type"), expected_type)
                self.assertIn("required", field)
                self.assertIn(field.get("id"), self.parser.labels)

    def test_submit_button_exists(self):
        self.assertEqual(self.parser.submit_buttons, 1)


if __name__ == "__main__":
    unittest.main()

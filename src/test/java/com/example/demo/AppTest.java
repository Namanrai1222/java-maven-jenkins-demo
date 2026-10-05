package com.example.demo;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

class AppTest {
    @Test
    void greetsDefaultUser() {
        assertEquals("Hello, Jenkins!", App.greeting("Jenkins"));
    }

    @Test
    void trimsName() {
        assertEquals("Hello, Maven!", App.greeting(" Maven "));
    }

    @Test
    void rejectsBlankName() {
        assertThrows(IllegalArgumentException.class, () -> App.greeting("  "));
    }

    @Test
    void rejectsNullName() {
        assertThrows(IllegalArgumentException.class, () -> App.greeting(null));
    }
}

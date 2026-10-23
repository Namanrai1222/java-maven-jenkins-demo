# Java Maven Jenkins Demo

A Java 25 application built with Maven and tested with JUnit. The repository also contains a static [contact form](index.html) and automated HTML structure tests. Jenkins runs the root `Jenkinsfile`, publishes Java test results, and archives the JAR.

## Build locally

Install JDK 25, Maven 3.9 or newer, and Python 3, then run:

```sh
mvn -B -ntp clean verify
java -jar target/java-maven-jenkins-demo-1.0.0-SNAPSHOT.jar
python3 -m unittest discover -s tests -v
```

The application prints `Hello, Jenkins!`. The JUnit tests verify the greeting behavior. The Python tests verify that the form contains labeled, required Name, Email, and Contact Number fields and a Submit button. Open `index.html` in a browser to view the form. Submission displays a demo message; no data is sent or stored.

## Connect Jenkins to GitHub

1. Install Jenkins LTS with JDK 25 and the Pipeline, Git, and JUnit plugins. Make JDK 25, Maven, and Python 3 available to the Jenkins process.
2. Create a Pipeline job. Choose Pipeline script from SCM, select Git, enter this repository HTTPS clone URL, set branch `*/main`, and set Script Path to `Jenkinsfile`.
3. Save and select Build Now. Jenkins runs Maven, publishes JUnit results, and archives the JAR.
4. The pipeline polls GitHub about every five minutes while Jenkins is running. This works for a local Jenkins server. For immediate builds, expose Jenkins securely and configure a GitHub webhook at `https://YOUR_JENKINS_HOST/github-webhook/`.

Do not put GitHub credentials in this repository. Public repositories can be cloned without credentials. For a private repository, add a Jenkins credential and select it in the job Git SCM settings.

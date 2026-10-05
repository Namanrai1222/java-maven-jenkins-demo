# Java Maven Jenkins Demo

A Java 25 application built with Maven and tested with JUnit. Jenkins runs the root `Jenkinsfile`, publishes test results, and archives the JAR.

## Build locally

Install JDK 25 and Maven 3.9 or newer, then run:

```sh
mvn -B -ntp clean verify
java -jar target/java-maven-jenkins-demo-1.0.0-SNAPSHOT.jar
```

The application prints `Hello, Jenkins!`. Three JUnit tests verify the greeting behavior.

## Connect Jenkins to GitHub

1. Install Jenkins LTS with JDK 25 and the Pipeline, Git, and JUnit plugins. Make JDK 25 and Maven available to the Jenkins process.
2. Create a Pipeline job. Choose Pipeline script from SCM, select Git, enter this repository HTTPS clone URL, set branch `*/main`, and set Script Path to `Jenkinsfile`.
3. Save and select Build Now. Jenkins runs Maven, publishes JUnit results, and archives the JAR.
4. The pipeline polls GitHub about every five minutes while Jenkins is running. This works for a local Jenkins server. For immediate builds, expose Jenkins securely and configure a GitHub webhook at `https://YOUR_JENKINS_HOST/github-webhook/`.

Do not put GitHub credentials in this repository. Public repositories can be cloned without credentials. For a private repository, add a Jenkins credential and select it in the job Git SCM settings.

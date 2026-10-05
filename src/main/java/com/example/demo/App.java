package com.example.demo;

public final class App {
    private App() {
    }

    public static String greeting(String name) {
        if (name == null || name.isBlank()) {
            throw new IllegalArgumentException("name must not be blank");
        }
        return "Hello, " + name.trim() + "!";
    }

    public static void main(String[] args) {
        String name = args.length > 0 ? args[0] : "Jenkins";
        System.out.println(greeting(name));
    }
}

package com.acme.seleniumpomdemo.config;

public class Config {
    private static Config instance;
    private final String baseUrl;
    private final String browser;

    private Config() {
        this.baseUrl = System.getProperty("baseUrl", "https://demowebshop.tricentis.com");
        this.browser = System.getProperty("browser", "chrome");
    }

    public static Config getInstance() {
        if (instance == null) {
            instance = new Config();
        }
        return instance;
    }

    public String getBaseUrl() {
        return baseUrl;
    }

    public String getBrowser() {
        return browser;
    }
}
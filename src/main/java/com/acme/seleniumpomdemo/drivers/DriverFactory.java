package com.acme.seleniumpomdemo.drivers;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import com.acme.seleniumpomdemo.config.Config;

public class DriverFactory {
    private DriverFactory() {}

    public static WebDriver createDriver() {
        String browser = Config.getInstance().getBrowser();
        switch (browser) {
            case "chrome":
                return new ChromeDriver();
            case "firefox":
                return new FirefoxDriver();
            default:
                throw new IllegalArgumentException("Unsupported browser: " + browser);
        }
    }
}
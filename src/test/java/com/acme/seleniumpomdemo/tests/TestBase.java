package com.acme.seleniumpomdemo.tests;

import com.acme.seleniumpomdemo.config.Config;
import com.acme.seleniumpomdemo.drivers.DriverFactory;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.openqa.selenium.WebDriver;

public abstract class TestBase {
    protected WebDriver driver;

    @BeforeEach
    public void setUp() {
        // Initialize WebDriver using the factory
        driver = DriverFactory.createDriver();
        // Navigate to the base URL
        driver.get(Config.getInstance().getBaseUrl());
    }

    @AfterEach
    public void tearDown() {
        // Quit the driver after each test
        if (driver != null) {
            driver.quit();
        }
    }
}
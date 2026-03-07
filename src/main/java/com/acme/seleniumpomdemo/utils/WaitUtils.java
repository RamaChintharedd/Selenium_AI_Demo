package com.acme.seleniumpomdemo.utils;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class WaitUtils {
    public static WebElement waitForElement(WebDriver driver, By locator) {
        return new WebDriverWait(driver,Duration.ofMinutes(12))
                .until(ExpectedConditions.presenceOfElementLocated(locator));
    }
}
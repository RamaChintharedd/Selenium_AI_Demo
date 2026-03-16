package utils;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

/**
 * Small wait utility to centralize explicit waits.
 */
public final class WaitUtils {
    private static final Duration DEFAULT_TIMEOUT = Duration.ofSeconds(10);

    private WaitUtils() {
    }

    public static WebElement waitForElementVisible(WebDriver driver, By locator) {
        WebDriverWait wait = new WebDriverWait(driver, DEFAULT_TIMEOUT);
        return wait.until(ExpectedConditions.visibilityOfElementLocated(locator));
    }

    public static boolean waitForUrlContains(WebDriver driver, String fragment) {
        WebDriverWait wait = new WebDriverWait(driver, DEFAULT_TIMEOUT);
        return wait.until(ExpectedConditions.urlContains(fragment));
    }

    public static boolean waitForElementNotVisible(WebDriver driver, By locator) {
        WebDriverWait wait = new WebDriverWait(driver, DEFAULT_TIMEOUT);
        return wait.until(ExpectedConditions.invisibilityOfElementLocated(locator));
    }
}

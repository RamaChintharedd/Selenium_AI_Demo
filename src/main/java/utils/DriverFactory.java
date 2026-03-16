package utils;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

/**
 * Simple driver factory. Adjust system property "webdriver.chrome.driver" to point to your chromedriver.
 * You can extend this to support other browsers and remote drivers.
 */
public final class DriverFactory {

    private DriverFactory() {
        // utility class
    }

    public static WebDriver createChromeDriver() {
        // Optional: read headless from system property
        boolean headless = Boolean.parseBoolean(System.getProperty("headless", "false"));

        // Ensure chromedriver binary path set via -Dwebdriver.chrome.driver or environment PATH
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--start-maximized");
        if (headless) {
            options.addArguments("--headless=new");
            options.addArguments("--window-size=1920,1080");
        }

        return new ChromeDriver(options);
    }
}

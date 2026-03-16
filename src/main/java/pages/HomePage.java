package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import utils.WaitUtils;

/**
 * Page Object representing the homepage of Demo Web Shop.
 */
public class HomePage {
    private final WebDriver driver;

    private final By loginLink = By.linkText("Log in");

    public HomePage(WebDriver driver) {
        this.driver = driver;
    }

    public void open(String url) {
        driver.get(url);
    }

    public void clickLogin() {
        WebElement link = WaitUtils.waitForElementVisible(driver, loginLink);
        link.click();
    }

    public boolean isLoginLinkPresent() {
        try {
            return driver.findElement(loginLink).isDisplayed();
        } catch (Exception e) {
            return false;
        }
    }
}

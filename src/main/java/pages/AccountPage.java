package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import utils.WaitUtils;

/**
 * Page Object representing the authenticated account area / landing page.
 */
public class AccountPage {
    private final WebDriver driver;

    private final By myAccountLink = By.linkText("My account");
    private final By logoutLink = By.linkText("Log out");

    public AccountPage(WebDriver driver) {
        this.driver = driver;
    }

    public boolean isAt() {
        try {
            return driver.findElement(logoutLink).isDisplayed();
        } catch (Exception e) {
            return false;
        }
    }

    public boolean isMyAccountVisible() {
        try {
            return WaitUtils.waitForElementVisible(driver, myAccountLink).isDisplayed();
        } catch (Exception e) {
            return false;
        }
    }
}

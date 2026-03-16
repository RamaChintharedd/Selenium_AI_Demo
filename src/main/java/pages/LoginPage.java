package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import utils.WaitUtils;

/**
 * Page Object for the login page.
 * Contains methods to interact with the login form and read validation messages.
 */
public class LoginPage {
    private final WebDriver driver;

    // Locators based on Demo Web Shop markup
    private final By emailInput = By.id("Email");
    private final By passwordInput = By.id("Password");
    private final By loginButton = By.cssSelector("input.button-1.login-button, input[type='submit']");
    private final By errorSummary = By.cssSelector(".message-error, .validation-summary-errors");

    public static final String LOGIN_PATH = "/login";
    public static final String LOGIN_URL = "https://demowebshop.tricentis.com/login";

    public LoginPage(WebDriver driver) {
        this.driver = driver;
    }

    public boolean isAt() {
        String url = driver.getCurrentUrl();
        return url.contains(LOGIN_PATH) || url.equalsIgnoreCase(LOGIN_URL);
    }

    public boolean isEmailFieldDisplayed() {
        try {
            return driver.findElement(emailInput).isDisplayed();
        } catch (Exception e) {
            return false;
        }
    }

    public void enterEmail(String email) {
        WebElement emailEl = WaitUtils.waitForElementVisible(driver, emailInput);
        emailEl.clear();
        emailEl.sendKeys(email == null ? "" : email);
    }

    public void enterPassword(String password) {
        WebElement pwEl = WaitUtils.waitForElementVisible(driver, passwordInput);
        pwEl.clear();
        pwEl.sendKeys(password == null ? "" : password);
    }

    public void clickLogin() {
        WebElement btn = WaitUtils.waitForElementVisible(driver, loginButton);
        btn.click();
    }

    public String getValidationError() {
        try {
            WebElement err = WaitUtils.waitForElementVisible(driver, errorSummary);
            return err.getText().trim();
        } catch (Exception e) {
            return "";
        }
    }

    public boolean hasAuthenticationError() {
        String txt = getValidationError();
        return txt != null && !txt.isEmpty();
    }
}

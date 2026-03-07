package com.acme.seleniumpomdemo.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class LoginPage extends BasePage {

    private final By emailInput = By.id("Email");
    private final By passwordInput = By.id("Password");
    private final By rememberCheck = By.id("RememberMe");
    private final By forgotPasswordLink = By.linkText("Forgot password?");
    private final By loginButton = By.cssSelector("input.button-1.login-button");
    private final By genericError = By.cssSelector("div.message-error.validation-summary-errors");
    private final By emailError = By.cssSelector("span.field-validation-error[data-valmsg-for='Email']");
    private final By passwordError = By.cssSelector("span.field-validation-error[data-valmsg-for='Password']");

    public LoginPage(WebDriver driver) {
        super(driver);
    }

    public boolean isPageLoaded() {
        return isDisplayed(emailInput) && isDisplayed(passwordInput);
    }

    public boolean isEmailFieldPresent() {
        return isDisplayed(emailInput);
    }

    public boolean isPasswordFieldPresentAndMasked() {
        if (!isDisplayed(passwordInput)) return false;
        return find(passwordInput).getAttribute("type").equals("password");
    }

    public boolean isRememberMePresent() {
        return isDisplayed(rememberCheck);
    }

    public boolean isForgotPasswordPresent() {
        return isDisplayed(forgotPasswordLink);
    }

    public boolean isLoginButtonPresent() {
        return
                isDisplayed(loginButton);
    }

    public void login(String email, String password, boolean remember) {
        type(emailInput, email);
        type(passwordInput, password);
        if (remember && !find(rememberCheck).isSelected()) {
            click(rememberCheck);
        }
        click(loginButton);
    }

    public String getGenericError() {
        return getText(genericError);
    }

    public String getEmailError() {
        return getText(emailError);
    }

    public String getPasswordError() {
        return getText(passwordError);
    }
}
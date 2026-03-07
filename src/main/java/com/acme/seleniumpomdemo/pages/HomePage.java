package com.acme.seleniumpomdemo.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class HomePage extends BasePage {

    private final By loginLink = By.linkText("Log in");
    private final By myAccount = By.linkText("My account");
    private final By logoutLink = By.linkText("Log out");

    public HomePage(WebDriver driver) {
        super(driver);
    }

    public void navigateToLogin() {
        click(loginLink);
    }

    public boolean isLoggedIn() {
        return isDisplayed(myAccount) || isDisplayed(logoutLink);
    }
}
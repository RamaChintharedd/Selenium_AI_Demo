package com.acme.seleniumpomdemo.tests;

import com.acme.seleniumpomdemo.pages.HomePage;
import com.acme.seleniumpomdemo.pages.LoginPage;
import org.junit.jupiter.api.Test;

public class LoginUITest extends TestBase {

    @Test
    public void testLoginPageUIElementsPresence() {
        HomePage homePage = new HomePage(driver);
        homePage.navigateToLogin();
        LoginPage loginPage = new LoginPage(driver);

        // ... assertions ...
    }
}
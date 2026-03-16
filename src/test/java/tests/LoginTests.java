package tests;

import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import org.openqa.selenium.WebDriver;

import pages.AccountPage;
import pages.HomePage;
import pages.LoginPage;
import utils.DriverFactory;

/**
 * TestNG tests mapping to the provided BDD scenarios. Uses Page Object Model.
 */
public class LoginTests {

    private WebDriver driver;
    private HomePage homePage;
    private LoginPage loginPage;
    private AccountPage accountPage;

    private static final String BASE_URL = "https://demowebshop.tricentis.com";

    @BeforeMethod(alwaysRun = true)
    public void setUp() {
        driver = DriverFactory.createChromeDriver();
        homePage = new HomePage(driver);
        loginPage = new LoginPage(driver);
        accountPage = new AccountPage(driver);
    }

    @AfterMethod(alwaysRun = true)
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    @Test(description = "Click 'Log in' on homepage redirects to login page and shows email field")
    public void testNavigateToLoginFromHome() {
        homePage.open(BASE_URL);
        Assert.assertTrue(homePage.isLoginLinkPresent(), "Login link should be present on homepage");

        homePage.clickLogin();
        Assert.assertTrue(loginPage.isAt(), "Should be on the login page after clicking login");
        Assert.assertTrue(loginPage.isEmailFieldDisplayed(), "Email input should be displayed on login page");
    }

    @Test(description = "Registered user logs in successfully")
    public void testSuccessfulLoginWithValidCredentials() {
        // Use the registered credentials from BDD
        String email = "registered_user@example.com";
        String password = "CorrectPassword123";

        // Navigate directly to login page
        driver.get(LoginPage.LOGIN_URL);
        Assert.assertTrue(loginPage.isAt(), "Must be on login page");

        loginPage.enterEmail(email);
        loginPage.enterPassword(password);
        loginPage.clickLogin();

        // After a successful login, account specific elements should be visible
        Assert.assertTrue(accountPage.isAt(), "User should be authenticated and logout link visible");
        Assert.assertTrue(accountPage.isMyAccountVisible(), "My account link should be visible for authenticated users");
    }

    @Test(description = "Prevent submission when email field is empty")
    public void testPreventSubmissionWhenEmailEmpty() {
        driver.get(LoginPage.LOGIN_URL);
        Assert.assertTrue(loginPage.isAt());

        // Leave email empty
        loginPage.enterEmail("");
        // Enter a valid password
        loginPage.enterPassword("SomeValidPassword123");
        loginPage.clickLogin();

        // Expect validation or remain on login page with error
        Assert.assertTrue(loginPage.hasAuthenticationError() || loginPage.isAt(), "Should remain on login page and show error when email is empty");
        String err = loginPage.getValidationError();
        Assert.assertTrue(err.toLowerCase().contains("email") || err.length() > 0, "Should show an error mentioning email or a general error");
    }

    @DataProvider(name = "malformedEmails")
    public Object[][] malformedEmails() {
        return new Object[][] {
            {"user@"},
            {"userexample.com"},
            {"@example.com"},
            {"user@.com"}
        };
    }

    @Test(dataProvider = "malformedEmails", description = "Show validation error for malformed email formats")
    public void testEmailFormatValidation(String email) {
        driver.get(LoginPage.LOGIN_URL);
        Assert.assertTrue(loginPage.isAt());

        loginPage.enterEmail(email);
        loginPage.enterPassword("AnyValidPassword123");
        loginPage.clickLogin();

        // Should remain on login page and show validation about invalid email
        Assert.assertTrue(loginPage.isAt(), "User should remain on login page for malformed email");
        String err = loginPage.getValidationError();
        Assert.assertTrue(err.length() > 0, "Validation message should be shown for malformed email");
    }

    @Test(description = "Prevent submission when password field is empty")
    public void testPreventSubmissionWhenPasswordEmpty() {
        driver.get(LoginPage.LOGIN_URL);
        Assert.assertTrue(loginPage.isAt());

        // Enter a registered email but no password
        loginPage.enterEmail("registered_user@example.com");
        loginPage.enterPassword("");
        loginPage.clickLogin();

        Assert.assertTrue(loginPage.isAt(), "Should remain on login page when password is empty");
        String err = loginPage.getValidationError();
        Assert.assertTrue(err.length() > 0 || loginPage.hasAuthenticationError(), "Should display an error indicating password required");
    }

    @DataProvider(name = "invalidCredentials")
    public Object[][] invalidCredentials() {
        return new Object[][] {
            {"registered_user@example.com", "WrongPassword123"},
            {"unregistered@example.com", "AnyPassword123"}
        };
    }

    @Test(dataProvider = "invalidCredentials", description = "Show error for incorrect or unregistered credentials")
    public void testIncorrectCredentialsHandling(String email, String password) {
        driver.get(LoginPage.LOGIN_URL);
        Assert.assertTrue(loginPage.isAt());

        loginPage.enterEmail(email);

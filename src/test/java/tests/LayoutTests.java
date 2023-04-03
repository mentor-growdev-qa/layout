package tests;

import com.galenframework.testng.GalenTestNgTestBase;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.testng.annotations.Test;

import java.io.IOException;

import static java.util.Arrays.asList;

public class LayoutTests extends GalenTestNgTestBase {

    @Override
    public WebDriver createDriver(Object[] objects) {
        System.setProperty("webdriver.chrome.driver", "/Users/williamsoares/Documents/chromedriver");
        ChromeOptions chromeOptions = new ChromeOptions();
        chromeOptions.addArguments("--remote-debugging-port=9222");
        chromeOptions.addArguments("--no-sandbox");
        WebDriver driver = new ChromeDriver(chromeOptions);
        return driver;
    }

    @Test
    public void test() throws IOException {
        load("https://www.growdev.com.br/", 1280, 2000);
        checkLayout("src/test/java/specs/growdevspec.spec", asList("desktop"));
    }

}

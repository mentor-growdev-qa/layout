package tests;

import com.galenframework.testng.GalenTestNgTestBase;
import core.GalenTestBase;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.testng.annotations.Test;

import java.io.IOException;

import static java.util.Arrays.asList;

public class LayoutTests extends GalenTestBase {
    @Test(dataProvider = "devices")
    public void test(TestDevice device) throws IOException {
        load("https://www.growdev.com.br");
        checkLayout("src/test/java/specs/growdevspec.spec", device.getTags());
    }

}
package tests;

import com.galenframework.testng.GalenTestNgTestBase;
import core.GalenTestBase;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
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
        load("https://www.petz.com.br/");
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        if (device.getTags().contains("mobile") || device.getTags().contains("tablet")){
            getDriver().findElement(By.id("openMenuMobile")).click();
        }
        checkLayout("src/test/java/specs/growdevspec.spec", device.getTags());
    }

}
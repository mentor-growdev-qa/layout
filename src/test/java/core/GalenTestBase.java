package core;

import com.galenframework.testng.GalenTestNgTestBase;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.testng.annotations.DataProvider;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static java.util.Arrays.asList;

public abstract class GalenTestBase extends GalenTestNgTestBase {

    @Override
    public WebDriver createDriver(Object[] args) {
        WebDriverManager.chromedriver().setup();
        WebDriver driver = null;
        Map<String, String> mobileEmulation = new HashMap<>();
        ChromeOptions chromeOptions = new ChromeOptions();
        if (args.length > 0) {
            if (args[0] != null && args[0] instanceof TestDevice) {
                TestDevice device = (TestDevice) args[0];
                if (device.getScreenSize() != null && (device.getTags().contains("mobile") || device.getTags().contains("tablet"))) {
                    mobileEmulation.put("userAgent", "Mozilla/5.0 (Linux; Android 8.0.00; Pixel 2 XL Build/OPD1.170816.004)" +
                            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36");
                    chromeOptions.setExperimentalOption("mobileEmulation", mobileEmulation);
                    driver = new ChromeDriver(chromeOptions);
                    driver.manage().window().setSize(device.getScreenSize());
                } else if (device.getScreenSize() != null && device.getTags().contains("desktop")) {
                    driver = new ChromeDriver();
                    driver.manage().window().setSize(device.getScreenSize());
                }
            }
        }
        return driver;
    }

    public void load(String uri) {
        getDriver().get(uri);
    }

    @DataProvider(name = "devices")
    public Object[][] devices() {
        return new Object[][]{
                {new TestDevice("mobile", new Dimension(320, 2000), asList("mobile"))},
                {new TestDevice("tablet", new Dimension(768, 800), asList("tablet"))},
                {new TestDevice("desktop", new Dimension(1280, 800), asList("desktop"))}
        };
    }

    public static class TestDevice {
        private final String name;
        private final Dimension screenSize;
        private final List<String> tags;

        public TestDevice(String name, Dimension screenSize, List<String> tags) {
            this.name = name;
            this.screenSize = screenSize;
            this.tags = tags;
        }

        public String getName() {
            return name;
        }

        public Dimension getScreenSize() {
            return screenSize;
        }

        public List<String> getTags() {
            return tags;
        }

        @Override
        public String toString() {
            return String.format("%s %dx%d", name, screenSize.width, screenSize.height);
        }
    }
}

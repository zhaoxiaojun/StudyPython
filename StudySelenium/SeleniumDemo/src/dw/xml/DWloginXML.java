package dw.xml;

import java.io.File;
import java.io.FileOutputStream;
import java.util.Iterator;
import java.util.List;

import org.apache.commons.codec.binary.Base64;
import org.dom4j.Document;
import org.dom4j.DocumentException;
import org.dom4j.Element;
import org.dom4j.io.SAXReader;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;

import com.thoughtworks.selenium.DefaultSelenium;
import com.thoughtworks.selenium.SeleneseTestBase;
import com.thoughtworks.selenium.Selenium;

/**
 * @author Zhu Shang Yuan
 * 
 */
public class DWloginXML extends SeleneseTestBase {
	private static Selenium selenium;
	private static List<Element> stepNodes;
	private static int timeout = 2;

	@SuppressWarnings("unchecked")
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		// settings
		String application_url = "http://www.google.com.hk/";
		String browser = "*iexplore";
		String seleniumServer = "127.0.0.1";
		String seleniumPort = "4444";
		String ucXMLFile = System.getProperty("user.dir") + File.separator
				+ "UseCases" + File.separator + "GoogleDWTest.xml";
		;
		Document document = null;
		try {
			System.out.println("测试用例XML文件位置::" + ucXMLFile);
			document = new SAXReader().read(new File(ucXMLFile));
		} catch (DocumentException e) {
			e.printStackTrace();
		}
		Element suiteElm = document.getRootElement();
		// settings element
		Element settings = suiteElm.element("SETTINGS");
		if (settings != null) {
			browser = settings.attributeValue("browser");
			seleniumServer = settings.attributeValue("seleniumServer");
			seleniumPort = settings.attributeValue("seleniumPort");
			application_url = settings.attributeValue("application_url");
		}

		// TEST element
		Element testElm = suiteElm.element("TEST");
		System.out.println("测试用例名称为::" + testElm.attributeValue("name"));
		if (testElm.attributeValue("timeout") != null) {
			// 用例级别的timeout设置,覆盖了默认设置！
			timeout = new Integer(testElm.attributeValue("timeout")).intValue();
			System.out.println("延时设置，timeout=" + testElm.attributeValue("timeout")+"秒");
	}

		stepNodes = testElm.element("STEPS").elements();
		selenium = new DefaultSelenium(seleniumServer,
				new Integer(seleniumPort).intValue(), browser, application_url);
		System.out.println("正在启动Selenium。。。");
		selenium.start();
		selenium.windowMaximize();
		selenium.open(application_url);
		selenium.waitForPageToLoad(1000000000+"");

	}

	@AfterClass
	public static void tearDownAfterClass() throws Exception {
		if (selenium != null) {
			System.out.println("停止Selenium！");
			selenium.close();
			selenium.stop();
			
		}
	}

	@Test
	public void test() {
		Element elm = null;
		// 循环解析测试步骤
		Iterator<Element> iterator = null;
		iterator = stepNodes.iterator();
		while (iterator != null && iterator.hasNext()) {// while循环开始
			elm = iterator.next();
			System.out.println("------------------------------>");
			System.out.println("step index=" + elm.attributeValue("index"));
			System.out.println("step name=" + elm.attributeValue("name"));
			System.out.println("step type=" + elm.attributeValue("type"));
			String type = elm.attributeValue("type");
			if (type == null) {
				SeleneseTestBase.fail("必须定义type属性，请检查XML测试用例。");
			}
			if (type.equals("Type.CLICK")) {
				// 处理Click单击操作
				pause(timeout*1000);
				try {
					String xpValue = elm.element("XPATH").getText();
					selenium.click(xpValue);

				} catch (Exception e) {
					SeleneseTestBase.fail(e.getMessage()
							+ "\n步骤执行失败，测试执行被中止,测试元素为:\n" + elm.asXML());
				}
			} else if (type.equals("Type.INPUT")) {
				// 处理Input 在输入框执行输入操作
				pause(timeout*1000);
				try {
					String inValue = elm.element("VALUE").getText();
					selenium.type(elm.element("XPATH").getText(), inValue);
				} catch (Exception e) {
					SeleneseTestBase.fail(e.getMessage()
							+ "\n步骤执行失败，测试执行被中止,测试元素为:\n" + elm.asXML());
				}
			}
			else if(type.equals("Type.CaptureScreenshot")){
				pause(timeout*1000);
				String fileName = elm.element("VALUE").getText();
				captureScreenshot(fileName);
			}
		}// 循环解析测试步骤；while循环结束
	}

	/**
	 * fileName 保存截图的文件名
	 */
	private void captureScreenshot(String fileName) {

		String imagePath = System.getProperty("user.dir") + File.separator
				+ fileName + ".png";
		try {
			String base64Screenshot = selenium.captureScreenshotToString();
			byte[] decodedScreenshot = Base64.decodeBase64(base64Screenshot
					.getBytes());
			FileOutputStream fos = new FileOutputStream(new File(imagePath));
			fos.write(decodedScreenshot);
			fos.close();
			System.out.println("截图保存至" + imagePath);

		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}

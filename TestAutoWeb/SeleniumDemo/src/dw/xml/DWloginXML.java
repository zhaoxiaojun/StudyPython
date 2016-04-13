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
			System.out.println("��������XML�ļ�λ��::" + ucXMLFile);
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
		System.out.println("������������Ϊ::" + testElm.attributeValue("name"));
		if (testElm.attributeValue("timeout") != null) {
			// ���������timeout����,������Ĭ�����ã�
			timeout = new Integer(testElm.attributeValue("timeout")).intValue();
			System.out.println("��ʱ���ã�timeout=" + testElm.attributeValue("timeout")+"��");
	}

		stepNodes = testElm.element("STEPS").elements();
		selenium = new DefaultSelenium(seleniumServer,
				new Integer(seleniumPort).intValue(), browser, application_url);
		System.out.println("��������Selenium������");
		selenium.start();
		selenium.windowMaximize();
		selenium.open(application_url);
		selenium.waitForPageToLoad(1000000000+"");

	}

	@AfterClass
	public static void tearDownAfterClass() throws Exception {
		if (selenium != null) {
			System.out.println("ֹͣSelenium��");
			selenium.close();
			selenium.stop();
			
		}
	}

	@Test
	public void test() {
		Element elm = null;
		// ѭ���������Բ���
		Iterator<Element> iterator = null;
		iterator = stepNodes.iterator();
		while (iterator != null && iterator.hasNext()) {// whileѭ����ʼ
			elm = iterator.next();
			System.out.println("------------------------------>");
			System.out.println("step index=" + elm.attributeValue("index"));
			System.out.println("step name=" + elm.attributeValue("name"));
			System.out.println("step type=" + elm.attributeValue("type"));
			String type = elm.attributeValue("type");
			if (type == null) {
				SeleneseTestBase.fail("���붨��type���ԣ�����XML����������");
			}
			if (type.equals("Type.CLICK")) {
				// ����Click��������
				pause(timeout*1000);
				try {
					String xpValue = elm.element("XPATH").getText();
					selenium.click(xpValue);

				} catch (Exception e) {
					SeleneseTestBase.fail(e.getMessage()
							+ "\n����ִ��ʧ�ܣ�����ִ�б���ֹ,����Ԫ��Ϊ:\n" + elm.asXML());
				}
			} else if (type.equals("Type.INPUT")) {
				// ����Input �������ִ���������
				pause(timeout*1000);
				try {
					String inValue = elm.element("VALUE").getText();
					selenium.type(elm.element("XPATH").getText(), inValue);
				} catch (Exception e) {
					SeleneseTestBase.fail(e.getMessage()
							+ "\n����ִ��ʧ�ܣ�����ִ�б���ֹ,����Ԫ��Ϊ:\n" + elm.asXML());
				}
			}
			else if(type.equals("Type.CaptureScreenshot")){
				pause(timeout*1000);
				String fileName = elm.element("VALUE").getText();
				captureScreenshot(fileName);
			}
		}// ѭ���������Բ��裻whileѭ������
	}

	/**
	 * fileName �����ͼ���ļ���
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
			System.out.println("��ͼ������" + imagePath);

		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}

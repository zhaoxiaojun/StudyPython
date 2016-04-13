package dw.junit;
import java.io.File;
import java.io.FileOutputStream;

import org.apache.commons.codec.binary.Base64;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import com.thoughtworks.selenium.DefaultSelenium;
import com.thoughtworks.selenium.SeleneseTestBase;
import com.thoughtworks.selenium.Selenium;

/**
 * 
 */

/**
 * @author Zhu Shang Yuan
 *
 */
public class DWloginJUnit extends SeleneseTestBase{
	private static Selenium selenium;

	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
	     selenium = new DefaultSelenium("localhost", 4444, "*firefox",
	                "http://www.google.com.hk/");
	        System.out.println("��������Selenium������");
	        selenium.start();
	        selenium.windowMaximize();
	        selenium.open("/webhp?hl=en-US");
	        }

	@AfterClass
	public static void tearDownAfterClass() throws Exception {
	    if(selenium != null){
	    	 System.out.println("ֹͣSelenium��");
            selenium.stop();
        }
	}

	@Test
	public void test() {
		//��Google��ѯ���������ibm developerworks cn
		String queryString="ibm developerworks cn";
		selenium.type("//input[@name='q']", queryString);
		pause(1000);
		//������ѯ��ť��ִ�в�ѯ
		selenium.click("//input[@name='btnK']");
		pause(1000);
		System.out.println("��ȡ��ҳ����⣺"+selenium.getTitle());	
		pause(2000);
		SeleneseTestBase.assertTrue(selenium.getTitle().contains(queryString));
		//���Խ�ͼ����
		captureScreenshot("��ͼ����JUnit");
		
		
	}

		/**
		 * fileName �����ͼ���ļ���
		 */
	  private void captureScreenshot(String fileName) {

			String imagePath = System.getProperty("user.dir") + File.separator + fileName + ".png";	
			try {
				String base64Screenshot = selenium.captureScreenshotToString();
				byte[] decodedScreenshot = Base64.decodeBase64(base64Screenshot
						.getBytes());
				FileOutputStream fos = new FileOutputStream(new File(imagePath));
				fos.write(decodedScreenshot);
				fos.close();
				System.out.println("��ͼ������"+imagePath);

			} catch (Exception e) {
		e.printStackTrace();
			}
		}
}

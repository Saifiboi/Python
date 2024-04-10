from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


def connect_to_vpn():
    # Replace "INSERT_EXTENSION_ID" with the actual extension ID
    extension_id = "bihmplhobchoageeokmgbdihknkjbknd"

    # Set up Chrome WebDriver with the VPN extension
    chrome_options = Options()
    chrome_options.add_argument(f"--load-extension={extension_id}.crx")
    driver = webdriver.Chrome(options=chrome_options)

    # Check if the VPN panel window is open
    if len(driver.window_handles) > 1:
        # Switch to the extension's panel window
        driver.switch_to.window(driver.window_handles[1])
        # Insert any additional logic to check if the VPN is connected or wait for it to connect
        # For example, you can add some time.sleep() or use explicit waits to check for elements

    return driver


def main():
    # Connect to VPN
    driver = connect_to_vpn()

    # Wait for the VPN connection to establish (you can modify this based on your needs)
    time.sleep(5)

    # Open amazon.com in the main window
    driver.get("https://www.amazon.com/Apple-AirPods-Charging-Previous-Model/dp/B01MQWUXZS/ref=sr_1_7?crid=2JVA9L37VDBY0&keywords=earpods&qid=1690810219&sprefix=earpods%2Caps%2C500&sr=8-7")
    print(driver.find_element(by=By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/span[2]/span[2]').text)
    # You can add further code here to interact with the website or perform any operations on amazon.com

    # Close the browser when done
    driver.quit()


if __name__ == "__main__":
    main()

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# display = Display(visible=0, size=(1024, 768))
# display.start()
# 生成浏览器对象
binary = FirefoxBinary('/usr/bin/firefox')
browser = webdriver.Firefox(executable_path='/home/bigbigbro/Downloads/geckodriver')
 # 使浏览器访问 https://www.amazon.com/。
page = 'https://sellercentral.amazon.fr/orders-v3/fba/all?date-range=1588284000000-1590530399000&page=1'

browser.get(page)
# 找到亚马逊主页切换语言的element。
browser.find_element_by_id("ap_email").clear()
browser.find_element_by_id("ap_password").clear()

# inputemail = input("请输入账号：")
# inputpassword = input("请输入密码：")

inputemail = "info@elfcams.com"
inputpassword = "ABC&1234567892"

browser.find_element_by_id("ap_email").send_keys(inputemail)
browser.find_element_by_id("ap_password").send_keys(inputpassword)

browser.find_element_by_id("signInSubmit").click()

time.sleep(1)
print("等待网址加载完毕...")

inputOTP = input("请输入OTP：")
browser.find_element_by_id("auth-mfa-otpcode").send_keys(inputOTP)
browser.find_element_by_id("auth-signin-button").click()

# commande = browser.find_element_by_link_text("Expédier vos commandes")
# commande.click()
# Selects = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "a-button-inner")))
# for select in Selects:
#     if select.text == '15':
#         time.sleep(0.5)943673
#         s1 = Select(select)
#         s1.select_by_value("100")

time.sleep(1)


elements = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "cell-body-title"))
    )

elements_list = []

title_elements = []
for element in elements:
    element_text = element.text
    if '-' in element_text:
        elements_list.append(element_text)
        title_elements.append(element)

print(elements_list)
time.sleep(1)

for title in title_elements:
    title.click()
    try:
        time.sleep(0.5)
        commande = browser.find_element_by_link_text("Demander un avis")
        commande.click()
        time.sleep(0.5)
        try:
            oui = browser.find_element_by_link_text("oui")
            oui.click()
            time.sleep(0.5)
            browser.back()
            time.sleep(0.5)
        except:
            time.sleep(0.5)
            print('not_found_oui')
            browser.back()
        browser.back()
    except:

        time.sleep(0.5)
        browser.back()
        time.sleep(0.5)


browser.get(page)


from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

# display = Display(visible=0, size=(1024, 768))
# display.start()
# 生成浏览器对象
binary = FirefoxBinary('/usr/bin/firefox')
browser = webdriver.Firefox(executable_path='/home/bigbigbro/Downloads/geckodriver')
 # 使浏览器访问 https://www.amazon.com/。
browser.get('https://sellercentral.amazon.fr/home?')
# 找到亚马逊主页切换语言的element。
browser.find_element_by_id("ap_email").clear()
browser.find_element_by_id("ap_password").clear()

# inputemail = input("请输入账号：")
# inputpassword = input("请输入密码：")

inputemail = "info@elfcams.com"
inputpassword = "ABC&1234567891"

browser.find_element_by_id("ap_email").send_keys(inputemail)
browser.find_element_by_id("ap_password").send_keys(inputpassword)

browser.find_element_by_id("signInSubmit").click()

time.sleep(1)
print("等待网址加载完毕...")

inputOTP = input("请输入OTP：")
browser.find_element_by_id("auth-mfa-otpcode").send_keys(inputOTP)
browser.find_element_by_id("auth-signin-button").click()
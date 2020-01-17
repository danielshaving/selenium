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
browser.get('https://seller.cdiscount.com/login')
# 找到亚马逊主页切换语言的element。
browser.find_element_by_id("Login").clear()
browser.find_element_by_id("Password").clear()

# inputemail = input("请输入账号：")
# inputpassword = input("请输入密码：")

inputemail = "danielshaving"
inputpassword = "Abc&1234567895"

browser.find_element_by_id("Login").send_keys(inputemail)
browser.find_element_by_id("Password").send_keys(inputpassword)

browser.find_element_by_id("save").click()

try:
    element = browser.find_element_by_xpath("//div[@class='modal-backdrop fade in']")
    browser.execute_script("arguments[0].style.visibility='hidden'", element)
    browser.find_element_by_id("chartCmdInProgressBtn").click()
except:
    element = browser.find_element_by_xpath("//div[@class='modal fade popinInfo  in']")
    browser.execute_script("arguments[0].style.visibility='hidden'", element)
    browser.find_element_by_id("chartCmdInProgressBtn").click()


all_confirmer_expediteurs = browser.find_elements_by_link_text("Confirmer l'expédition")
for confirmer_expedition in all_confirmer_expediteurs:
    confirmer_expedition.click()
    ele = browser.find_element_by_class_name("panel-collapse")
    screenshot = browser.get_screenshot_as_file('png1.png')

#browser.find_element_by_id("19326406-6ffb-47c4-8299-4c00fc3bd752").click()
# try:
#     browser.find_element_by_id("19326406-6ffb-47c4-8299-4c00fc3bd752").click()
#     browser.find_element_by_id("chartCmdInProgressBtn").click()
# except:
#     browser.find_element_by_id("chartCmdInProgressBtn").click()
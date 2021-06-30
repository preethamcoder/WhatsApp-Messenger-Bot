import time, requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait

#contact = input("Enter the contact name: ")
#message = input("Enter the message you want to send: ")

url = "https://web.whatsapp.com"

driver = webdriver.Chrome(executable_path='C:\\Users\\sthelluri1\\Desktop\\Python Programs\\chromedriver_win32\\chromedriver.exe')
driver.get(url)

#Finding the search bar and looking up the contact
def find_contact(contact):
    inp_xpath_search = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    input_box_search = WebDriverWait(driver, 50).until(
        lambda driver: driver.find_element_by_xpath(inp_xpath_search))
    #clicks on search bar
    input_box_search.click()
    time.sleep(0)
    try:
        #Enters name of contact
        input_box_search.send_keys(contact)
        time.sleep(0.8)
        #Finds contact
        selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
        selected_contact.click()
    except Exception as e:
        print("Invalid contact name, dummy!")

#Finding the messageing box using this command
def send_message(contact, message):
    try:
        inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
        input_box = driver.find_element_by_xpath(inp_xpath)
        time.sleep(0.2)
        #Enters message
        input_box.send_keys(message + Keys.ENTER)
        time.sleep(0)
        print(f"You said '{message}' to {contact}.")
    except Exception as e:
        print("This is not possible!")

#Defining the spam feature
def spam(contact, message):
    print("This is the beginning of the spam process!!!!!! Brace yourselves!")
    repeat = int(input("Enter the number of times you want to send the message: "))
    for i in range(repeat):
        send_message(contact, f'{message}')

#Defining the feature that interacts with the user
def spam_or_message():
    contact = input("Enter the contact name: ")
    message = input("Enter the message you want to send: ")
    action = input("Do you want to MESSAGE or SPAM the person? (M/S)")
    if(action == 'M' or action == 'm'):
        find_contact(contact)
        send_message(contact, f'{message}')
    elif(action == 'S' or action == 's'):
        find_contact(contact)
        spam(contact, message)

spam_or_message()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def open_wp():
    browser=webdriver.Chrome()

    browser.get("https://web.whatsapp.com/")
    print(">>>press enter after you scan the qr code.")
    input()
    return browser
    

def search_person(browser):
    search_box = browser.find_element(
        By.XPATH, "//div[@contenteditable='true' and @data-tab='3']"
    )
    search_box.click()

    while True:
        person = input(">>>put the person name you want to send message: ")


        search_box.send_keys(Keys.CONTROL, "a") #burda searchboz ı temizlemek için öyle bir şey yapıyoruz
        search_box.send_keys(Keys.DELETE)



        for char in person:
            search_box.send_keys(char)
            time.sleep(0.05)

        try:
            find_person = browser.find_element(
                By.XPATH,
                f"//div[@role='gridcell' and @aria-colindex='2']//span[@title='{person}']/ancestor::div[@role='gridcell']"
            )
            find_person.click()

            return person   
        except:
            print("person not found, try again")
            time.sleep(0.5)



def send_message(browser,person):

    while True:
        message=input(">>>put the message you want to send: ")
        while True:
            try:
                count=int(input(">>>How many times do you want to send? "))
                break
            except ValueError:
                print("only integer numbers.")

        if message.strip()=="" or count<=0:
            print("message or count can't be null!")
            continue

        else:
            a=1

            for i in range(count):

                message_box=browser.find_element(By.XPATH,"//div[@contenteditable='true' and @data-tab='10']")

                message_box.click()
                
                message_box.send_keys(f"{a}-{message}")

                send_button=browser.find_element(By.XPATH,"//footer//button[@type='button' and @data-tab='11']")

                send_button.click()

                a+=1

                time.sleep(0.02)

        time.sleep(4)
        break

    print("All messages sent succesfully...")
    

def main():
    browser=open_wp()

    person=search_person(browser)

    send_message(browser,person)



if __name__=="__main__":
    main()


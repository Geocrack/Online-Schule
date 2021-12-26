from selenium import webdriver
import datetime
import time
import pyautogui
import base64                                                        #temp
from  threading import Thread
import keyboard
import sys


moodle = ["https://moodle.humpis-schule.rv.schule-bw.de/moodle/my/"]
englisch = ["https://moodle.humpis-schule.rv.schule-bw.de/moodle/course/view.php?id=1642","https://moodle.humpis-schule.rv.schule-bw.de/moodle/mod/bigbluebuttonbn/view.php?id=54845"]
deutsch = ["https://moodle.humpis-schule.rv.schule-bw.de/moodle/course/view.php?id=1577","https://moodle.humpis-schule.rv.schule-bw.de/moodle/mod/bigbluebuttonbn/view.php?id=53903"]
mathe = ["https://moodle.humpis-schule.rv.schule-bw.de/moodle/course/view.php?id=1585","https://moodle.humpis-schule.rv.schule-bw.de/moodle/mod/bigbluebuttonbn/view.php?id=53967"]
bwl = ["https://moodle.humpis-schule.rv.schule-bw.de/moodle/course/view.php?id=545","https://moodle.humpis-schule.rv.schule-bw.de/moodle/mod/bigbluebuttonbn/view.php?id=6415"]
fm_1 = ["https://moodle.humpis-schule.rv.schule-bw.de/moodle/course/view.php?id=770","https://moodle.humpis-schule.rv.schule-bw.de/moodle/mod/bigbluebuttonbn/view.php?id=8317"]
fm_2 = ["https://moodle.humpis-schule.rv.schule-bw.de/moodle/course/view.php?id=208","https://moodle.humpis-schule.rv.schule-bw.de/moodle/mod/bigbluebuttonbn/view.php?id=3706"]
ggk = ["https://moodle.humpis-schule.rv.schule-bw.de/moodle/course/view.php?id=878","https://moodle.humpis-schule.rv.schule-bw.de/moodle/mod/bigbluebuttonbn/view.php?id=9156"]
religion = ["https://moodle.humpis-schule.rv.schule-bw.de/moodle/course/view.php?id=1239","https://moodle.humpis-schule.rv.schule-bw.de/moodle/mod/bigbluebuttonbn/view.php?id=14304"]
informatik = ["https://moodle.humpis-schule.rv.schule-bw.de/moodle/course/view.php?id=1598","https://moodle.humpis-schule.rv.schule-bw.de/moodle/mod/bigbluebuttonbn/view.php?id=54071"]
physik = ["https://moodle.humpis-schule.rv.schule-bw.de/moodle/course/view.php?id=1625","https://moodle.humpis-schule.rv.schule-bw.de/moodle/mod/bigbluebuttonbn/view.php?id=54726"]

i = 0
schluss = False
lookup = None
stunden = [7.27 ,8.12, 9.17, 10.02, 11.02, 11.47, 12.40, 13.28, 14.12, 15.07, 15.57]
montag = ["",deutsch, deutsch, englisch, englisch, bwl, mathe, "", fm_2, fm_2]
dienstag = ["", fm_1, fm_1, englisch, ggk, religion, religion]
mittwoch = ["", "", "", deutsch, mathe, mathe, englisch, "", physik, physik]
donnerstag = ["", "", "", ggk, mathe, bwl, bwl]
freitag = ["", deutsch, bwl, informatik, informatik, bwl, bwl]

name = ""
password = base64.b64decode("").decode("utf-8")         #temp   
 
#Chrome öffnen
driver = webdriver.Chrome("chromedriver.exe")
pyautogui.keyDown('ctrl')
pyautogui.press('w')
pyautogui.keyUp('ctrl')
driver.maximize_window()

#peüfen ob man den Driver schließen möchte
def schliesen():
    global schluss
    while True:
        if keyboard.is_pressed("#"):
            schluss = True
            driver.close()
            driver.quit()  
            sys.exit()                 
thread_1 = Thread(target = schliesen)
thread_1.start()

#Moodle anmelden
driver.execute_script('window.open("{}","_blank");'.format(moodle[0]))
driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_id("username").send_keys(name)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("loginbtn").click()
time.sleep(1)
driver.close()
driver.switch_to.window(driver.window_handles[-1])

#öffnen
def opentab(temp):
    global i, lookup
    if temp == lookup:
        return
    lookup = temp
    for x in range(i - 1):
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.get(temp[0])
    i = 0
    while True:
        try:
            print(temp[i + 1])
            i += 1
            driver.execute_script('window.open("{}","{}");'.format(temp[i], i))
            driver.switch_to.window(driver.window_handles[i])
        except:
            try:
                driver.switch_to.window(driver.window_handles[i + 1])
            except:
                pass
            return       
        
#abfragen
while True:
    if schluss:
        sys.exit()
    wochentag = int(datetime.datetime.now().strftime("%w"))
    stunde = float(datetime.datetime.now().strftime("%H"))
    minute = float(datetime.datetime.now().strftime("%M"))
    uhrzeit = (minute/100) + stunde
    t = 0
    for s in stunden:
        t += 1
        try:
            if s == uhrzeit:
                if wochentag == 1:
                    opentab(montag[t])
                elif wochentag == 2:
                    opentab(dienstag[t])
                elif wochentag == 3:
                    opentab(mittwoch[t])
                elif wochentag == 4:
                    opentab(donnerstag[t])
                elif wochentag == 5:
                    opentab(freitag[t])  
        except:
            break  
    time.sleep(40)

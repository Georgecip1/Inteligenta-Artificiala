import pyautogui
import keyboard
import time


def cautare_google():
    if pyautogui.locateOnScreen(r'C:\Users\gdanc\Desktop\inteligenta artificiala\ssSearchBar.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(
            r'C:\Users\gdanc\Desktop\inteligenta artificiala\ssSearchBar.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(2)
        pyautogui.write("https://www.youtube.com")
        pyautogui.press('enter')
        time.sleep(5)
        if pyautogui.locateOnScreen(r'C:\Users\gdanc\Desktop\inteligenta artificiala\ssYtSearch.png', confidence=0.7):
            camp_youtube = pyautogui.locateOnScreen(
                r'C:\Users\gdanc\Desktop\inteligenta artificiala\ssYtSearch.png', confidence=0.7)
            pyautogui.click(camp_youtube)
            time.sleep(3)
            pyautogui.write("androssini")
            pyautogui.press('enter')
            time.sleep(5)
            if pyautogui.locateOnScreen(r'C:\Users\gdanc\Desktop\inteligenta artificiala\ssAndrossini.png', confidence=0.7):
                click_poza = pyautogui.locateOnScreen(
                    r'C:\Users\gdanc\Desktop\inteligenta artificiala\ssAndrossini.png', confidence=0.7)
                time.sleep(5)
                pyautogui.click(click_poza)
                time.sleep(5)
                if pyautogui.locateOnScreen(r'C:\Users\gdanc\Desktop\inteligenta artificiala\ssVideos.png', confidence=0.7):
                    click_subscribe = pyautogui.locateOnScreen(
                        r'C:\Users\gdanc\Desktop\inteligenta artificiala\ssVideos.png', confidence=0.7)
                    time.sleep(3)
                    pyautogui.click(click_subscribe)
                    time.sleep(5)
    else:
        print("IMAGINEA NU SE AFLA PE ECRAN")


def coordonate():
    print(pyautogui.position())


time.sleep(5)
# cautare_google()
coordonate()

# x = 571, y = 599, x = 871, y = 599
# x =

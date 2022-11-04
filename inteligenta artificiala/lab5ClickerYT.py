import pyautogui
import keyboard
import time


def clicker_youtube():
    if pyautogui.locateOnScreen(r'C:\Users\gdanc\Desktop\inteligenta artificiala\ssSearchBar.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(
            r'C:\Users\gdanc\Desktop\inteligenta artificiala\ssSearchBar.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(2)
        pyautogui.write("https://www.youtube.com/c/ZonaitTvro")
        pyautogui.press('enter')
        time.sleep(5)
        if pyautogui.locateOnScreen(r'C:\Users\gdanc\Desktop\inteligenta artificiala\ssVideos.png', confidence=0.7):
            videos = pyautogui.locateOnScreen(
                r'C:\Users\gdanc\Desktop\inteligenta artificiala\ssVideos.png', confidence=0.7)
            pyautogui.click(videos)
            time.sleep(3)
    else:
        print("IMAGINEA NU SE AFLA PE ECRAN")
    for i in range(3):
        pyautogui.scroll(-350)
        time.sleep(0.2)
        x = 592
        y = 411
        v = 0
        for v in range(4):

            pyautogui.keyDown('CTRL')
            pyautogui.click(x, y)
            pyautogui.keyUp('CTRL')
            time.sleep(0.2)
            x += 300
            v += 1
    i += 1


# def vizualizare():
#     for i in range(3):
#         pyautogui.scroll(-350)
#         x = 592
#         y = 411
#         v = 0
#         for v in range(4):
#             pyautogui.keyDown('CTRL')
#             pyautogui.click(x, y)
#             pyautogui.keyUp('CTRL')
#             x += 300
#             v += 1
#     i += 1


# def coordonate():
#     time.sleep(2)
#     print(pyautogui.position())


time.sleep(2)
clicker_youtube()
# coordonate()
# vizualizare()

# x = 592, y = 386, x = 874
# 282
# x =

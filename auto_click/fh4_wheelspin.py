# coding: utf-8
import time

import pyautogui
from pyautogui import locateCenterOnScreen


def loc_img(img):
    location = locateCenterOnScreen(img, grayscale=True)
    if location is not None:
        return location.x, location.y
    else:
        return None


def wait_to_click(img):
    while not loc_img(img):
        time.sleep(1)
    pyautogui.click(loc_img(img))


def main():
    while True:
        # pyautogui.click(loc_img('1.png'))
        if loc_img('enter.png'):
            pyautogui.press('enter')
        time.sleep(1)


if __name__ == '__main__':
    main()

import time

import pyautogui
import keyboard
import win32gui


def focus_outside_window(name):
    toplist = []
    winlist = []

    def enum_callback(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

    win32gui.EnumWindows(enum_callback, toplist)
    foreground_window = [(hwnd, title) for hwnd, title in winlist if name in title.lower()]
    foreground_window = foreground_window[0]
    win32gui.SetForegroundWindow(foreground_window[0])


def select_color(hex_code):
    focus_outside_window("file explorer")
    time.sleep(0.06)
    pyautogui.click(1439, 1110)
    pyautogui.leftClick()
    focus_outside_window("file explorer")
    pyautogui.moveTo(1439, 993)
    pyautogui.leftClick()
    pyautogui.leftClick()
    keyboard.write(hex_code)
    time.sleep(0.06)
    pyautogui.moveTo(1774, 726)
    focus_outside_window("file explorer")
    time.sleep(0.06)
    pyautogui.leftClick()
    pyautogui.leftClick()


def paint_at(x, y):
    if y == 0:
        if x == 0:
            focus_outside_window("file explorer")
            pyautogui.moveTo(882, 223)
            pyautogui.leftClick()
            pyautogui.leftClick()
        else:
            focus_outside_window("file explorer")
            pyautogui.moveTo((x * 25.61290322580645 + 882), 223)
            pyautogui.leftClick()
            pyautogui.leftClick()
    else:
        if x == 0:
            focus_outside_window("file explorer")
            pyautogui.moveTo(882, (y * 25.93548387096774 + 223))
            pyautogui.leftClick()
            pyautogui.leftClick()
        else:
            focus_outside_window("file explorer")
            pyautogui.moveTo((x * 25.61290322580645 + 882), (y * 25.93548387096774 + 223))
            pyautogui.leftClick()
            pyautogui.leftClick()

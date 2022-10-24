from numpy import vectorize
import pyautogui as pgui
import time

# GUIポジションでx,y座標を取得して代入
X_POS = 227
Y_POS = 576

# 指定した座標をクリック
pgui.click(X_POS, Y_POS)


while(True):
    print('60秒毎にaを入力')
    # pgui.click()
    pgui.typewrite('a')
    time.sleep(60)

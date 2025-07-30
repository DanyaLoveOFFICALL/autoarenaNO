import pyautogui
import time
import keyboard

tabs = ["gonyaw.png", "xqanke.png", "xqnaxuser.png"]
rank_battle_img = "rank_battle.png"
confirm_imgs = ["confirm1.png", "confirm2.png", "confirm3.png"]
delay_between_tabs = 0.5

CONFIDENCE = 0.7
GRAYSCALE = True

def safe_locate(image, conf=CONFIDENCE, gray=GRAYSCALE):
    try:
        return pyautogui.locateCenterOnScreen(image, confidence=conf, grayscale=gray)
    except Exception as e:
        print(f"❌ Ошибка при поиске {image}: {e}")
        return None

def try_click_once(image):
    loc = safe_locate(image)
    if loc:
        pyautogui.moveTo(loc)
        pyautogui.click()
        print(f"✅ Клик по: {image}")
        return True
    return False

def try_any_click_once(images):
    for img in images:
        loc = safe_locate(img)
        if loc:
            pyautogui.moveTo(loc)
            pyautogui.click()
            print(f"✅ Клик по Confirm: {img}")
            return True
    return False

print("🚀 Ускоренный цикл арены запущен (нажми NumPad3 чтобы остановить)")

while True:
    if keyboard.is_pressed('num 3'):
        print("🛑 Выход по NumPad3")
        break

    for tab in tabs:
        if keyboard.is_pressed('num 3'):
            print("🛑 Выход по NumPad3")
            break

        print(f"\n🔄 Переключаюсь на вкладку: {tab}")
        tab_loc = safe_locate(tab)
        if tab_loc:
            pyautogui.click(tab_loc)
            time.sleep(0.7)

            clicked = False

            if try_any_click_once(confirm_imgs):
                clicked = True
            elif try_click_once(rank_battle_img):
                clicked = True

            if clicked:
                print("➡️ Нашёл кнопку, идём дальше.")
            else:
                print("🕵️ Ничего не нашёл.")
        else:
            print(f"❌ Вкладка {tab} не найдена.")

        time.sleep(delay_between_tabs)

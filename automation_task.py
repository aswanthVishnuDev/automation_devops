import win32gui
import pyautogui
import asyncio

async def find_window_by_title(title):
    print('entry check')
    def enum_windows_callback(hwnd, titles):        
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            if title.lower() in window_title.lower():
                titles.append(hwnd)
        
    titles =[]
    win32gui.EnumWindows(enum_windows_callback, titles)
    return titles


async def wait_for_window(title, check_interval=1, no_tries=5):
    print(f'Waiting for title {title} to appear...')
    count = 0
    found_windows_with_title = await find_window_by_title(title)
    while title not in found_windows_with_title:
        count = count +1 
        await asyncio.sleep(check_interval)
        if count > no_tries:
            return
    print(f'Window {title} detected')
    return

async def automate_typing():
    print(f'performing automation')
    await asyncio.sleep(1)
    pyautogui.write('Hello World!')
    await asyncio.sleep(1)
    pyautogui.press('enter')
    await asyncio.sleep(1)
    pyautogui.write('This text was written by a Python automation script')
    return

async def save_file():
    print("Saving file ...")
    await asyncio.sleep(1)
    pyautogui.hotkey('ctrl', 's')
    await asyncio.sleep(1)
    pyautogui.write('automated_output')
    await asyncio.sleep(1)
    pyautogui.press('enter')
    print("Notepad is saved sucessfully")
    return

async def main():
    print(f'Launching Notepad')
    pyautogui.hotkey('win', 'r')
    pyautogui.write('wordpad')
    pyautogui.press('enter')
    await asyncio.sleep(1)
    pyautogui.press('enter')

    await wait_for_window('Document')

    await automate_typing()
    await save_file()

if __name__ == "__main__":
    asyncio.run(main())

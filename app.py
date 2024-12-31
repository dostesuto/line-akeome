import time
import datetime
import pyautogui

# 送信するメッセージと送信時刻を設定
message = "あけおめ！"  # 送信するメッセージ
send_time = datetime.datetime(2024, 1, 1, 0, 0, 0)  # 送信時刻

# テキストボックスの座標を指定（LINEのテキストボックスの位置）
textbox_position = (417, 989)  # 指定された座標

# 指定時間まで待機
while True:
    current_time = datetime.datetime.now()
    if current_time >= send_time:
        break
    time.sleep(1)  # 1秒待機

# メッセージを入力・送信
pyautogui.click(textbox_position)  # テキストボックスをクリックしてカーソルをアクティブ化
time.sleep(0.5)  # クリック後の安定のため少し待つ

# 入力動作を再現
for char in message:
    pyautogui.typewrite(char)  # 1文字ずつ入力
    time.sleep(0.05)  # 入力速度を調整（自然な感じにする）
pyautogui.press("enter")  # Enterキーを押して送信

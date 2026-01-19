import requests
import time
import os
import sys

# Clear screen
os.system("clear")

# Colors
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
C = "\033[1;36m"
W = "\033[0m"

# Slow print
def slow(text, speed=0.03):
    for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Banner
slow(f"""{C}
███╗   ███╗     ██╗██╗  ██╗
████╗ ████║     ██║██║  ██║
██╔████╔██║     ██║███████║
██║╚██╔╝██║██   ██║██╔══██║
██║ ╚═╝ ██║╚█████╔╝██║  ██║
╚═╝     ╚═╝ ╚════╝ ╚═╝  ╚═╝
{Y}      MJH FAST TOOLS v2.0
{C}  Professional API Testing System
{W}
╔════════════════════════════════════╗
║ Credit : Jihan (MJH)               ║
║ Max Request Limit : 15             ║
║ Platform : Termux / Python         ║
╚════════════════════════════════════╝
""", 0.002)

slow(f"{Y}[!] Educational & Legal Use Only\n{W}")

print(f"{G}🔗 Join our Telegram Channel:{W}")
print(f"{C}https://t.me/scripthvi{W}\n")

# API Config
API_URL = "https://api.jubairbro.store/api"
API_KEY = "jubairff"
MAX_LIMIT = 15
DELAY = 1

# Input section
number = input(f"{Y}📱 Enter target number (with permission): {W}")

if not number.startswith("01") or len(number) < 11:
    print(f"{R}❌ Invalid Bangladeshi number format!{W}")
    exit()

try:
    amount = int(input(f"{Y}🔢 Enter request amount (max 15): {W}"))
except:
    print(f"{R}❌ Invalid input!{W}")
    exit()

if amount < 1 or amount > MAX_LIMIT:
    print(f"{R}❌ Limit exceeded! Max = 15{W}")
    exit()

print(f"\n{C}🚀 Initializing API Test...\n{W}")
time.sleep(1)

success = 0
failed = 0

try:
    for i in range(amount):
        params = {
            "key": API_KEY,
            "num": number
        }
        r = requests.get(API_URL, params=params, timeout=10)

        if r.status_code == 200:
            success += 1
            print(f"{G}[{i+1}/{amount}] ✅ Request Sent Successfully{W}")
        else:
            failed += 1
            print(f"{R}[{i+1}/{amount}] ❌ Failed | Status {r.status_code}{W}")

        time.sleep(DELAY)

except KeyboardInterrupt:
    print(f"\n{R}⚠ Interrupted by user!{W}")

# Summary
print(f"\n{B}═══════════ TEST SUMMARY ═══════════{W}")
print(f"{G}✔ Successful Requests : {success}{W}")
print(f"{R}✖ Failed Requests     : {failed}{W}")
print(f"{Y}📊 Total Attempts      : {success + failed}{W}")
print(f"{B}═════════════════════════════════════{W}")

print(f"\n{C}✨ Thanks for using MJH Fast Tools ✨{W}")
print(f"{Y}👑 Coded by Jihan (MJH){W}")

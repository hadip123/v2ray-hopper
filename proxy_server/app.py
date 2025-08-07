import subprocess
from dotenv import load_dotenv
import random
import os
import time
import requests

load_dotenv()

print(os.getenv("CONFIGS_DIR"))
print(os.getenv("PATHS_DIR"))


proxy = "socks5://127.0.0.1:10808"


def choose_config_file():
    print("CHOOSING THE CONFIG FILE")
    configs = os.listdir(os.getenv("PATHS_DIR"))
    configs.sort()
    f = open(f"{os.getenv("PATHS_DIR")}/{configs[0]}", "r")
    configs = f.readlines()
    random.shuffle(configs)
    return f"{os.getenv("CONFIGS_DIR")}/{configs[0]}".rstrip()


process = subprocess.Popen(
    ["v2ray", "run", "-c", choose_config_file()])

while True:
    try:
        res = requests.get("https://icanhazip.com",
                           proxies=dict(https=proxy, http=proxy))
    except Exception as e:
        print(e)
        process.kill()
        process = subprocess.Popen(
            ["v2ray", "run", "-c", choose_config_file()])
        time.sleep(3)
        continue
    time.sleep(10)

process.kill()

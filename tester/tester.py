import subprocess
import os
import time
from datetime import datetime
import random

import requests

config_files = os.listdir("configs/")
random.shuffle(config_files)

http_proxy = "socks5://127.0.0.1:10808"
https_proxy = "socks5://127.0.0.1:10808"

working_configs = []
dt = datetime.now()
formatted_date = dt.strftime("%Y_%m_%d__%H_%M_%S")
for config_file in config_files:
    print(f"TESTING {config_file}")
    process = subprocess.Popen(
        ["v2ray", "run", "-c", f"./configs/{config_file}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for line in process.stdout:
        if ("started" in line):
            break

    print("REQUESTING")

    try:
        response = requests.get(
            "https://icanhazip.com", proxies=dict(http=http_proxy, https=https_proxy), timeout=2)
        print(response.text)
        print("-----------------WORKED-------" + config_file)
        f = open(f"./wcp/working_configs_paths_{formatted_date}.txt", "a")
        f.write(config_file + "\n")
        f.close()

        working_configs.append(config_file)
    except Exception as e:
        print(e)
        continue
    finally:
        process.kill()

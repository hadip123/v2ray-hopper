import subprocess
import os
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

TEST_URL = os.getenv("TEST_URL") if os.getenv(
    "TEST_URL") is not None else "https://youtube.com"
ANTI_403 = os.getenv("ANTI_403") if os.getenv(
    "ANTI_403") is not None else "false"

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
            TEST_URL, proxies=dict(http=http_proxy, https=https_proxy), timeout=1)
        elapsed = response.elapsed.total_seconds() * 1000
        if ANTI_403 == "true" and response.status_code == 403:
            print("XXXXXXXX--403--XXXXXXXXXX")
            continue
        print(
            f"-----------------STATUS CODE -> {response.status_code} REACHED in {elapsed}ms-----------------" + config_file)

        f = open(f"./wcp/working_configs_paths_{formatted_date}.txt", "a")
        f.write(config_file + "\n")
        f.close()

        working_configs.append(config_file)
    except Exception as e:
        print(e)
        continue
    finally:
        process.kill()

import subprocess
import os
from time import sleep

import requests

config_files = os.listdir("configs/")

http_proxy = "socks5://127.0.0.1:10808"
https_proxy = "socks5://127.0.0.1:10808"

working_configs = []
f = open("./working_configs_paths.txt", "w")
for config_file in config_files:
    print(f"TESTING {config_file}")
    process = subprocess.Popen(
        ["v2ray", "run", "-c", f"./configs/{config_file}"])

    sleep(1)

    print("REQUESTING")

    try:
        response = requests.get(
            "https://icanhazip.com", proxies=dict(http=http_proxy, https=https_proxy), timeout=2)
        print(response.body)
        f.write(config_file)

        working_configs.append(config_file)
    except Exception as e:
        print(e)
        continue
    finally:
        process.kill()

f.close()

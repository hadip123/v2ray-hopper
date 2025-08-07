## V2Ray hopper

It collects the configs from [here](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/refs/heads/main/Config/vless.txt), runs some checks, then with the proxy_server hosts a socks5 server that changes its config file when there's a problem with the current configuration.
> It's still being developed

## Usage
#### Cloning the repository
```bash
git clone https://github.com/hadip123/v2ray-hopper.git
cd v2ray-hopper/
```
#### Creating the docker image
First, an environment should be created, there's a `Dockerfile` in the `environment_docker_image`.
```bash
docker build -t v2ray-hopper environment_docker_image/
```
#### Gattering the config files and testing them
There's a script in the `/app` direcotry in the docker image created.
```bash
docker run -it --network=host --rm -v ./:/app v2ray-hopper "/app/gattc"
```
#### Running the proxy server
- with docker compose
```bash
docker compose up -d
```
- w/o docker compose
```bash
docker run --name vhopper -d --network=host -v ./:/app -e PATHS_DIR=/app/tester/wcp -e CONFIGS_DIR=/app/tester/configs v2ray-hopper:latest "/app/entrypoint"
```
Now proxy is up and running on socks5://<your_host>:10808
#### Restarting the server
```bash
docker restart vhopper
```
#### Stopping the server
```bash
docker stop vhopper
docker rm vhopper
```

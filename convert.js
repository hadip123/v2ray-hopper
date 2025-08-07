import url from 'url'
export function convert(link) {
	const parsedUrl = url.parse(link, true);

	const configObj =
	{
		"dns": {
			"hosts": {
				"domain:googleapis.cn": "googleapis.com"
			},
			"servers": [
				"1.1.1.1"
			]
		},
		"inbounds": [
			{
				"listen": "127.0.0.1",
				"port": 10808,
				"protocol": "socks",
				"settings": {
					"auth": "noauth",
					"udp": true,
					"userLevel": 8
				},
				"sniffing": {
					"destOverride": [
						"http",
						"tls"
					],
					"enabled": true
				},
				"tag": "socks"
			},
			{
				"listen": "127.0.0.1",
				"port": 10809,
				"protocol": "http",
				"settings": {
					"userLevel": 8
				},
				"tag": "http"
			}
		],
		"log": {
			"loglevel": "warning"
		},
		"outbounds": [
			{
				"mux": {
					"concurrency": 8,
					"enabled": false
				},
				"protocol": "vless",
				"settings": {
					"vnext": [
						{
							"address": parsedUrl.hostname,
							"port": parseInt(parsedUrl.port),
							"users": [
								{
									"encryption": "none",
									"flow": "",
									"id": parsedUrl.auth,
									"level": 8,
									"security": "auto"
								}
							]
						}
					]
				},
				"streamSettings": {
					"grpcSettings": {
						"multiMode": false,
						"serviceName": parsedUrl.query.serviceName
					},
					"network": parsedUrl.query.type,
					"security": parsedUrl.query.security,
					"tlsSettings": {
						"allowInsecure": false,
						"alpn": [
							parsedUrl.query.alpn
						],
						"serverName": parsedUrl.query.sni
					}
				},
				"tag": "proxy"
			},
			{
				"protocol": "freedom",
				"settings": {},
				"tag": "direct"
			},
			{
				"protocol": "blackhole",
				"settings": {
					"response": {
						"type": "http"
					}
				},
				"tag": "block"
			}
		],
		"routing": {
			"domainMatcher": "mph",
			"domainStrategy": "IPIfNonMatch",
			"rules": [
				{
					"ip": [
						"1.1.1.1"
					],
					"outboundTag": "proxy",
					"port": "53",
					"type": "field"
				}
			]
		}
	};

	return configObj;
}

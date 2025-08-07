import axios from "axios"
import { convert } from "./convert.js"
import fs from "fs"

let response = await axios.get("https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/refs/heads/main/Config/vless.txt")

const configList = response.data.split("\n")

let count = 0;
configList.map((config) => {
	count++;
	const configObj = convert(config)
	const configJson = JSON.stringify(configObj, null, 4);


	fs.writeFileSync(`configs/config_${count}.json`, configJson);

	console.log(`${count} DONE`)
})


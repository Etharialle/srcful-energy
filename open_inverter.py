import requests
import os
import yaml
from dotenv import load_dotenv

load_dotenv(override=True)
srcful_ip = os.getenv("SRCFUL_IP_ADDRESS")
url = f"http://{srcful_ip}/api/device"

headers = {
    "Content-Type": "application/json"
    #"Authorization": f"Bearer {token}"
}

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        yaml_data = yaml.dump(data, sort_keys=False, default_flow_style=False)
        #with open("output.yaml", "w") as yaml_file:
        #    yaml_file.write(yaml_data)
        print(yaml_data)
    else:
        print(f"Failed to fetch data: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")

import requests
import yaml
from dotenv import load_dotenv
import os
load_dotenv(override=True)

envoy_ip = os.getenv("ENPHASE_IP_ADDRESS")
url = f"http://{envoy_ip}/ivp/livedata/status"
# Endpoints
# /production.json
# /ivp/ensemble/inventory
# /ivp/ensemble/secctrl
# /ivp/livedata/status


token = os.getenv("ENPHASE_TOKEN")
headers = {
    "Authorization": f"Bearer {token}"
}

try:
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()
        yaml_data = yaml.dump(data, sort_keys=False, default_flow_style=False)
        with open("output.yaml", "w") as yaml_file:
            yaml_file.write(yaml_data)
        print(yaml_data)
    else:
        print(f"Failed to fetch data: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")

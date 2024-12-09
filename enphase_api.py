import requests
import yaml
from dotenv import load_dotenv
import os


load_dotenv(override=True)

envoy_ip = "192.168.4.57"  # Replace with your Envoy's IP address
url = f"http://{envoy_ip}/ivp/ensemble/inventory"
token = os.getenv("ENPHASE_TOKEN")

headers = {
    "Authorization": f"Bearer {token}"
}

try:
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()
        #max_capacity = data["battery"][0].get("maximumCapacity", None)
        #if max_capacity:
        #    print(f"Battery Maximum Capacity: {max_capacity / 1000} kWh")
        #else:
        #    print("Maximum capacity field not found in response.")
        yaml_data = yaml.dump(data, sort_keys=False, default_flow_style=False)
        with open("inventory.yaml", "w") as yaml_file:
            yaml_file.write(yaml_data)
        print(yaml_data)
    else:
        print(f"Failed to fetch data: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")

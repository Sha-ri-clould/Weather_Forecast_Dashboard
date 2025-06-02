import requests
import os
API_KEY= os.environ.get("API_KEY")


def get_data(name, days=None, type=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={name}&appid={API_KEY}"
    response = requests.get(url)
    contents = response.json()
    filtered_data = contents['list']
    n_value = 8 * days
    filtered_data =  filtered_data[:n_value]

    if type == "Temperature":
        filtered_data = [data["main"]["temp"]for data in filtered_data]
    if type == "Sky":
        filtered_data = [data["weather"][0]["main"] for data in filtered_data]
    return filtered_data

if __name__ == "__main__":
    print(get_data(name="London",days=3,type="Sky"))
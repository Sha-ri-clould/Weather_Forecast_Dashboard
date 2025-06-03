import requests
API_KEY= "55ed09cccf55385d2af90eeeecaaa6f4"



def get_data(name, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={name}&appid={API_KEY}"
    response = requests.get(url)
    contents = response.json()
    filtered_data = contents['list']
    n_value = 8 * days
    filtered_data =  filtered_data[:n_value]
    return filtered_data

if __name__ == "__main__":
    print(get_data(name="London",days=3))
import requests

def get_train_locations():
    url = "https://rata.digitraffic.fi/api/v1/train-locations/latest/"
    headers = {
        'Digitraffic-User': 'YourAppName/1.0'
    }
    print(f"Fetching data from {url}...")
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print("Data fetched successfully!")
        return data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

if __name__ == "__main__":
    train_locations = get_train_locations()
    if train_locations:
        print(train_locations)
    else:
        print("No data received.")
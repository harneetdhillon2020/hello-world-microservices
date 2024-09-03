import requests

def get_hello():
    try:
        response = requests.get('http://localhost:5000/hello')
        response.raise_for_status()  
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching hello: {e}")
        return None

def get_world():
    try:
        response = requests.get('http://localhost:5001/world')
        response.raise_for_status()  
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching world: {e}")
        return None

def main():
    hello = get_hello()
    world = get_world()

    if hello and world:
        print(f"{hello} {world}")
    else:
        print("Failed to retrieve messages.")

if __name__ == "__main__":
    main()

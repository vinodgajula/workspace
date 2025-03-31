import requests

def make_get_request(base_url, number):
    # Define the query parameter
    params = {"number": number}
    
    try:
        # Send a GET request
        response = requests.get(base_url, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print(f"Error {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Base URL of the Flask app
    base_url = "http://localhost:80"
    
    # Test with a sample integer value
    for number  in range(1, 100):
        make_get_request(base_url, number)

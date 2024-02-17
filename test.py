import requests

# Set the base URL for your Flask application
base_url = 'http://127.0.0.1:5000'  # Update this if your Flask app is running on a different address/port

# Function to test retrieving ice cream flavors
def test_get_ice_cream(name):
    url = f"{base_url}/ice_cream?name={name}"
    response = requests.get(url)
    print(response.json())

# Function to test updating ice cream flavors (for admin)
def test_update_flavors(admin_key, flavor, ingredients):
    url = f"{base_url}/update_flavors"
    payload = {
        'admin_key': admin_key,
        'flavor': flavor,
        'ingredients': ingredients
    }
    response = requests.post(url, json=payload)
    print(response.json())

if __name__ == '__main__':
    # Testing retrieving ice cream flavors
    test_get_ice_cream('vanilla')
    test_get_ice_cream('strawberry')
    
    # Testing updating ice cream flavors (requires admin key)
    test_update_flavors('fiZazaeBwX2ul9nh', 'new_flavor', ['milk', 'cream', 'sugar', 'new_ingredient'])

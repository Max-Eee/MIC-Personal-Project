# --Ice Cream Mixer Mini Project--

The Ice Cream Mixer project involves providing an API for managing ice cream flavors. Here's an overview of its functionality:

Retrieve Ice Cream Flavors: Users can query the API to retrieve the ingredients for specific ice cream flavors by providing the name of the flavor. The API returns a list of ingredients required to make the requested ice cream flavor.

Update Ice Cream Flavors (Admin Only): Administrators have the ability to update the ingredients for ice cream flavors. They can send a POST request to the API endpoint along with an admin key for authentication, the name of the flavor to be updated, and the updated list of ingredients. Upon successful authentication and validation, the API updates the ingredients for the specified ice cream flavor.

This project serves as a simple demonstration of building a Flask-based API for managing ice cream flavors. It provides basic functionality for querying and updating ice cream flavors, with authentication for administrative actions to ensure data integrity and security. It can serve as a foundation for further development, such as adding user authentication, input validation, database integration, and more sophisticated functionality for managing and interacting with ice cream flavors.

![image](https://github.com/Max-Eee/MIC-Personal-Project/assets/76102874/2c393f7d-ed59-43ff-bf50-abd9d46e2ad7)

---
# --API Documentation--

## Base URL
```
http://127.0.0.1:5000
```
Replace `127.0.0.1:5000` with the actual address/port where your Flask app is hosted.

## Endpoints

---

### Retrieve Ice Cream Flavors

**URL:** `/ice_cream`

**Method:** GET

**Description:** Retrieves the flavor ingredients for a specific ice cream flavor.

**Parameters:**
- `name` (string, required): The name of the ice cream flavor.

**Response:**
- `200 OK`: Returns JSON object with the ingredients for the specified ice cream flavor.
  ```json
  {
    "ingredients": ["milk", "cream", "sugar", "vanilla extract"]
  }
  ```
- `404 Not Found`: If the provided ice cream flavor name is not found.
  ```json
  {
    "error": "Ice cream not found"
  }
  ```

---

### Update Ice Cream Flavors (Admin Only)

**URL:** `/update_flavors`

**Method:** POST

**Description:** Updates the ingredients for a specific ice cream flavor. This endpoint is accessible only by administrators.

**Request Payload:**
- `admin_key` (string, required): The admin key for authentication.
- `flavor` (string, required): The name of the ice cream flavor to be updated.
- `ingredients` (array of strings, required): The updated list of ingredients for the specified ice cream flavor.

**Response:**
- `200 OK`: If the flavor is updated successfully.
  ```json
  {
    "message": "Flavor vanilla updated successfully"
  }
  ```
- `400 Bad Request`: If the request payload is missing required parameters or contains invalid JSON.
  ```json
  {
    "error": "Missing parameters in request"
  }
  ```
- `403 Forbidden`: If the provided admin key is invalid.
  ```json
  {
    "error": "Invalid admin key"
  }
  ```


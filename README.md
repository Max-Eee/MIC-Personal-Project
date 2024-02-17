# Ice Cream Mixer API Documentation

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



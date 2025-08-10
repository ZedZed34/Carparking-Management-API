# 📖 API Documentation

## Carpark Management API v1

The Carpark Management API provides comprehensive endpoints for managing carpark information, including CRUD operations, filtering, searching, and statistical analysis.

### Base URL
- **Development**: `http://localhost:8000/api/v1/`
- **Production**: `https://your-railway-app.railway.app/api/v1/`

### Authentication
Currently, the API is open and doesn't require authentication. All endpoints are publicly accessible.

---

## 🎯 Quick Start

### Example API Call
```bash
curl -X GET "https://your-railway-app.railway.app/api/v1/carparks/" \
  -H "Accept: application/json"
```

### Response Format
All responses are in JSON format:
```json
{
  "count": 2341,
  "next": "http://localhost:8000/api/v1/carparks/?page=2",
  "previous": null,
  "results": [...]
}
```

---

## 📋 Endpoints Overview

| Endpoint | Method | Description | Parameters |
|----------|---------|-------------|------------|
| [`/carparks/`](#list-all-carparks) | GET | List all carparks (paginated) | `page`, `page_size` |
| [`/carparks/`](#create-carpark) | POST | Create a new carpark | Request body |
| [`/carparks/{id}/`](#get-carpark-details) | GET | Get specific carpark details | `id` |
| [`/carparks/{id}/`](#update-carpark) | PUT/PATCH | Update specific carpark | `id`, Request body |
| [`/carparks/filter/`](#filter-by-type) | GET | Filter carparks by type | `type` |
| [`/carparks/free/`](#filter-free-parking) | GET | Get carparks with free parking | None |
| [`/carparks/search/`](#search-by-address) | GET | Search carparks by address | `address` |
| [`/carparks/group/`](#group-by-parking-system) | GET | Group by parking system | None |
| [`/carparks/average/`](#average-gantry-height) | GET | Get average gantry height | None |
| [`/carparks/height-range/`](#filter-by-height-range) | GET | Filter by gantry height range | `min_height`, `max_height` |
| [`/carparks/types/`](#get-carpark-types) | GET | Get all available carpark types | None |

---

## 📊 Data Models

### CarPark Model

```json
{
  "id": 1,
  "car_park_no": "HDB001",
  "address": "123 Main Street",
  "x_coord": 103.8198,
  "y_coord": 1.3521,
  "car_park_type": "SURFACE CAR PARK",
  "type_of_parking_system": "ELECTRONIC PARKING",
  "short_term_parking": "WHOLE DAY",
  "free_parking": "NO",
  "night_parking": true,
  "car_park_decks": 1,
  "gantry_height": 2.5,
  "car_park_basement": false,
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z",
  "has_free_parking": false,
  "location": [103.8198, 1.3521]
}
```

### Field Descriptions

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `id` | Integer | Unique identifier | Auto-generated |
| `car_park_no` | String | Car park number | Max 100 chars |
| `address` | String | Full address | Max 255 chars |
| `x_coord` | Float | X coordinate | Required |
| `y_coord` | Float | Y coordinate | Required |
| `car_park_type` | String | Type of car park | Max 150 chars |
| `type_of_parking_system` | String | Parking system type | Max 150 chars |
| `short_term_parking` | String | Short term parking info | Max 100 chars |
| `free_parking` | String | Free parking information | Max 100 chars |
| `night_parking` | Boolean | Night parking availability | Default: false |
| `car_park_decks` | Integer | Number of decks | 0-50 |
| `gantry_height` | Float | Gantry height in meters | 0.0-10.0 |
| `car_park_basement` | Boolean | Has basement | Default: false |
| `created_at` | DateTime | Creation timestamp | Auto-generated |
| `updated_at` | DateTime | Last update timestamp | Auto-updated |
| `has_free_parking` | Boolean | Computed free parking flag | Read-only |
| `location` | Array | [x_coord, y_coord] | Read-only |

---

## 🔍 Detailed Endpoint Documentation

### List All Carparks

**GET** `/carparks/`

Returns a paginated list of all carparks.

#### Parameters
- `page` (optional): Page number (default: 1)
- `page_size` (optional): Items per page (default: 50, max: 100)

#### Example Request
```bash
curl -X GET "http://localhost:8000/api/v1/carparks/?page=1&page_size=10"
```

#### Example Response
```json
{
  "count": 2341,
  "next": "http://localhost:8000/api/v1/carparks/?page=2&page_size=10",
  "previous": null,
  "results": [
    {
      "id": 1,
      "car_park_no": "HDB001",
      "address": "123 Main Street",
      "car_park_type": "SURFACE CAR PARK",
      "gantry_height": 2.5,
      "has_free_parking": false,
      "night_parking": true
    }
  ]
}
```

#### Response Codes
- `200 OK`: Success
- `400 Bad Request`: Invalid parameters

---

### Create Carpark

**POST** `/carparks/`

Creates a new carpark entry.

#### Request Body
```json
{
  "address": "456 New Street",
  "car_park_type": "MULTI-STOREY CAR PARK",
  "gantry_height": 3.0,
  "night_parking": true,
  "car_park_decks": 5
}
```

#### Required Fields
- `address`
- `car_park_type`
- `gantry_height`

#### Optional Fields
All other fields are optional and will use default values if not provided.

#### Example Request
```bash
curl -X POST "http://localhost:8000/api/v1/carparks/" \
  -H "Content-Type: application/json" \
  -d '{
    "address": "456 New Street",
    "car_park_type": "MULTI-STOREY CAR PARK",
    "gantry_height": 3.0,
    "night_parking": true
  }'
```

#### Example Response
```json
{
  "id": 2342,
  "car_park_no": "MANUAL-A1B2C3D4",
  "address": "456 New Street",
  "x_coord": 0.0,
  "y_coord": 0.0,
  "car_park_type": "MULTI-STOREY CAR PARK",
  "type_of_parking_system": "ELECTRONIC PARKING",
  "short_term_parking": "NO",
  "free_parking": "NO",
  "night_parking": true,
  "car_park_decks": 0,
  "gantry_height": 3.0,
  "car_park_basement": false,
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z",
  "has_free_parking": false,
  "location": [0.0, 0.0]
}
```

#### Response Codes
- `201 Created`: Successfully created
- `400 Bad Request`: Validation errors
- `409 Conflict`: Duplicate carpark

---

### Get Carpark Details

**GET** `/carparks/{id}/`

Returns detailed information about a specific carpark.

#### Parameters
- `id`: Carpark ID (integer)

#### Example Request
```bash
curl -X GET "http://localhost:8000/api/v1/carparks/1/"
```

#### Example Response
```json
{
  "id": 1,
  "car_park_no": "HDB001",
  "address": "123 Main Street",
  "x_coord": 103.8198,
  "y_coord": 1.3521,
  "car_park_type": "SURFACE CAR PARK",
  "type_of_parking_system": "ELECTRONIC PARKING",
  "short_term_parking": "WHOLE DAY",
  "free_parking": "NO",
  "night_parking": true,
  "car_park_decks": 1,
  "gantry_height": 2.5,
  "car_park_basement": false,
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z",
  "has_free_parking": false,
  "location": [103.8198, 1.3521]
}
```

#### Response Codes
- `200 OK`: Success
- `404 Not Found`: Carpark not found

---

### Update Carpark

**PUT** `/carparks/{id}/` or **PATCH** `/carparks/{id}/`

Updates an existing carpark. Use PUT for full updates, PATCH for partial updates.

#### Parameters
- `id`: Carpark ID (integer)

#### Request Body (PATCH example)
```json
{
  "gantry_height": 3.5,
  "night_parking": false
}
```

#### Example Request
```bash
curl -X PATCH "http://localhost:8000/api/v1/carparks/1/" \
  -H "Content-Type: application/json" \
  -d '{
    "gantry_height": 3.5,
    "night_parking": false
  }'
```

#### Response Codes
- `200 OK`: Successfully updated
- `400 Bad Request`: Validation errors
- `404 Not Found`: Carpark not found

---

### Filter by Type

**GET** `/carparks/filter/`

Filters carparks by their type.

#### Parameters
- `type`: Carpark type (case-insensitive)

#### Example Request
```bash
curl -X GET "http://localhost:8000/api/v1/carparks/filter/?type=SURFACE%20CAR%20PARK"
```

#### Example Response
```json
[
  {
    "id": 1,
    "car_park_no": "HDB001",
    "address": "123 Main Street",
    "car_park_type": "SURFACE CAR PARK",
    "gantry_height": 2.5,
    "has_free_parking": false,
    "night_parking": true
  }
]
```

#### Response Codes
- `200 OK`: Success
- `400 Bad Request`: Missing type parameter

---

### Filter Free Parking

**GET** `/carparks/free/`

Returns carparks that offer free parking.

#### Example Request
```bash
curl -X GET "http://localhost:8000/api/v1/carparks/free/"
```

#### Example Response
```json
[
  {
    "id": 10,
    "car_park_no": "HDB010",
    "address": "789 Free Street",
    "car_park_type": "SURFACE CAR PARK",
    "free_parking": "SUN & PH FR 7AM-10.30PM",
    "has_free_parking": true
  }
]
```

#### Response Codes
- `200 OK`: Success

---

### Search by Address

**GET** `/carparks/search/`

Searches carparks by address (case-insensitive partial match).

#### Parameters
- `address`: Search term for address

#### Example Request
```bash
curl -X GET "http://localhost:8000/api/v1/carparks/search/?address=clementi"
```

#### Example Response
```json
[
  {
    "id": 15,
    "car_park_no": "HDB015",
    "address": "Clementi Avenue 1",
    "car_park_type": "MULTI-STOREY CAR PARK",
    "gantry_height": 2.8
  }
]
```

#### Response Codes
- `200 OK`: Success
- `400 Bad Request`: Missing address parameter

---

### Group by Parking System

**GET** `/carparks/group/`

Returns carparks grouped by their parking system with counts.

#### Example Request
```bash
curl -X GET "http://localhost:8000/api/v1/carparks/group/"
```

#### Example Response
```json
[
  {
    "type_of_parking_system": "ELECTRONIC PARKING",
    "total": 1500
  },
  {
    "type_of_parking_system": "COUPON PARKING",
    "total": 841
  }
]
```

#### Response Codes
- `200 OK`: Success

---

### Average Gantry Height

**GET** `/carparks/average/`

Returns the average gantry height across all carparks.

#### Example Request
```bash
curl -X GET "http://localhost:8000/api/v1/carparks/average/"
```

#### Example Response
```json
{
  "average_height": 2.47
}
```

#### Response Codes
- `200 OK`: Success

---

### Filter by Height Range

**GET** `/carparks/height-range/`

Filters carparks by gantry height range.

#### Parameters
- `min_height`: Minimum height (float)
- `max_height`: Maximum height (float)

#### Example Request
```bash
curl -X GET "http://localhost:8000/api/v1/carparks/height-range/?min_height=2.0&max_height=3.0"
```

#### Example Response
```json
[
  {
    "id": 1,
    "car_park_no": "HDB001",
    "address": "123 Main Street",
    "gantry_height": 2.5
  }
]
```

#### Response Codes
- `200 OK`: Success
- `400 Bad Request`: Missing or invalid height parameters

---

### Get Carpark Types

**GET** `/carparks/types/`

Returns all available carpark types.

#### Example Request
```bash
curl -X GET "http://localhost:8000/api/v1/carparks/types/"
```

#### Example Response
```json
[
  "BASEMENT CAR PARK",
  "COVERED CAR PARK",
  "MECHANISED CAR PARK",
  "MULTI-STOREY CAR PARK",
  "SURFACE CAR PARK"
]
```

#### Response Codes
- `200 OK`: Success

---

## 🚨 Error Handling

### Error Response Format
```json
{
  "error": "Error message",
  "detail": "Detailed error information",
  "field_errors": {
    "field_name": ["Error message for this field"]
  }
}
```

### Common HTTP Status Codes

| Code | Description | Example |
|------|-------------|---------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST |
| 400 | Bad Request | Validation errors, missing parameters |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Duplicate resource |
| 500 | Internal Server Error | Server error |

### Example Error Responses

#### Validation Error (400)
```json
{
  "gantry_height": ["Gantry height cannot be negative."],
  "car_park_type": ["This field is required."]
}
```

#### Not Found Error (404)
```json
{
  "detail": "Not found."
}
```

#### Duplicate Error (409)
```json
{
  "detail": "A car park with similar details already exists."
}
```

---

## 📊 Pagination

All list endpoints support pagination using the following parameters:

### Parameters
- `page`: Page number (starts from 1)
- `page_size`: Number of items per page (default: 50, max: 100)

### Response Structure
```json
{
  "count": 2341,
  "next": "http://localhost:8000/api/v1/carparks/?page=3",
  "previous": "http://localhost:8000/api/v1/carparks/?page=1",
  "results": [...]
}
```

### Example
```bash
# Get page 2 with 25 items per page
curl -X GET "http://localhost:8000/api/v1/carparks/?page=2&page_size=25"
```

---

## 🔧 Rate Limiting

Currently, there are no rate limits applied. However, please use the API responsibly:

- Don't make excessive concurrent requests
- Implement proper error handling and retries
- Cache responses when appropriate
- Use pagination for large datasets

---

## 📝 Examples

### Complete CRUD Example

```bash
# 1. Create a new carpark
CARPARK_ID=$(curl -s -X POST "http://localhost:8000/api/v1/carparks/" \
  -H "Content-Type: application/json" \
  -d '{
    "address": "Example Street 123",
    "car_park_type": "SURFACE CAR PARK",
    "gantry_height": 2.8,
    "night_parking": true
  }' | jq -r '.id')

# 2. Get the created carpark
curl -X GET "http://localhost:8000/api/v1/carparks/$CARPARK_ID/"

# 3. Update the carpark
curl -X PATCH "http://localhost:8000/api/v1/carparks/$CARPARK_ID/" \
  -H "Content-Type: application/json" \
  -d '{
    "night_parking": false,
    "gantry_height": 3.0
  }'

# 4. Search for similar carparks
curl -X GET "http://localhost:8000/api/v1/carparks/search/?address=Example"
```

### Data Analysis Examples

```bash
# Get statistics
curl -X GET "http://localhost:8000/api/v1/carparks/average/"
curl -X GET "http://localhost:8000/api/v1/carparks/group/"

# Find all surface carparks with free parking
curl -X GET "http://localhost:8000/api/v1/carparks/filter/?type=SURFACE%20CAR%20PARK" | \
  jq '.[] | select(.has_free_parking == true)'

# Find high gantry carparks
curl -X GET "http://localhost:8000/api/v1/carparks/height-range/?min_height=3.0&max_height=10.0"
```

---

## 🛠️ SDKs and Tools

### Python SDK Example

```python
import requests

class CarparkAPI:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
    
    def get_carparks(self, page=1, page_size=50):
        response = requests.get(
            f"{self.base_url}/api/v1/carparks/",
            params={"page": page, "page_size": page_size}
        )
        return response.json()
    
    def create_carpark(self, data):
        response = requests.post(
            f"{self.base_url}/api/v1/carparks/",
            json=data
        )
        return response.json()
    
    def search_by_address(self, address):
        response = requests.get(
            f"{self.base_url}/api/v1/carparks/search/",
            params={"address": address}
        )
        return response.json()

# Usage
api = CarparkAPI("http://localhost:8000")
carparks = api.get_carparks(page=1)
print(f"Found {carparks['count']} carparks")
```

### JavaScript/Node.js Example

```javascript
class CarparkAPI {
  constructor(baseUrl) {
    this.baseUrl = baseUrl.replace(/\/$/, '');
  }

  async getCarparks(page = 1, pageSize = 50) {
    const response = await fetch(
      `${this.baseUrl}/api/v1/carparks/?page=${page}&page_size=${pageSize}`
    );
    return response.json();
  }

  async createCarpark(data) {
    const response = await fetch(`${this.baseUrl}/api/v1/carparks/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    return response.json();
  }
}

// Usage
const api = new CarparkAPI('http://localhost:8000');
api.getCarparks().then(data => {
  console.log(`Found ${data.count} carparks`);
});
```

---

## 🔍 Testing the API

### Using curl

```bash
# Test basic functionality
curl -X GET "http://localhost:8000/api/v1/carparks/" | jq '.'

# Test filtering
curl -X GET "http://localhost:8000/api/v1/carparks/filter/?type=SURFACE%20CAR%20PARK" | jq '.'

# Test creation
curl -X POST "http://localhost:8000/api/v1/carparks/" \
  -H "Content-Type: application/json" \
  -d '{"address": "Test Address", "car_park_type": "SURFACE CAR PARK", "gantry_height": 2.5}' | jq '.'
```

### Using Postman

1. Import the following collection URL: `[Add your Postman collection here]`
2. Set the environment variable `base_url` to your API URL
3. Run the collection tests

### Using Python requests

```python
import requests

base_url = "http://localhost:8000/api/v1"

# Test GET
response = requests.get(f"{base_url}/carparks/")
print(f"Status: {response.status_code}")
print(f"Count: {response.json()['count']}")

# Test POST
new_carpark = {
    "address": "Test Address",
    "car_park_type": "SURFACE CAR PARK",
    "gantry_height": 2.5
}
response = requests.post(f"{base_url}/carparks/", json=new_carpark)
print(f"Created: {response.json()}")
```

---

## 📞 Support

For API support:
- **Documentation Issues**: Open an issue on GitHub
- **API Bugs**: Report on the issues page
- **Feature Requests**: Create a feature request issue

---

**Happy API coding! 🚀**

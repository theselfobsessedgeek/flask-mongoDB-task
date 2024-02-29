# Items App with Flask and MongoDB

## Setup
1. Clone the repository: `git clone <url to the repository>`
2. Navigate to the project directory: `cd your-repo`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Linux/Mac: `source venv/bin/activate`
   - On Windows: `venv\Scripts\activate`
5. Install dependencies: `pip install -r requirements.txt`

## Configuration
1. Set up MongoDB and obtain the connection Password as well as get the JWT secret.
2. Set the MongoDB Password and JWT Secret in `.env` file.

## Run the Application
1. Run the Flask app: `python app.py`
2. The app will be running at `http://127.0.0.1:5000/`

## Authenticate using JWT
1. Use the `/login` endpoint with the following credentials:
   - Username: `user`
   - Password: `password`
2. Copy the generated access token.

## Interact with API Endpoints
1. Create a new item:
   - Endpoint: `POST /items`
   - Headers: `Authorization: Bearer YOUR_ACCESS_TOKEN`
   - Body: JSON data with `name` and optional `description`

2. Retrieve all items:
   - Endpoint: `GET /items`

3. Retrieve a specific item by ID:
   - Endpoint: `GET /items/<item_id>`

4. Update an existing item:
   - Endpoint: `PUT /items/<item_id>`
   - Headers: `Authorization: Bearer YOUR_ACCESS_TOKEN`
   - Body: JSON data with updated `name` and/or `description`

5. Delete an item:
   - Endpoint: `DELETE /items/<item_id>`
   - Headers: `Authorization: Bearer YOUR_ACCESS_TOKEN`

# Interacting with a Database of Cosmetic Products Using Flask and REST API
This application can be used to manipulate a collection of cosmetic products by applying the CRUD operations through REST API. This is achieved using Flask framework to expose specific endpoints and one of three database engines (SQLite, PostgreSQL or MongoDB).

## Screenshots
1. The JSON returned by the backend app after a HTTP request using GET method

<picture>
 <img alt="Screenshot1" src="https://raw.githubusercontent.com/ambientWave/Cosmetic-Product-Flask-REST-API/main/Image1.png">
</picture>

2. One adds an item to the database by sending a HTTP request using POST method and putting the details of the added product in JSON format inside the body of the request

<picture>
 <img alt="Screenshot2" src="https://raw.githubusercontent.com/ambientWave/Cosmetic-Product-Flask-REST-API/main/Image2.png">
</picture>

3. The product collection after addition

<picture>
 <img alt="Screenshot3" src="https://raw.githubusercontent.com/ambientWave/Cosmetic-Product-Flask-REST-API/main/Image3.png">
</picture>

4. One can remove an item by sending a HTTP request using DELETE method. Here's the response after sending the request using cURL CLI utility

<picture>
 <img alt="Screenshot4" src="https://raw.githubusercontent.com/ambientWave/Cosmetic-Product-Flask-REST-API/main/Image4.png">
</picture>

5. The product collection after removal

<picture>
 <img alt="Screenshot5" src="https://raw.githubusercontent.com/ambientWave/Cosmetic-Product-Flask-REST-API/main/Image5.png">
</picture>

## Instructions for Running the Application
1. clone the repository
2. (optional but preferable) create a virtual environment
3. install the dependencies in the requirements.txt file using pip
5. open a new terminal and make sure that you are in the directory of the cloned repository
6. run the app using the following command:

### `flask run`

## Technology
- Python, Werkzeug, Flask
- HTTP, REST API, JSON
- SQLite, PostgreSQL, MongoDB

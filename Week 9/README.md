# Open-Meteo Location Search

## Description
This is a simple Python console application that uses the Open-Meteo Geocoding API to search for locations by name.

Users can:
- Search for a location
- View matching locations returned by the API
- Filter the most recent search results by country
- Exit the application

The program includes basic error handling for timeouts, connection errors, invalid responses, and HTTP status code errors.

## Features
- Search locations using the Open-Meteo Geocoding API
- Display location name, country, latitude, and longitude
- Filter results by country
- Handle request and connection errors
- Simple menu-driven interface

## Requirements
- Python 3
- requests library

Install the required package:

```bash
pip install requests
```

## How to Run
Run the program from the terminal:

```bash
python main.py
```

## Menu Options

### 1. Search
Search for a location by name.

Example:

```text
Enter location: Abuja
```

### 2. Filter Last Results by Country
Filters the most recent search results using a country name.

Example:

```text
Enter country: Peru
```

### 3. Exit
Closes the application.

## API Used
Open-Meteo Geocoding API
Endpoint:

```text
https://geocoding-api.open-meteo.com/v1/search
```

## Error Handling

The application handles:
- Request timeouts
- Connection errors
- Invalid API responses
- HTTP errors (404, 429, 500+)
- Empty user input

## Demo
https://drive.google.com/file/d/1nhcDiYwTww7L1SXn2lFoVzkkYXVBLLTE/view?usp=sharing


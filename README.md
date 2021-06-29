# Display and add car details using Rest API
Code to add and show car details using rest api

### URLS ###
-  Add a New Car
    - /add_car - POST request to add a new car having json as body.
    - example json - {
    "car_name": "Creta",
    "brand_name": "Hyundai",
    "top_speed": 220,
    "fuel_type": "Diesel",
    "car_type": "SUV",
    "price": 35000
}
  
- Display Car details
    - /<car_name> - GET request to get all details with the car name
    - example_url - http://127.0.0.1:8000/Creta
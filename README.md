# DRF Training System

A simple Django Rest Framework application for training system.


## Description

- Currently there are 7 currencies available for conversion: ['AED', 'USD', 'EUR', 'RUB', 'TRY', 'CNY', 'HKD'].
- Courses are requested from the service https://currencyapi.com/
- In order to reduce the number of requests to a third-party service, the data received from the service is cached in Redis every 24 hours.
- A request for current courses is made using a deferred task in Celery on a schedule once every 24 hours.


## Installation

1. Clone the repository: `git clone https://github.com/shmicer/training_system_test_case.git`
2. Navigate to the project directory: `cd training_system_test_case`
3. Rename the `.env.example` file found in the root directory of the project to folder `.envs/local/.django` 
and update the environment variables accordingly.
4. Then you can start the project using Docker or manually using virtual environment.

Using Docker:

```
$ docker compose -f local.yml build

$ docker compose -f local.yml up

```


Open a browser and go to http://localhost:8000


## API Documentation

### Endpoints

#### 1. Retrieve List of Lessons

- **URL:** `/api/lessons/`
- **Method:** `GET`
- **Description:** Retrieve a list of all lessons for authenticated user with a status of view.
- **Parameters:** None
- **Response:**
  - Status Code: 200 OK
  - Body: JSON array of lessons.

#### 2. Retrieve Product List

- **URL:** `/api/products/`
- **Method:** `GET`
- **Description:** Return a list of all products for authenticated user.
- **Parameters:** None
- **Response:**
  - Status Code: 200 OK
  - Body: JSON array of lessons.

#### 3. Retrieve Product Lessons

- **URL:** `/api/products/{product_id}/`
- **Method:** `GET`
- **Description:** Retrieve lessons for a specific product.
- **Parameters:**
  - `{product_id}`: ID of the product.
- **Response:**
  - Status Code: 200 OK
  - Body: JSON object with product lessons.

#### 3. Retrieve Product Summary

- **URL:** `/api/summary/{product_id}/`
- **Method:** `GET`
- **Description:** Retrieve details for a specific product.
- **Parameters:**
  - `{product_id}`: ID of the product.
- **Response:**
  - Status Code: 200 OK
  - Body: JSON object with product summary.


# Product Catalog Service

[![License](https://img.shields.io/badge/License-Apache-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/badge/Python-3.10-green)](https://www.python.org/downloads/)

This repository contains a Flask-based Product Catalog Service allowing management of products through various endpoints.

## Prerequisites and Dependencies

Before you can run the application, ensure you have the following prerequisites and dependencies:

- **Docker:** Used for containerizing the application.
  
## Contents

- **bin:** Contains the setup script `setup.sh` for setting up the project.
- **app:** Directory for the Flask application.
  - **__init__.py:** Initializes the Flask app, configures SQLAlchemy, and sets up routes.
  - **config.py:** Holds configurations for the Flask app and tests.
  - **models:** Includes the `Product` model for database operations.
  - **routes:** Defines endpoints for product management.
  - **tests:** Contains unit tests for the product endpoints.
- **run.py:** Entry point to run the Flask application.
- **Dockerfile:** Docker configuration for containerizing the application.
- **.env:** Environment variables configuration file.
- **LICENCE:** License file for the project.
- **pytest.ini:** Configuration for pytest.

## Running the Application

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/munuhee/product-catalog-service.git
    cd product-catalog-service
    ```

2. Grant execution permissions to the setup script:
    ```bash
    chmod +x bin/setup.sh
    ```

3. Run the setup script to build the Docker image and start the Flask app:
    ```bash
    ./bin/setup.sh
    ```

4. Access the application:
   - Locally: [http://localhost:8080](http://localhost:8080)
   - Remotely: [http://YOUR_SERVER_IP:8080](http://YOUR_SERVER_IP:8080)

## Usage

### HTTP Routes

- **Health Status:** `/status`
  - Example: `GET /status` - Retrieves the health status of the service.

- **Create Product:** `/product-create` (POST)
  - Example: `POST /product-create` - Creates a new product.

- **Get Products:** `/products` (GET)
  - Example: `GET /products` - Retrieves a list of all products.

- **Get Product by ID:** `/products/<product_id>` (GET)
  - Example: `GET /products/123` - Retrieves product details with ID 123.

- **Update Product by ID:** `/products/<product_id>/update` (PUT)
  - Example: `PUT /products/123/update` - Updates product details with ID 123.

- **Delete Product by ID:** `/products/<product_id>/delete` (DELETE)
  - Example: `DELETE /products/123/delete` - Deletes product with ID 123.

Refer to the `product_routes.py` file in `app/routes` for detailed endpoint implementations.

## CI/CD Configuration

The `docker-img.yml` file in the repository sets up CI/CD using GitHub Actions for continuous integration and deployment of the Docker image.

## Testing

The `app/tests` directory contains comprehensive unit tests (`test_product_endpoints.py`) for various product-related endpoints. The tests cover functionalities such as health status, product creation, retrieval, update, and deletion.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements, bug fixes, or new features.

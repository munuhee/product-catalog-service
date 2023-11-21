# Product Catalog Service

The **Product Catalog Service** is a Flask-based application aimed at efficient management and storage of a comprehensive product catalog. It leverages Docker for containerization and PostgreSQL as the database for storing product-related information.

## Features

- **Flask Framework**: Utilizes Flask, a lightweight and flexible web framework in Python.
- **Docker Integration**: Dockerized setup for simplified deployment and development.
- **PostgreSQL Database**: Uses PostgreSQL for data storage, ensuring reliability and scalability.
- **Structured Codebase**: Organized code structure with clear separation of concerns for models, routes, and services.
- **RESTful API**: Provides RESTful endpoints for CRUD operations on the product catalog.

## Installation

### Prerequisites

- Docker installed on your system.
- Python 3.x and pip installed.

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/product-catalog-service.git
    cd product-catalog-service
    ```

2. Set up the Docker environment:

    ```bash
    docker-compose up --build
    ```

3. Access the application via `http://localhost:5000`.

## API Endpoints

- **GET /products**: Retrieve all products.
- **GET /products/{product_id}**: Retrieve a specific product by ID.
- **POST /products**: Create a new product.
- **PUT /products/{product_id}**: Update an existing product.
- **DELETE /products/{product_id}**: Delete a product by ID.

### Sample Request and Response

#### GET /products

Request:

```http
GET /products
```

Response:

```json
[
    {
        "id": 1,
        "name": "Product A",
        "description": "Description of Product A",
        "price": 29.99,
        "category": "Category A"
    },
    {
        "id": 2,
        "name": "Product B",
        "description": "Description of Product B",
        "price": 39.99,
        "category": "Category B"
    }
]
```

#### POST /products

Request:

```http
POST /products
Content-Type: application/json

{
    "name": "New Product",
    "description": "Description of New Product",
    "price": 49.99,
    "category": "Category C"
}
```

Response:

```json
{
    "id": 3,
    "name": "New Product",
    "description": "Description of New Product",
    "price": 49.99,
    "category": "Category C"
}
```

## Usage

- **API Endpoints**: Utilize the provided endpoints to manage the product catalog.
- **Database Configuration**: Adjust database configurations in `app/config.py` as needed.

## Contributing

We welcome contributions! To contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

Please ensure your code follows the project's coding style and includes necessary tests.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

Special thanks to all contributors who have helped shape and improve this project.

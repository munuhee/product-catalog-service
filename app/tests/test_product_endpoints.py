"""
Contains unit tests to validate the functionality of Flask endpoints handling product operations:
- Tests health status, product creation, retrieval, update, and deletion.
- Initializes a test environment, simulates HTTP requests, and asserts expected behaviors.
"""
import unittest
import json
from app import app, db
from app.models.product import Product

class TestProductEndpoints(unittest.TestCase):
    """Tests for product-related endpoints."""

    def setUp(self):
        """Set up the testing environment"""
        app.config.from_pyfile('config.py')
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        """Tear down the testing environment"""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_health_status(self):
        """Test health status endpoint"""
        with app.app_context():
            response = self.app.get('/status')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(data['message'], 'application is healthy')

    def test_create_product(self):
        """Test create product endpoint"""
        with app.app_context():
            # Test valid product creation
            data = {
                "name": "Test Product",
                "description": "Test Description",
                "category": "Test Category",
                "price": 99.99
            }
            response = self.app.post('/product-create', json=data)
            self.assertEqual(response.status_code, 201)

            # Test missing fields in product creation
            incomplete_data = {
                "description": "Incomplete Product"
            }
            response_missing_fields = self.app.post('/product-create', json=incomplete_data)
            self.assertEqual(response_missing_fields.status_code, 400)

    def test_get_products(self):
        """Test get all products endpoint"""
        with app.app_context():
            product1 = Product(
                name="Product 1",
                description="Description 1",
                category="Category 1",
                price=10.0
            )
            product2 = Product(
                name="Product 2",
                description="Description 2",
                category="Category 2",
                price=20.0
            )
            db.session.add(product1)
            db.session.add(product2)
            db.session.commit()

            response = self.app.get('/products')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(len(data), 2)

    def test_get_product(self):
        """Test get single product endpoint"""
        with app.app_context():
            product = Product(name="Test", description="Test Desc", category="Test Cat", price=50.0)
            db.session.add(product)
            db.session.commit()

            # Test valid product retrieval
            response = self.app.get(f'/products/{product.id}')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(data['name'], 'Test')

            # Test product retrieval by invalid ID
            invalid_id_response = self.app.get('/products/999')  # Non-existent product ID
            self.assertEqual(invalid_id_response.status_code, 404)

    def test_valid_product_update(self):
        """Test valid product update endpoint"""
        with app.app_context():
            product = Product(name="Test", description="Test Desc", category="Test Cat", price=50.0)
            db.session.add(product)
            db.session.commit()

            updated_data = {
                "name": "Updated Product",
                "description": "Updated Description",
                "category": "Updated Category",
                "price": 75.0
            }
            response = self.app.put(f'/products/{product.id}/update', json=updated_data)
            self.assertEqual(response.status_code, 200)

    def test_invalid_product_update(self):
        """Test invalid product update endpoint"""
        with app.app_context():
            updated_data = {
                "name": "Updated Product",
                "description": "Updated Description",
                "category": "Updated Category",
                "price": 75.0
            }

            invalid_update_response = self.app.put('/products/999/update', json=updated_data)
            self.assertEqual(invalid_update_response.status_code, 404)


    def test_valid_product_removal(self):
        """Test valid product removal endpoint"""
        with app.app_context():
            product = Product(name="Test", description="Test Desc", category="Test Cat", price=50.0)
            db.session.add(product)
            db.session.commit()

            response = self.app.delete(f'/products/{product.id}/delete')
            self.assertEqual(response.status_code, 200)

    def test_invalid_product_removal(self):
        """Test invalid product removal endpoint"""
        with app.app_context():
            invalid_delete_response = self.app.delete('/products/999/delete')
            self.assertEqual(invalid_delete_response.status_code, 404)


if __name__ == '__main__':
    unittest.main()

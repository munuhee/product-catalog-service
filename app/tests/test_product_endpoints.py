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
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        """Tear down the testing environment"""
        db.session.remove()
        db.drop_all()

    def test_health_status(self):
        """Test health status endpoint"""
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['message'], 'application is healthy')

    def test_create_product(self):
        """Test create product endpoint"""
        data = {
            "name": "Test Product",
            "description": "Test Description",
            "category": "Test Category",
            "price": 99.99
        }
        response = self.app.post('/product-create', json=data)
        self.assertEqual(response.status_code, 201)

    def test_get_products(self):
        """Test get all products endpoint"""
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
        product = Product(name="Test", description="Test Desc", category="Test Cat", price=50.0)
        db.session.add(product)
        db.session.commit()
        response = self.app.get(f'/products/{product.id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['name'], 'Test')

    def test_update_product(self):
        """Test update product endpoint"""
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

    def test_remove_product(self):
        """Test remove product endpoint"""
        product = Product(name="Test", description="Test Desc", category="Test Cat", price=50.0)
        db.session.add(product)
        db.session.commit()
        response = self.app.delete(f'/products/{product.id}/delete')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

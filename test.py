import unittest
import json
from app import app
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):
    def test_calculate_bmi(self):
        # Test BMI calculation
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
        self.assertAlmostEqual(calculate_bmi(1.60, 55), 21.48, places=2)
        self.assertAlmostEqual(calculate_bmi(1.80, 90), 27.78, places=2)
    
    def test_calculate_bmr_male(self):
        # Test BMR calculation for male
        self.assertAlmostEqual(calculate_bmr(175, 70, 30, 'male'), 1686.99, places=2)
    
    def test_calculate_bmr_female(self):
        # Test BMR calculation for female
        self.assertAlmostEqual(calculate_bmr(165, 55, 25, 'female'), 1340.18, places=2)

class TestAPIEndpoints(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        # Create a test client
        self.client = app.test_client()
    
    def test_home_endpoint(self):
        # Test the home endpoint
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Health Calculator API', response.data)
    
    def test_bmi_endpoint_valid(self):
        # Test valid BMI calculation
        response = self.client.post('/bmi', 
                              json={'height': 1.75, 'weight': 70})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('bmi', data)
        self.assertAlmostEqual(data['bmi'], 22.86, places=2)
    
    def test_bmi_endpoint_invalid(self):
        # Test missing parameter
        response = self.client.post('/bmi', 
                              json={'height': 1.75})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
    
    def test_bmr_endpoint_valid(self):
        # Test valid BMR calculation
        response = self.client.post('/bmr', 
                              json={'height': 175, 'weight': 70, 'age': 30, 'gender': 'male'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('bmr', data)
        self.assertAlmostEqual(data['bmr'], 1686.99, places=2)
    
    def test_bmr_endpoint_invalid(self):
        # Test missing parameter
        response = self.client.post('/bmr', 
                              json={'height': 175, 'weight': 70, 'age': 30})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
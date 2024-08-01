import unittest
import requests

class TestAPI(unittest.TestCase):
    BASE_URL = "http://localhost:8080"

    def test_post_address_with_invalid_customer(self):
        endpoint = f"{self.BASE_URL}/Address"
        
        payload = {
            "street": "Test Street",
            "city": "Test City",
            "postCode": "12345",
            "buildingNumber": "1",
            "flatNumber": "101",
            "verificationStatus": 1,
            "customerId": 0
        }
        
        response = requests.post(endpoint, json=payload)
        
        self.assertEqual(response.status_code, 500)
        
        self.assertIn('The INSERT statement conflicted with the FOREIGN KEY constraint', response.text)
        self.assertIn('CustomerId', response.text)
        
    def test_post_address_with_valid_data(self):
        endpoint = f"{self.BASE_URL}/Address"
        
        payload = {
            "street": "Dummy Street",
            "city": "Dummy City",
            "postCode": "54321",
            "buildingNumber": "10",
            "flatNumber": "202",
            "verificationStatus": 1,
            "customerId": 1
        }
        
        response = requests.post(endpoint, json=payload)

        self.assertEqual(response.status_code, 200)

        data = response.json()
        
        self.assertIsInstance(data, int)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()

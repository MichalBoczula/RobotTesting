import unittest
import requests

class GetAddressById(unittest.TestCase):
    BASE_URL = "http://localhost:8080"

    def test_get_address(self):
        endpoint = f"{self.BASE_URL}/Address/1"
        
        response = requests.get(endpoint)
        
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        
        self.assertIsInstance(data, dict) 
        
        self.assertEqual(data['street'], '123 Main St')
        self.assertEqual(data['city'], 'CityA')
        self.assertEqual(data['postCode'], '10001')
        self.assertEqual(data['buildingNumber'], '1')
        self.assertEqual(data['flatNumber'], '101')
        self.assertEqual(data['verificationStatus'], 1)

if __name__ == '__main__':
    unittest.main()
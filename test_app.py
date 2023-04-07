import unittest
import json
from app import app

class TestProperties(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_properties(self):
        response = self.app.get('/properties?location=37.774,-122.419')
        data = json.loads(response.get_data())
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['address'], '123 Main St')
        self.assertEqual(data[1]['address'], '456 Elm St')

    def test_invalid_location(self):
        response = self.app.get('/properties?location=invalid')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
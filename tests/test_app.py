import unittest
import os
from flask import Flask
from app import app, get_db_connection  # Adjust based on your file structure

class FlaskTestCase(unittest.TestCase):
    # Test basic route '/' to ensure the app is running and returns a valid response
    def test_index(self):
        with app.test_client() as c:
            response = c.get('/')
            self.assertEqual(response.status_code, 200)  # Ensure it returns HTTP 200
            self.assertIn(b'Beagle of the Day', response.data)  # Ensure the content is correct

    # Test the database connection function
    def test_db_connection(self):
        connection = get_db_connection()
        self.assertIsNotNone(connection)  # Ensure connection is established
        connection.close()

    # Optionally, add more tests like:
    # Test if the app can fetch a random GIF (not necessarily meaningful but to check DB)
    def test_random_image(self):
        with app.test_client() as c:
            response = c.get('/')
            self.assertIn(b'http', response.data)  # Check if the image URL starts with 'http'

if __name__ == '__main__':
    unittest.main()

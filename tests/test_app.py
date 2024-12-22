import unittest
import os
from flask import Flask
from app import app, get_db_connection
from unittest.mock import patch, MagicMock

class FlaskTestCase(unittest.TestCase):

    # Test basic route '/' to ensure the app is running and returns a valid response
    def test_index(self):
        with app.test_client() as c:
            response = c.get('/')
            self.assertEqual(response.status_code, 200)  # Ensure it returns HTTP 200
            self.assertIn(b'Beagle of the Day', response.data)  # Ensure the content is correct

    # Test the database connection function
    @patch('app.get_db_connection')  # Mocking the get_db_connection function
    def test_db_connection(self, mock_get_db_connection):
        # Mock the database connection
        mock_connection = MagicMock()
        mock_get_db_connection.return_value = mock_connection

        connection = get_db_connection()
        self.assertIsNotNone(connection)  # Ensure connection is established (mocked)
        mock_connection.close.assert_called_once()  # Ensure the connection's close method is called

    # Test if the random image URL starts with "http"
    def test_random_image(self):
        # Mocking the database query to return a sample image URL
        with patch('app.mysql.connector.connect') as mock_connect:
            mock_cursor = MagicMock()
            mock_cursor.fetchone.return_value = ('https://somegifurl.com/sample.gif',)
            mock_connect.return_value.cursor.return_value = mock_cursor

            with app.test_client() as c:
                response = c.get('/')
                self.assertIn(b'http', response.data)  # Check if the image URL starts with 'http'

if __name__ == '__main__':
    unittest.main()

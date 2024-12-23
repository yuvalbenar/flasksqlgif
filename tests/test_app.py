import unittest
import os
from flask import Flask
from app import app, get_db_connection
import mysql.connector

class FlaskTestCase(unittest.TestCase):

    # Test basic route '/' to ensure the app is running and returns a valid response
    def test_index(self):
        with app.test_client() as c:
            response = c.get('/')
            self.assertEqual(response.status_code, 200)  # Ensure it returns HTTP 200
            self.assertIn(b'Beagle of the Day', response.data)  # Ensure the content is correct

    # Test the database connection function (real DB connection)
    def test_db_connection(self):
        try:
            connection = get_db_connection()  # This should connect to gif-db container
            self.assertIsNotNone(connection)  # Ensure connection is established
            connection.close()  # Close the connection
        except mysql.connector.Error as err:
            self.fail(f"Error connecting to MySQL: {err}")

    # Test if the random image URL starts with "http" (real DB query)
    def test_random_image(self):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT url FROM images ORDER BY RAND() LIMIT 1")
            random_image = cursor.fetchone()
            self.assertIsNotNone(random_image)  # Ensure we got a result
            self.assertTrue(random_image[0].startswith('http'))  # Ensure the URL starts with 'http'
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            self.fail(f"Error querying the database: {err}")

if __name__ == '__main__':
    unittest.main()

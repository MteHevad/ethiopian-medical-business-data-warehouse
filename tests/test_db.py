import unittest
import psycopg2

class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Establish a connection to the test database
        cls.conn = psycopg2.connect(
            dbname="test_medical_data", user="postgres", password="password", host="localhost"
        )
        cls.cur = cls.conn.cursor()

        # Create test tables in the database
        cls.cur.execute("""
            CREATE TABLE IF NOT EXISTS medical_businesses (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                location VARCHAR(255)
            );
            CREATE TABLE IF NOT EXISTS scraped_images (
                id SERIAL PRIMARY KEY,
                business_id INT REFERENCES medical_businesses(id),
                image_url VARCHAR(255)
            );
        """)
        cls.conn.commit()

    def test_insert_business(self):
        # Test inserting a new business record
        self.cur.execute("""
            INSERT INTO medical_businesses (name, location) 
            VALUES ('Test Medical Clinic', 'Addis Ababa');
        """)
        self.conn.commit()

        # Check if the record exists
        self.cur.execute("SELECT * FROM medical_businesses WHERE name='Test Medical Clinic';")
        result = self.cur.fetchone()
        self.assertIsNotNone(result, "Failed to insert business record")

    def test_insert_image(self):
        # Test inserting a new image record
        self.cur.execute("""
            INSERT INTO scraped_images (business_id, image_url) 
            VALUES (1, 'test_image.jpg');
        """)
        self.conn.commit()

        # Check if the record exists
        self.cur.execute("SELECT * FROM scraped_images WHERE image_url='test_image.jpg';")
        result = self.cur.fetchone()
        self.assertIsNotNone(result, "Failed to insert image record")

    @classmethod
    def tearDownClass(cls):
        # Clean up the test tables
        cls.cur.execute("DROP TABLE IF EXISTS scraped_images, medical_businesses;")
        cls.conn.commit()

        # Close the connection
        cls.cur.close()
        cls.conn.close()

if __name__ == '__main__':
    unittest.main()

import unittest
from telethon.sync import TelegramClient
from telegram_scraper import scrape_telegram_channel

class TestScraper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Mock Telegram API credentials for testing
        cls.api_id = 'TEST_API_ID'
        cls.api_hash = 'TEST_API_HASH'
        cls.phone_number = 'TEST_PHONE_NUMBER'
        cls.client = TelegramClient('test_session', cls.api_id, cls.api_hash)
    
    def test_scraping_channel(self):
        # Test the scraping function with a test channel link
        result = scrape_telegram_channel('https://t.me/DoctorsET')
        self.assertIsNotNone(result, "Scraping failed, result is None")

    @classmethod
    def tearDownClass(cls):
        cls.client.disconnect()

if __name__ == '__main__':
    unittest.main()

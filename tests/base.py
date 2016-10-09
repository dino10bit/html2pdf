import unittest
import main


class BaseCase(unittest.TestCase):
    def setUp(self):
        main.app.config['TESTING'] = True
        self.client = main.app.test_client()

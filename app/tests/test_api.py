import json
import unittest

from app import api


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = api.app.test_client()
        cls.app.testing = True

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # do something before each test
        pass

    def tearDown(self):
        # do something after each test
        pass

    def test_healthz_00(self):
        expect = {
            u'flask': True,
            u'global': True
        }

        result = self.app.get('/healthz')
        self.assertEqual(result.status_code, 200)
        data = result.data.decode("utf-8")
        content = json.loads(data)
        self.assertEqual(content, expect)

    def test_one_00(self):
        expect = {
            'one': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        }

        result = self.app.get('/api/one')
        self.assertEqual(result.status_code, 200)
        data = result.data.decode("utf-8")
        content = json.loads(data)
        self.assertEqual(content, expect)

    def test_two_00(self):
        expect = {
            'two': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        }

        result = self.app.get('/api/two')
        self.assertEqual(result.status_code, 200)
        data = result.data.decode("utf-8")
        content = json.loads(data)
        self.assertEqual(content, expect)


if __name__ == '__main__':
    unittest.main()

import unittest
import uuid
import app


class FlaskBaseTest(unittest.TestCase):

    def setUp(self):
        self.tester = app.app.test_client()
        app.BOOKS = [
            {
                'id': 1234,
                'title': 'On the Road',
                'author': 'Jack Kerouac',
                'read': True
            }]

    def test_ping(self):
        response = self.tester.get('/ping')
        self.assertEqual('pong!', response.json)

    def test_getbooks(self):
        response = self.tester.get('books')
        expectedBooks = [{
            'id': 1234,
            'title': 'On the Road',
            'author': 'Jack Kerouac',
            'read': True
        }]
        self.assertListEqual(response.json['books'], expectedBooks)


if __name__ == '__main__':
    unittest.main()

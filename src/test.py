import unittest
import app

class TestHello(unittest.TestCase):
    def setUp(self) -> None:
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_hello(self):
        rv = self.app.get('/hello/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_name(self):
        name = "Neo"
        rv = self.app.get(f'/hello/{name}')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray(f"{name}", 'utf-8'), rv.data)

    def test_hello_garrett(self):
        rv = self.app.get(f'/hello/garrett')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(rv.data, b'Hi Garrett!\n')


if __name__ == "__main__":
    unittest.main()
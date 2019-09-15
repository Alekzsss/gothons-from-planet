import unittest
from flask import session
import planisphere
from bin.__init__ import app


# app.config['LKSJFLKJFLKDAF'] = True

class BasicTestCase(unittest.TestCase):

    def test_routes(self):
        web = app.test_client(self)
        rv = web.get('/', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        rv = web.get('/')
        self.assertEqual(rv.status_code, 302)
        with web:
            web.get('/')
            self.assertEqual(session['room_name'], planisphere.START)

        rv = web.get('/game', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)

        rv = web.get('/play_again/', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        rv = web.get('/play_again/')
        self.assertEqual(rv.status_code, 302)
        with web:
            web.get('/play_again/')
            self.assertNotIn(planisphere.START, session)


    # data = {'name': 'Michail', 'greet': 'Hello, '}
    # rv = web.post('/hello', follow_redirects=True, data=data)
    # assert_in(b"Michail", rv.data)
    # assert_in(b"Hello, ", rv.data)

if __name__ == '__main__':
    unittest.main()
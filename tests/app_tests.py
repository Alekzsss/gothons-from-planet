from nose.tools import *
from bin.__init__ import app

app.config['NTCNBHJDFYBT'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 404)

    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    # assert_in(b"Fill-in this form", rv.data)

    rv = web.get('/game', follow_redirects=True)
    assert_equal(rv.status_code, 200)

    rv = web.get('/play_again', follow_redirects=True)
    assert_equal(rv.status_code, 200)

    # data = {'name': 'Michail', 'greet': 'Hello, '}
    # rv = web.post('/hello', follow_redirects=True, data=data)
    # assert_in(b"Michail", rv.data)
    # assert_in(b"Hello, ", rv.data)

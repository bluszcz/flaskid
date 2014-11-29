import os
import flaskid
import unittest
import tempfile

class FlaskidTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskid.app.config['DATABASE'] = tempfile.mkstemp()
        flaskid.app.config['TESTING'] = True
        self.app = flaskid.app.test_client()
        #flaskid.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskid.app.config['DATABASE'])

    def test_start_page(self):
        rv = self.app.get('/')
        assert 'start_page' in rv.data

    def test_openid_server(self):
        rv = self.app.get('/openidserver')
        assert '/openidserver' in rv.data

    def test_login(self):
        rv = self.app.get('/login')
        assert '/login' in rv.data

    def test_login_submit(self):
        rv = self.app.get('/loginsubmit')
        assert '/loginsubmit' in rv.data

    def test_id(self):
        rv = self.app.get('/id/')
        assert '/id/' in rv.data

    def test_yadis(self):
        rv = self.app.get('/yadis')
        assert '/yadis' in rv.data

    def test_server_yadis(self):
        rv = self.app.get('/serveryadis')
        assert '/serveryadis' in rv.data

if __name__ == '__main__':
    unittest.main()
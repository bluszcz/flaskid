from flask import Flask
app = Flask(__name__)

@app.route('/')
def on_start_page():
    return 'start_page'

@app.route('/openidserver')
def on_openid_server():
    return '/openidserver'

@app.route('/login')
def on_login():
    return '/login'

@app.route('/loginsubmit')
def on_login_submit():
    return '/loginsubmit!'

@app.route('/id/')
def on_id():
    return '/id/'

@app.route('/yadis/')
def on_yadis():
    return '/yadis/'

@app.route('/serveryadis')
def on_server_yadis():
    return '/serveryadis'

if __name__ == '__main__':
    app.run(port=5080)
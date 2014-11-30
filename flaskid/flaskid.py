from flask import Flask
from flask import render_template

app = Flask(__name__)

MOCKUP_TEXT="""Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
Proin nibh augue, suscipit a, scelerisque sed, lacinia in, mi. Cras vel 
lorem. Etiam pellentesque aliquet tellus."""

@app.route('/')
def on_start_page():
    return render_template('index.html', mockup_text=MOCKUP_TEXT)

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


@app.route('/processTrustResult')
def on_processTrustResult():
    return '/processTrustResult'

@app.route('/user')
def on_user():
    return '/user'

@app.route('/xrds')
def on_xrds():
    return '/xrds'    

@app.route('/endpoint')
def on_endpoint():
    return '/endpoint'

@app.route('/trust')
def on_trust():
    return '/trust'



if __name__ == '__main__':
    app.run(port=5080, debug=True)
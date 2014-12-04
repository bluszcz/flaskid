from flask import Flask
from flask import render_template
from flask import request
from openid.store.sqlstore import SQLiteStore
from flask import Response

from openid.server import server
import sqlite3

app = Flask(__name__)

MOCKUP_APPNAME="FlaskID"
MOCKUP_TEXT="""Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
Proin nibh augue, suscipit a, scelerisque sed, lacinia in, mi. Cras vel 
lorem. Etiam pellentesque aliquet tellus."""

@app.route('/')
def on_start_page():
    return render_template('index.html', 
        mockup_text=MOCKUP_TEXT,
        title="%s index page" % MOCKUP_APPNAME)

@app.route('/id/<username>')
def on_id(username):
    return render_template('user_id.html', 
        title="%s - %s" % (MOCKUP_APPNAME, username),
        username=username,
        url_root=request.url_root)
    return '/id/'


def getServer(url_root):
    openidstore = SQLiteStore(sqlite3.connect('/tmp/cstore.db'))
    oserver = server.Server(openidstore, url_root+'/openidserver')
    return oserver

@app.route('/openidserver')
def on_openid_server():
    oserver = getServer(request.url_root)
    orequest = oserver.decodeRequest(request.args)

    if orequest.mode in ["checkid_immediate", "checkid_setup"]:
        if orequest.immediate:
            openid_response = orequest.answer(False)
            return display_response(request, openid_response)

        #self.handleCheckIDRequest(request)
        #is_authorized = self.isAuthorized(request.identity, request.trust_root)




    oresponse = oserver.handleRequest(orequest)
    webresponse = self.server.openid.encodeResponse(oresponse)

    return webresponse.body

def display_response(request,openid_response):
    """
    Display an OpenID response. Errors will be displayed directly to
    the user; successful responses and other protocol-level messages
    will be sent using the proper mechanism (i.e., direct response,
    redirection, etc.).
    """
    s = getServer(request)

    response = Response()

    # Encode the response into something that is renderable.
    try:
        webresponse = s.encodeResponse(openid_response)
    except EncodingError, why:
        # If it couldn't be encoded, display an error.
        text = why.response.encodeToKVForm()
        return text

    for header, value in webresponse.headers.iteritems():
        response.headers[header] = value

    response.status_code = webresponse.code
    return  webresponse.body
# Construct the appropriate django framework response.
    


@app.route('/login')
def on_login():
    return '/login'

@app.route('/loginsubmit')
def on_login_submit():
    return '/loginsubmit!'


@app.route('/yadis/<username>')
def on_yadis(username):
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
    return render_template('trust.html', 
        mockup_text=MOCKUP_TEXT,
        title="%s index page" % MOCKUP_APPNAME)

if __name__ == '__main__':
    app.run(port=5080, debug=True)
from flask import Blueprint, render_template, jsonify, current_app, url_for, session, redirect
from authlib.integrations.flask_client import OAuth
from MySQLPackage import *

Auth = Blueprint(
    "Auth",
    __name__
)

Connection = Connection(
    host="127.0.0.1",
    username="Noah721",
    password="Satchel21",
    databaseName="YoutubeStyledTwitter"
)

OAuth2 = OAuth(current_app)
OAuth2.register (
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_id='245223128786-qq116jsrpsmructovnjrcqd01t38ar0b.apps.googleusercontent.com',
    client_secret='Jbv9EG_NklpOXHdudtqkFigx',
    client_kwargs={'scope': 'openid profile email'},
)

def Start():
    Connection.run()

    Database = Connection.getDatabase()
    Cursor = Connection.getCursor()

    return Database, Cursor

@Auth.route('/login')
def index():
    if 'LoggedIn' in session:
        return redirect(url_for('index'))
    redirect_uri = url_for('Auth.authorize', _external=True)
    return OAuth2.google.authorize_redirect(redirect_uri)

@Auth.route('/authorize')
def authorize():
    token = OAuth2.google.authorize_access_token()
    user = OAuth2.google.parse_id_token(token)

    Database, Cursor = Start()

    Users = Read(Database=Database, Cursor=Cursor, table="Users")

    session['LoggedIn'] = True
    session['email'] = user['email']
    session['picture'] = user['picture']
    session['name'] = user['name']

    if Users is not []:
        if session['email'] in Users:
            pass
        elif session['email'] not in [item for user in Users for item in user]:
            Create(Database=Database, Cursor=Cursor, table="Users", dict={
                "email": session['email'],
                "picture": session['picture'],
                "name": session['name']
            })
    else:
        Create(Database=Database, Cursor=Cursor, table="Users", dict={
            "email": session['email'],
            "picture": session['picture'],
            "name": session['name']
        })

    Database.close()

    return redirect(url_for('index'))

@Auth.route('/logout')
def logout():
    if 'LoggedIn' in session:
        session.pop('LoggedIn')
    if 'email' in session:
        session.pop('email')
    if 'picture' in session:
        session.pop('picture')
    if 'name' in session:
        session.pop('name')
    return redirect(url_for('index'))

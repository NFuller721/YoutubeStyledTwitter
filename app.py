from flask import Flask, render_template, session, redirect
from MySQLPackage import *

# Blueprints
from auth.main import Auth


Connection = Connection(host="127.0.0.1", username="Noah721", password="Satchel21", databaseName="YoutubeStyledTwitter")

def Start():
    Connection.run()

    Database = Connection.getDatabase()
    Cursor = Connection.getCursor()

    return Database, Cursor

App = Flask(__name__)
App.secret_key = 'secretKey'

# Register Blueprints
App.register_blueprint(Auth)

@App.route('/Api/<Key>/<Option>')
def Api(Key, Option):
    if Key == "34567654":
        Database, Cursor = Start()
        if Option == "CreatePost":



            Database.close()
            return {"Response": "Created Post"}
        if Option == "ReadPost":
            Post = {}

            Database.close()
            return {"Response": {"Post": Post}}
        if Option == "ReadAllPosts":
            Posts = {}

            Database.close()
            return {"Response": {"Posts": Posts}}
        if Option == "UpdatePost":

            Database.close()
            return {"Response": "Updated Post"}
        if Option == "DeletePost":

            Database.close()
            return {"Response": "Deleted Post"}
        Database.close()
        return {"Error": "No function with that name"}
    return {"Error": "Wrong Key"}

@App.route('/ScreenWidth/<ScreenWidth>')
def ScreenWidthTester(ScreenWidth):
    print(f"Screen Width: {ScreenWidth}")
    return {}

@App.route('/')
def index():
    if 'LoggedIn' in session:
        return render_template('index.html', picture=session['picture'])
    return redirect('login')

if __name__ == '__main__':
    App.run()

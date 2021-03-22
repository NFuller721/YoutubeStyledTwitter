from flask import Flask, render_template, session, redirect, request
from MySQLPackage import *

# Blueprints
from auth.main import Auth
from Hashtags.main import Hashtags
from User.main import User


Connection = Connection(
    host="127.0.0.1",
    username="Noah721",
    password="Satchel21",
    databaseName="YoutubeStyledTwitter"
)

def Start():
    Connection.run()

    Database = Connection.getDatabase()
    Cursor = Connection.getCursor()

    return Database, Cursor

App = Flask(__name__)
App.secret_key = 'secretKey'

# Register Blueprints
App.register_blueprint(Auth)
App.register_blueprint(Hashtags, url_prefix="/Hashtags")
App.register_blueprint(User, url_prefix="/User")

@App.route('/Api/<Key>/<Option>', methods=["GET", "POST"])
def Api(Key, Option):
    if request.method == "POST":
        if Key == "34567654":
            if Option == "CreatePost":
                Database, Cursor = Start()
                postText = request.form['postText']
                userID = int(request.form['userID'])
                likes = 0

                LoggedInID = None

                Users = Read(Database=Database, Cursor=Cursor, table="Users")
                for User in Users:
                    if User[1] == session['email']:
                        LoggedInID = User[0]

                if userID == LoggedInID:
                    Create(Database=Database, Cursor=Cursor, table="Posts", dict={
                        "postText": postText,
                        "userID": userID,
                        "likes": likes
                    })

                    Database = "Null"
                    return {"Response": "Created Post"}
                Database = "Null"
                return {"Response": "Not logged in as this user"}
            if Option == "ReadPost":
                Database, Cursor = Start()
                id = int(request.form['id'])

                Post = Read(Database=Database, Cursor=Cursor, table="Posts", id=id)[0]
                User = Read(Database=Database, Cursor=Cursor, table="Users", id=Post[2])[0]

                Post = {
                    "id": Post[0],
                    "postText": Post[1],
                    "userID": Post[2],
                    "likes": Post[3],
                    "userPicture": User[2],
                    "userName": User[3]
                }

                Database = "Null"
                return {"Response": {"Post": Post}}
            if Option == "ReadAllPosts":
                Database, Cursor = Start()
                PostData = Read(Database=Database, Cursor=Cursor, table="Posts")

                Posts = []

                for Post in PostData:
                    User = Read(Database=Database, Cursor=Cursor, table="Users", id=Post[2])[0]

                    Posts += [{
                        "id": Post[0],
                        "postText": Post[1],
                        "userID": Post[2],
                        "likes": Post[3],
                        "userPicture": User[2],
                        "userName": User[3]
                    }]

                Database = "Null"
                return {"Response": {"Posts": Posts}}
            if Option == "UpdatePost":
                Database, Cursor = Start()
                id = int(request.form['id'])
                postText = request.form['postText']

                userID = Read(Database=Database, Cursor=Cursor, table="Posts", id=id)[0][2]

                LoggedInID = None

                Users = Read(Database=Database, Cursor=Cursor, table="Users")
                for User in Users:
                    if User[1] == session['email']:
                        LoggedInID = User[0]

                if userID == LoggedInID:
                    Update(Database=Database, Cursor=Cursor, table="Posts", id=id, dict={
                        "postText": postText
                    })

                    Database = "Null"
                    return {"Response": "Updated Post"}
                Database = "Null"
                return {"Error": "Not logged in as this user"}
            if Option == "DeletePost":
                Database, Cursor = Start()
                id = int(request.form['id'])

                UserID = Read(Database=Database, Cursor=Cursor, table="Posts", id=id)[0][2]
                Email = Read(Database=Database, Cursor=Cursor, table="Users", id=UserID)[0][1]

                if session['email'] == Email:
                    Delete(Database=Database, Cursor=Cursor, table="Posts", id=id)

                    Database = "Null"
                    return {"Response": "Deleted Post"}
                Database = "Null"
                return {"Error": "Not logged in as this user"}
            if Option == "DeleteAllPosts":
                Database, Cursor = Start()
                AdminUsername = request.form['AdminUsername']
                AdminPassword = request.form['AdminPassword']

                if AdminUsername == "ahhgfdyueighrfegfvw" and AdminPassword == "yfctgwhegfvcuywhjefgwf":
                    Delete(Database=Database, Cursor=Cursor, table="Posts", id="All")

                    Database = "Null"
                    return {"Response": "Deleted All Posts"}
                Database = "Null"
                return {"Error": "Wrong Username and Password"}
            Database = "Null"
            return {"Error": "No function with that name"}
        return {"Error": "Wrong Key"}
    return {"Error": "No request"}

@App.route('/ScreenWidth/<ScreenWidth>')
def ScreenWidthTester(ScreenWidth):
    print(f"Screen Width: {ScreenWidth}")
    return {}

@App.route('/')
def index():
    if 'LoggedIn' in session:
        Database, Cursor = Start()
        Users = Read(Database=Database, Cursor=Cursor, table="Users")

        UserID = None

        for User in Users:
            if User[1] == session['email']:
                UserID = User[0]

        deletablePosts = []

        for Post in Read(Database=Database, Cursor=Cursor, table="Posts"):
            if Post[2] == UserID:
                deletablePosts += [Post[0]]

        Database.close()
        return render_template(
            'index.html',
            picture=session['picture'],
            name=session['name'],
            id=UserID,
            deletablePosts=deletablePosts
        )
    return redirect('login')

if __name__ == '__main__':
    App.run()

from flask import Flask, render_template, session, redirect, request
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

@App.route('/Api/<Key>/<Option>', methods=["GET", "POST"])
def Api(Key, Option):
    if request.method == "POST":
        if Key == "34567654":
            Database, Cursor = Start()
            if Option == "CreatePost":
                postText = request.form['postText']
                userID = int(request.form['userID'])
                likes = 0

                Create(Database=Database, Cursor=Cursor, table="Posts", dict={
                    "postText": postText,
                    "userID": userID,
                    "likes": likes
                })

                Database.close()
                return {"Response": "Created Post"}
            if Option == "ReadPost":
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

                Database.close()
                return {"Response": {"Post": Post}}
            if Option == "ReadAllPosts":
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

                Database.close()
                return {"Response": {"Posts": Posts}}
            if Option == "UpdatePost":
                id = int(request.form['id'])
                postText = request.form['postText']

                Update(Database=Database, Cursor=Cursor, table="Posts", id=id, dict={
                    "postText": postText
                })

                Database.close()
                return {"Response": "Updated Post"}
            if Option == "DeletePost":
                id = int(request.form['id'])

                Delete(Database=Database, Cursor=Cursor, table="Posts", id=id)

                Database.close()
                return {"Response": "Deleted Post"}
            Database.close()
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

        Database.close()
        return render_template('index.html', picture=session['picture'], name=session['name'], id=UserID)
    return redirect('login')

if __name__ == '__main__':
    App.run()

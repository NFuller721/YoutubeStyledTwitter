from flask import Blueprint, render_template, session, redirect, request
from MySQLPackage import *

Connection = Connection(
    host="127.0.0.1",
    username="Noah721",
    password="Satchel21",
    databaseName="YoutubeStyledTwitter"
)

User = Blueprint(
    "User",
    __name__
)

def Start():
    Connection.run()

    Database = Connection.getDatabase()
    Cursor = Connection.getCursor()

    return Database, Cursor

@User.route('/<userID>')
def UserPage(userID):
    if 'LoggedIn' in session:
        # Deletable posts
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

        isThisUser = UserID == userID

        Database.close()
        return render_template(
            'user.html',
            picture=session['picture'],
            name=session['name'],
            id=UserID,
            deletablePosts=deletablePosts,
            isThisUser=isThisUser,
            userid=userID
        )
    return redirect('login')

if __name__ == '__main__':
    App.run()

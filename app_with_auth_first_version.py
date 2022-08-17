import flask
import jwt
import sqlite3 as sql
from functools import wraps
import bcrypt


app=flask.Flask(__name__)
app.config["DEBUG"]=True
app.config["TOKEN"]="bharathkarkera"


db_file_path='/home/hackthebox/python_work/flask_basic_authentication/user.db'
connection=sql.connect(db_file_path)
cursor=connection.cursor()

cursor.execute("""select * from user_details""")
fetched_data=cursor.fetchall()
connection.commit()
connection.close()


#print(fetched_data)


def login_required(fun):
    @wraps(fun)
    def decorator(*args, **kwargs):
        user_found=False
        passed_auth=flask.request.authorization
        for i in fetched_data:
            print(f"i value is: {i} username is: {i[0]} password is: {i[1]}")
            if i[0]==passed_auth.username and bcrypt.checkpw(passed_auth.password,i[1]):
                user_found=True
                    
        if user_found==True:
            return fun(*args, **kwargs)
       
        return flask.make_response("Could not verify your login!", 401 , {"WWW-Authenticate":"Basic realm='Login Required !'"})
   
    return decorator


@app.route('/',methods=["GET"])
@login_required
def root_path():
    return "You are in the root path !"


@app.route('/unprotected',methods=["GET"])
def unprotected():
    return "You do not need auth token for this page!"



@app.route('/protected',methods=["GET"])
@login_required
def protected():
    return "You need auth token !"


app.run(host="0.0.0.0")


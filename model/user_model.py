import mysql.connector
from flask import make_response

class user_model():
    def __init__(self):
        # connection establishment
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="password", database="flask_tutorial")
            self.con.autocommit=True
            '''
                Create a cursor object associated with the connection
                Cursor objects are used to execute query and fetch data
                The is returned as a dictionary -> easier to work with
            '''
            self.cur=self.con.cursor(dictionary=True) 
            print("Connection successfull")
        except:
            print("Error connectiing to the db")
    

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result) > 0:
            return make_response(result, 200)
        else:
            return make_response({'message': 'no data found'}, 204)

    
    def user_addone_model(self, data):
        self.cur.execute("INSERT INTO users (name, email, phone, role, password) VALUES (%s, %s, %s, %s, %s)", (data['name'], data['email'], data['phone'], data['role'], data['password']))

        return make_response({'message': 'user created suucessfully'}, 201)

    def user_upload_avatar_model(self, uid, filepath):
        self.cur.execute("UPDATE users SET avatar=%s WHERE id=%s", (filepath, uid))
        if self.cur.rowcount > 0:
            return make_response({"message": "FILE_UPLOADED_SUCCESSFULLY"}, 201)
        else:
            return make_response({"message": "nothing to update"}, 202)









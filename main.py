from os import abort
import string
from flask import Flask, json, request , jsonify
import json
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this_is_my_secret_key'
class User:
    def __init__(self,username,email,id):
        self.username = username
        self.email = email
        self.id = id

users = [
    {
        "firstName": "Nirav",
        "email": "nirav@gmail.com",
        "id": "dsd232"
    }, 
    {
        "firstName": "Meet",
        "email": "Meet@gmail.com",
        "id": "123aasv"
    }
]

app.env = "development"
data = json.dumps({})
@app.route('/users',methods=['GET'])
def getMethod():
    try:
        response_data = {
            "message" : "Users Retrived",
            "success" : True,
            "users"  :  users
        }
     
        return jsonify(response_data), 200
    except:
        response = {
            "message": "Some error occurred",
            "status": False 
        }        
    return jsonify(response), 400

@app.route("/update/<user_id>", methods = ["PUT"])
def update_user(user_id):
    response = {}
    try:
        request_data = request.get_json()
        print(request_data)
        for user in users:
            if user.get("id") == user_id:
                if request_data.get("email"):
                    user["email"] = request_data.get("email")
                if request_data.get("firstName"):
                    user["firstName"] = request_data.get("firstName")
                response = {
                    "message": "User updated",
                    "status": True
                }
                
                return jsonify(response), 200 
        response = {
            "message": "User not found!",
            "status": False
        }
        return jsonify(response), 400
    except:
        response = {
            "message": "Some error occurred",
            "status": False 
        }        
    
    return jsonify(response), 404

@app.route("/add", methods=["POST"])
def add_user():
    request_data = request.get_json()
    try:
        flag = False
        new_user = {
            "email": request_data.get("email"),
            "firstName": request_data.get("firstName"),
            "id": "".join([random.choice(string.ascii_letters) for i in range(5)])
        }
    
        for user in users:
            if  user.get("email") == new_user.get("email"):
                flag = True
                break
        if not flag :
            print(new_user.get("email"))
            print(user.get("email"))
            print("Have")
            users.append(new_user)
            response = {
                "message": "User Added",
                "status": True 
            }     
            return jsonify(response), 201
        else:
            response = {
                "message": "User already exist ",
                "status": False 
            }  
            return response, 409
        
    except:
          response = {
            "message": "Some error occurred",
            "status": False 
        }        
    return jsonify(response) , 500
    
    
    
if __name__ == '__main__':
    app.run(debug=True)



 

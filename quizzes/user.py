import os
from pymongo import MongoClient


class User:
    client = MongoClient(os.getenv("MONGO_URI"))
    print(os.getenv("MONGO_URI"))
    # client = MongoClient(url)
    db = client['quiz_app_db']
    users_collection = db['users']

    def create_user(self,username, password):
        # Check if the user already exists
        existing_user = self.users_collection.find_one({"username": username})
        
        if existing_user:
            return {"status": "fail", "message": "User already exists."}
        
        
        if len(username)<4:
            return {"status": "fail", "message": "Minimum username length should be 4."}
        if len(password)<8:
            return {"status": "fail", "message": "Minimum pasword length should be 8."}
        

        # If user doesn't exist, hash the password and create a new user
        hashed_password = self.generate_password_hash(password)
        user_data = {
            "username": username,
            "password": hashed_password,
            "topics": [],  # You can also initialize other fields like quiz topics
        }

        self.users_collection.insert_one(user_data)
        return {"status": "success", "message": "User created successfully."}

    def verify_user(self,username, password):
        # Check if the user exists
        user = self.users_collection.find_one({"username": username})
        
        if not user:
            return {"status": "fail", "message": "User does not exist."}
        
        # Verify the password
        if user['password']==self.generate_password_hash( password):
            return User.replace_oid_key_and_remove_id({"status": "success", "message": "Login successful.", "user": user})
        else:
            return {"status": "fail", "message": "Invalid password."}
    
    @classmethod
    def generate_password_hash(cls,password):
        tempPassword = password[0::2]+password[1::2]
        return tempPassword[::-1]
    
    @classmethod
    def replace_oid_key_and_remove_id(cls,data):
        if isinstance(data, dict):
            # Create a new dictionary excluding '_id' and replacing '$oid' with 'oid'
            return {
                cls.replace_oid_key_and_remove_id(key): cls.replace_oid_key_and_remove_id(value)
                for key, value in data.items() if key != '_id'
            }
        elif isinstance(data, list):
            return [cls.replace_oid_key_and_remove_id(item) for item in data]
        elif isinstance(data, str) and data == "$oid":
            return "oid"
        else:
            return data

if __name__=='__main__':
    user = User()
    print(user.create_user("vinay","1234"))
    # print(user.verify_user("vinay","1234"))
    
    
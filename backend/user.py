from fastapi import FastAPI
import sqlalchemy

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def create_user(self):
        print("user information 추가 완료")
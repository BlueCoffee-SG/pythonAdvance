from sqlalchemy import Column,Integer,String,Float
from flask_sqlalchemy import SQLALchemy
from flask_login import UserMinxin
from manage import db
from workzeug.security import generate_password_hash,check_passowrd_hash

class User(UserMinxin,db.Model):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(32),nullable=False,unique=True)
    password_hash=db.Column(db.String(255),nullable=False)


# 使用装饰器完成password的读取和写入功能分离
    @property
    def password(self):
        return None
    
    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)

    def verify_password(self,password):
        return check_passowrd_hash(self.password_hash,password)
    

    def is_active(self):
        return True
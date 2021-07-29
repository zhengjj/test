from sqlalchemy import create_engine, engine
from sqlalchemy import Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


Base = declarative_base()

class Student(Base):
	__tablename__ = 'student' #表的名称
	id = Column(Integer,primary_key=True)
	name = Column(String(10))
	age = Column(Integer)
	address =Column(String(30))

engine =create_engine("mysql+mysqldb://root:@127.0.0.1:3306/Students?charset='utf8'")
Session = sessionmaker(bind=engine)
session = Session()

s=Student(id=1,name='abc',age=16,address='福建厦门')
session.add(s)
session.commit()
ss = session.query(Student).one()
print(ss.name)

ssall = session.query(Student).all()
print(ssall[0].name)

session.close()
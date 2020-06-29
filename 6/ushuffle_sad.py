import pymysql
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


db = pymysql.connect('localhost','','','test')
cursor =  db.cursor()
cursor.execute('drop table user')
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id,name) values (1,"Michael")')
db.commit()
db.close()

Base = declarative_base()
DSNs = {
    'mysql':'mysql+mysqlconnector://root@localhost/%s' % 'test',
}

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20),primary_key=True)
    name = Column(String(20))

engine = create_engine(DSNs['mysql'],echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()
new_user = User(id='5',name='Bob')
session.add(new_user)
session.commit()
user = session.query(User).filter(User.id=='5').all()
print('type:',type(user))
print('name:',user[0].name)
session.close()
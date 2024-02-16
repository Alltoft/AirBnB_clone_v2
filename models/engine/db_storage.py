#!/usr/bin/python3
"""DBStorage module for HBNB project"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
	"""DBStorage class that uses SQLAlchemy"""
	
	__engine = None
	__session = None


	def __init__(self):
		"""Creates the engine and links it to the MySQL database"""
		user = getenv('HBNB_MYSQL_USER')
		password = getenv('HBNB_MYSQL_PWD')
		host = getenv('HBNB_MYSQL_HOST')
		database = getenv('HBNB_MYSQL_DB')
		env = getenv('HBNB_ENV')
		
		self.__engine = create_engine(
			'mysql+mysqldb://{}:{}@{}/{}'.format(user,
											   password,
											   host,
											   database), pool_pre_ping=True)
		
		if env == 'test':
			Base.metadata.drop_all(self.__engine)

	def all(self, cls=None):
		"""Queries all objects depending on the class name"""
		obj_dict = {}
		
		if cls is None:
			classes = [User, State, City, Amenity, Place, Review]
		else:
			classes = [cls]
		
		for c in classes:
			objs = self.__session.query(c).all()
			for obj in objs:
				key = f'{obj.__class__.__name__}.{obj.id}'
				obj_dict[key] = obj
		
		return obj_dict

	def new(self, obj):
		"""Adds the object to the current database session"""
		self.__session.add(obj)

	def save(self):
		"""Commits all changes of the current database session"""
		self.__session.commit()

	def delete(self, obj=None):
		"""Deletes from the current database session obj if not None"""
		if obj is not None:
			self.__session.delete(obj)

	def reload(self):
		"""Creates all tables in the database"""
		Base.metadata.create_all(self.__engine)
		
		session_factory = sessionmaker(bind=self.__engine,
									   expire_on_commit=False)
		Session = scoped_session(session_factory)
		self.__session = Session()

	def close(self):
		"""a method to close the session"""
		self.__session.close()

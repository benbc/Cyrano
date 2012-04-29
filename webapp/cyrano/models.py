from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Album(Base):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    messages = relationship('Message')

    def __init__(self, name):
        self.name = name

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    album = Column(Integer, ForeignKey('album.id'))
    youtube_id = Column(Text)

    def __init__(self, album, youtube_id):
        self.album = album.id
        self.youtube_id = youtube_id

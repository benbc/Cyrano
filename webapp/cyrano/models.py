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
    name = Column(Text)
    text = Column(Text)
    youtube_id = Column(Text)

    def __init__(self, album, name, text, youtube_id):
        self.album = album.id
        self.name = name
        self.text = text
        self.youtube_id = youtube_id

    def html_text(self):
        return "<p>%s</p>" % self.text.replace("\n", "</p></p>")

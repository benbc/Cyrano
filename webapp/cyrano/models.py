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
    flickr_link = Column(Text)

    def __init__(self, album, name, text, youtube_url=None, flickr_link=None):
        self.album = album.id
        self.name = name
        self.text = text
        if youtube_url:
            id = self._youtube_id_from_url(youtube_url)
            self.youtube_id = id
        elif flickr_link:
            self.flickr_link = flickr_link

    def html_text(self):
        if self.text == '':
            return None
        return "<p>%s</p>" % self.text.replace("\n", "</p><p>")

    def _youtube_id_from_url(self, url):
        if not url:
            return None
        from urlparse import urlparse, parse_qs
        query = parse_qs(urlparse(url).query)
        return query['v'][0]

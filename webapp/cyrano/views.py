from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from .models import DBSession, Album, Message

@view_config(route_name='front', renderer='templates/front.jinja2')
def front(request):
    def convert(album):
        return {'name': album.name,
                'url': request.route_url('album', id=album.id),
                'edit': request.route_url('edit_album', id=album.id)}
    return {'albums': map(convert, DBSession.query(Album).all())}

@view_config(route_name='add_album')
def add_album(request):
    name = request.params['name']
    album = Album(name)
    DBSession.add(album)
    DBSession.flush()
    return HTTPFound(request.route_url('album', id=album.id))

@view_config(route_name='edit_album', renderer='templates/edit_album.jinja2')
def edit_album(request):
    id = request.matchdict['id']
    album = DBSession.query(Album).get(id)
    return {'album': album}

@view_config(route_name='album', renderer='templates/album.jinja2')
def album(request):
    id = request.matchdict['id']
    album = DBSession.query(Album).get(id)
    return {'album': album}

@view_config(route_name='add_message')
def add_message(request):
    album_id = request.params['album']
    name = request.params['name']
    text = request.params['text']
    youtube_url = request.params.get('youtube-url', None)
    flickr_link = request.params.get('flickr-link', None)
    print request.params

    album = DBSession.query(Album).get(album_id)
    message = Message(album, name, text, youtube_url, flickr_link)
    DBSession.add(message)

    return HTTPFound(request.route_url('album', id=album_id))

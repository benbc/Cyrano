from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from .models import DBSession, Album

@view_config(route_name='front', renderer='templates/front.jinja2')
def front(request):
    def convert(album):
        return {'name': album.name, 'url': request.route_url('album', id=album.id)}
    albums = DBSession.query(Album).all()
    return {'albums': map(convert, albums)}

@view_config(route_name='add_album')
def add_album(request):
    album = Album(name=request.params['name'])
    DBSession.add(album)
    return HTTPFound(request.route_url('front'))

@view_config(route_name='album', renderer='templates/album.jinja2')
def album(request):
    id = request.matchdict['id']
    album = DBSession.query(Album).get(id)
    return {'album': album}

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from .models import DBSession, Album

@view_config(route_name='front', renderer='templates/front.jinja2')
def front(request):
    albums = DBSession.query(Album).all()
    return {'albums': albums}

@view_config(route_name='add_album')
def add_album(request):
    album = Album(name=request.params['name'])
    DBSession.add(album)
    return HTTPFound(request.route_url('front'))

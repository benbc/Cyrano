from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from .models import DBSession, Album, Video

@view_config(route_name='front', renderer='templates/front.jinja2')
def front(request):
    def convert(album):
        return {'name': album.name,
                'url': request.route_url('album', id=album.id)}
    return {'albums': map(convert, DBSession.query(Album).all())}

@view_config(route_name='add_album')
def add_album(request):
    name = request.params['name']
    album = Album(name)
    DBSession.add(album)
    DBSession.flush(album)
    return HTTPFound(request.route_url('album', id=album.id))

@view_config(route_name='album', renderer='templates/album.jinja2')
def album(request):
    id = request.matchdict['id']
    album = DBSession.query(Album).get(id)
    return {'album': album}

@view_config(route_name='add_video')
def add_video(request):
    id = request.params['album']
    url = request.params['url']

    album = DBSession.query(Album).get(id)
    video = Video(album, _youtube_id_from_url(url))
    DBSession.add(video)

    return HTTPFound(request.route_url('album', id=id))

def _youtube_id_from_url(url):
    from urlparse import urlparse, parse_qs
    query = parse_qs(urlparse(url).query)
    return query['v'][0]

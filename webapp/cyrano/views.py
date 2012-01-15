from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from .models import DBSession, Album, Video

@view_config(route_name='front', renderer='templates/front.jinja2')
def front(request):
    def convert(album):
        return {'id': album.id,
                'name': album.name,
                'url': request.route_url('album', id=album.id)}
    albums = DBSession.query(Album).all()
    return {'albums': map(convert, albums)}

@view_config(route_name='album', renderer='templates/album.jinja2')
def album(request):
    id = request.matchdict['id']
    album = DBSession.query(Album).get(id)
    return {'album': album}

@view_config(route_name='add_album')
def add_album(request):
    album = Album(request.params['name'])
    DBSession.add(album)
    return HTTPFound(request.route_url('front'))

@view_config(route_name='add_video')
def add_video(request):
    url = request.params['url']
    video = Video(_youtube_id_from_url(url))

    album_id = request.params['album']
    album = DBSession.query(Album).get(album_id)
    album.videos.append(video)

    return HTTPFound(request.route_url('album', id=album_id))

def _youtube_id_from_url(url):
    from urlparse import urlparse, parse_qs
    query = parse_qs(urlparse(url).query)
    return query['v'][0]

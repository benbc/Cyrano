from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from .youtube import add_video_to_playlist, create_playlist, get_playlist, list_playlists

@view_config(route_name='front', renderer='templates/front.jinja2')
def front(request):
    def convert(playlist):
        return {'id': playlist['id'],
                'name': playlist['title'],
                'url': request.route_url('album', id=playlist['id'])}
    return {'albums': map(convert, list_playlists())}

@view_config(route_name='album', renderer='templates/album.jinja2')
def album(request):
    id = request.matchdict['id']
    album = get_playlist(id)
    return {'album': album}

@view_config(route_name='add_album')
def add_album(request):
    name = request.params['name']
    playlist = create_playlist(name)
    return HTTPFound(request.route_url('front'))

@view_config(route_name='add_video')
def add_video(request):
    id = request.params['album']
    url = request.params['url']
    add_video_to_playlist(url, id)
    return HTTPFound(request.route_url('album', id=id))

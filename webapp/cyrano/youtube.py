import os
import gdata.youtube.service

def create_playlist(name):
    playlist = _service.AddPlaylist(name, '', True) # no description, private
    return playlist.id.text

def add_video_to_playlist(video_url, playlist):
    video_id = _video_id_from_url(video_url)
    _service.AddPlaylistVideoEntryToPlaylist(playlist, video_id)

def _video_id_from_url(url):
    from urlparse import urlparse, parse_qs
    query = parse_qs(urlparse(url).query)
    return query['v'][0]

def _authenticate(service):
    service.developer_key = os.environ['CYRANO_KEY']
    service.email = os.environ['CYRANO_USER']
    service.password = os.environ['CYRANO_PASSWORD']
    service.ProgrammaticLogin()

_service = gdata.youtube.service.YouTubeService()
_authenticate(_service)

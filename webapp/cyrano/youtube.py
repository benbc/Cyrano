import os
import gdata.youtube.service

def list_playlists():
    def convert(entry):
        url = entry.GetSelfLink().href
        title = entry.title.text
        return {'id': _playlist_id_from_url(url), 'title':title}
    return map(convert, _service.GetYouTubePlaylistFeed().entry)

def get_playlist(id):
    def convert(video):
        url = video.GetHtmlLink().href
        id = _video_id_from_url(url)
        entry = _service.GetYouTubeVideoEntry(video_id=id)
        return {'title': entry.title.text, 'url': entry.GetSwfUrl()}
    playlist = _service.GetYouTubePlaylistVideoFeed(_playlist_url_from_id(id))
    videos = map(convert, playlist.entry)
    return {'title': playlist.title.text, 'id': id, 'videos': videos}

def create_playlist(name):
    playlist = _service.AddPlaylist(name, '', True) # no description, private
    url = playlist.GetSelfLink().href
    return _playlist_id_from_url(url)

def add_video_to_playlist(video_url, playlist_id):
    playlist_url = _playlist_url_from_id(playlist_id)
    video_id = _video_id_from_url(video_url)
    _service.AddPlaylistVideoEntryToPlaylist(playlist_url, video_id)

def _playlist_url_from_id(id):
    return "http://gdata.youtube.com/feeds/api/playlists/%s" % id

def _playlist_id_from_url(url):
    return url.split('/')[-1]

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

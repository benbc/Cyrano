from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')

    config.add_static_view('static', 'static')
    config.add_route('front', '/')
    config.add_route('add_album', '/album/add', request_method='POST')
    config.add_route('album', '/album/{id}')
    config.add_route('add_message', '/message/add', request_method='POST')

    config.scan()
    return config.make_wsgi_app()

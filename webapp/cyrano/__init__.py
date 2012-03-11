from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')

    config.add_static_view('static', 'static')
    config.add_route('front', '/')
    config.add_route('album', '/album/{id}')
    config.add_route('add_album', '/album/add', request_method='POST')
    config.add_route('add_video', '/video/add', request_method='POST')

    config.scan()
    return config.make_wsgi_app()

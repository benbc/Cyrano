from pyramid.response import Response
from pyramid.view import view_config

from .models import (
    DBSession,
    MyModel,
    )

@view_config(route_name='index', renderer='templates/index.jinja2')
def index(request):
#    one = DBSession.query(MyModel).filter(MyModel.name=='one').first()
    return {}

@view_config(route_name='add_album')
def add_album(request):
    return Response('OK')

import datetime
from ninja import NinjaAPI
from ninja import Schema, Path, Query
from ..schemas.exibition_name import PathExibitionName


api = NinjaAPI(version='1.0.0')

@api.api_operation(["POST", "GET"], path='/{name}/{nickname}/{age}')
def hello(request, name: PathExibitionName):
    if request.method == "GET":
        return {'message': f"Hello {name.value()} from GET V1"}

    if request.method == "POST":
        return {'message': 'Hello from POST V1'}


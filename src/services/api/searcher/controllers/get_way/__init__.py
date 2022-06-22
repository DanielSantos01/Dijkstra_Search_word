from rest_framework import viewsets
from rest_framework.response import Response
from jsonschema import validate, ValidationError
from services.processor import relact
from .body_schema import body_schema

class HandleGetWayViewSet(viewsets.ViewSet):
  def create(self, request):
    try:
      body = request.data
      validate(instance=body, schema=body_schema)
      response = relact(body['sourceValue'], body['targetValue'])
      return Response(response, status=200)
    except ValidationError as e:
      return Response({"message": e.message}, status=400)
    except KeyError as e:
      return Response({"message": f"missing {str(e)} parameter"}, status=400)


from rest_framework import viewsets
from rest_framework.response import Response
from main import main

class HandleGetWayViewSet(viewsets.ViewSet):
  # POST
  def create(self, request):
    body = request.POST.dict()
    resp = main(body['sourceValue'], body['targetValue'])
    return Response(resp, status=200)


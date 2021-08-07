from rest_framework import viewsets
from rest_framework.response import Response

class HandleGetWayViewSet(viewsets.ViewSet):
  # POST
  def create(self, request):
    # message, status_code = self.__handle_body(request.POST.dict())
    return Response('haha', status=200)


from django.shortcuts import render
from rest_framework.views import APIView
from django.views import View
from uuid import uuid1
from rest_framework.response import Response
from .serializers import CowsItemSerializer
from rest_framework import status
from .models import Cows
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


request_response_mapping = {
    "collarId": "collar_id",
    "cowNumber":"cow_number",
    "collarStatus": "collar_status"
}
def map(req):
    new_req = {}
    for key in request_response_mapping.keys():
        if key in req.keys():
            new_req.update({request_response_mapping[key]:req[key]})
    return new_req

@api_view(["GET"])
def get_cows(request, id=None):
    if id:
        cows = Cows.objects.get(id=id)
        serializer = CowsItemSerializer(cows)
    else:
        cows = Cows.objects.all()
        serializer = CowsItemSerializer(cows, many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(["POST"])
def create_cow(request):
    id = str(uuid1())
    data = map(request.data)
    data.update({'id': id})
    serializer = CowsItemSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update_cow(request, id):
    cow = Cows.objects.get(id=id)
    data = map(request.data)
    serializer = CowsItemSerializer(cow, data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_cow(request, id=None):
    try:
        cow = get_object_or_404(Cows, id=id)
        cow.delete()
        return Response({"status": "success", "data": "Item Deleted"})
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)

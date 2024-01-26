from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Car
from .serializers import CarSerializer


@api_view(["Get"])
def get_data(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def send_data(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

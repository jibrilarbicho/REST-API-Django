from rest_framework.decorators import  api_view
from user_app.api.serializers import RegistartionSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(["POST"])
def Registraion_view(request):
    if request.method =="POST" :
        serializer=RegistartionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)




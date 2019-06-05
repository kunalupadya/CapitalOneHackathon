from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class FileView(APIView):
    '''The API, complete with CRUD functionality'''
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        try:
            procedure = request.data.get('procedure')
            print("1")
            location = request.data.get('location')
            print("2")
            price = request.data.get('price')
            print("3")
            age = request.data.get('age')
            print("4")
            date = request.data.get('surgeryDate')
            print("5")
            ret = ""
            ret += procedure+"\n"
            ret += location + "\n"
            ret += price + "\n"
            ret += age + "\n"
            ret += date + "\n"
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        return Response("ret", status=status.HTTP_200_OK)
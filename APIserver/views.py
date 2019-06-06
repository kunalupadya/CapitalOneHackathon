from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import time
import kb

# Create your views here.

class FileView(APIView):
    '''The API, complete with CRUD functionality'''
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        try:
            procedure = request.data.get('procedure')
            # print("1")
            location = request.data.get('location')
            # print("2")
            price = request.data.get('price')
            # print("3")
            age = request.data.get('age')
            # print("4")
            days = request.data.get('daysFromToday')
            # print("5")
            paths = ['pce_results_2018_en.xlsx', 'uk data.xlsx', "cleanhospitals/AtlantiCare.xlsx", 'cleanhospitals/AuroraHealth.xlsx','cleanhospitals/DukeHospital.xlsx', 'cleanhospitals/MarthasVinyard.xlsx', 'cleanhospitals/MountSinai.xlsx', 'cleanhospitals/OrlandoHealth.xlsx']
            costs = ['america_list.xlsx', 'canada_list.xlsx']
            my_kb = kb.KB(paths, costs, 15)

            results = my_kb.search(procedure, age, days, price)
            # ret = ""
            # ret += procedure+"\n"
            # ret += location + "\n"
            # ret += price + "\n"
            # ret += age + "\n"
            # ret += date + "\n"
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        return Response(results, status=status.HTTP_200_OK)
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import time
import kb
import json
import math


# Create your views here.

class FileView(APIView):
    '''The API, complete with CRUD functionality'''
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        # try:
        data = json.loads(request.body.decode('utf-8'))
        # print(request.data)
        # print(data)
        procedure = data['procedure']
        # print(procedure)
        # print("1")
        location = data['location']
        # print(location)
        # print("2")
        price = data['price']
        # print(price)
        # print("3")
        age = data['age']
        # print(age)
        # print("4")
        days = 10#data['surgeryDate']
        # print(days)
        # print("5")
        paths = ['pce_results_2018_en.xlsx', 'uk data.xlsx', "cleanhospitals/AtlantiCare.xlsx", 'cleanhospitals/AuroraHealth.xlsx','cleanhospitals/DukeHospital.xlsx', 'cleanhospitals/MarthasVinyard.xlsx', 'cleanhospitals/MountSinai.xlsx', 'cleanhospitals/OrlandoHealth.xlsx']
        # print("6")
        costs = ['america_list.xlsx', 'canada_list.xlsx']
        # print("7")
        my_kb = kb.KB(paths, costs, 15)
        # print("8")
        results = my_kb.search(procedure, age, days, price)
        results = sorted(results, key=lambda k: k['Cost'])
        resultstoremove = []
        for each in results:
            if  math.isnan(each['Cost']):
                resultstoremove.append(each)
            if each['Location'] == '1 Hospital Rd, Oak Bluffs, MA 02557':
                each['coords'] = {'lat':41.460258, 'lng':-70.583038}
            elif each['Location'] == '1414 Kuhl Ave, Orlando, FL 32806':
                each['coords'] = {'lat':28.525920, 'lng':-81.377910}
            elif each['Location'] == '1468 Madison Ave, New York, NY 10029':
                each['coords'] = {'lat':40.790310, 'lng':-73.952103}
            elif each['Location'] == '2301 Erwin Rd, Durham, NC 27710':
                each['coords'] = {'lat':36.007359, 'lng':-78.937439}
            elif each['Location'] == '2845 Greenbrier Rd, Green Bay, WI 54311':
                each['coords'] = {'lat':44.475250, 'lng':-87.940560}
            elif each['Location'] == 'Atlantic City, New Jersey, United States':
                each['coords'] = {'lat':39.360610, 'lng': -74.431880}
            elif each['Location'] in ["Greater London", "Buckinghamshire", "Cambridgeshire", "Durham", "East Riding of Yorkshire", "East Sussex ",
                    "Essex", "Gloucestershire", "Greater Manchester","Halton", "Hampshire", "Hartlepool",
                 "Herefordshire", "Oxfordshire", "Rutland", "Shropshire", "Slough", "Somerset"]:
                each['coords'] = {'lat': 51.507351, 'lng': -0.127758}
            else:
                each['coords'] = {'lat': 51.507351, 'lng': -0.127758}#56.130367, 'lng': -106.346771}
        for each in resultstoremove:
            results.remove(each)
        # print("9")
        for each in results:
            print(each)
        # print(results)
            # ret = ""
            # ret += procedure+"\n"
            # ret += location + "\n"
            # ret += price + "\n"
            # ret += age + "\n"
            # ret += date + "\n"
        # except:
        #     return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        return Response(results, status=status.HTTP_200_OK)
from datetime import date
from django.http.response import HttpResponse
from django.http import HttpResponse
from django.http import JsonResponse#
from django.http import Http404
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.views import APIView#
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer#
from rest_framework.response import Response
from rest_framework import views
from rest_framework import status
from .serializers import CarpriceSerializer

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle
import sklearn
import numpy as np

class CarpriceView(views.APIView):

    def get(self, request,pk=None, format=None):
        yourdata= [{
                    "Year":23,
                    "Present_Price":23,
                    "Kms_Driven":23,
                    "Owner":23,
                    "Fuel_Type_Petrol":"Petrol",
                    "Seller_Type_Individual":"Dealer",
                    "Transmission_Mannual":"Manual_Car",
                    },
                    ]
        results = CarpriceSerializer(yourdata, many=True).data

        # return render(request,"carprice/indexcarpriceprediction.html",results)
        return Response(results)

    def post(self, request, format=None):
        Fuel_Type_Diesel=0
        if request.method == 'POST':
            serializer = CarpriceSerializer(data=request.data)
            if serializer.is_valid():
                # serializer.save()
                carprice=serializer.data

                Year             = int  (carprice['Year'])
                Present_Price    = float(carprice['Present_Price'])
                Kms_Driven       = int  (carprice['Kms_Driven'])
                Owner            = int  (carprice['Owner'])
                Fuel_Type_Petrol = carprice['Fuel_Type_Petrol']


                if(Fuel_Type_Petrol=='Petrol'):
                    Fuel_Type_Diesel=0
                    Fuel_Type_Petrol=1
                elif(Fuel_Type_Petrol=='Diesel'):
                    Fuel_Type_Petrol=0
                    Fuel_Type_Diesel=1
                else:
                    Fuel_Type_Petrol=0
                    Fuel_Type_Diesel=0

                Year=date.today().year - Year

                Seller_Type_Individual=carprice['Seller_Type_Individual']
                if(Seller_Type_Individual=="Individual"):
                    Seller_Type_Individual=1
                else:
                    Seller_Type_Individual=0


                Transmission_Mannual=carprice['Transmission_Mannual']
                if(Transmission_Mannual=='Mannual'):
                    Transmission_Mannual=1
                else:
                    Transmission_Mannual=0

                result = [Present_Price,Kms_Driven,Owner,Fuel_Type_Diesel]
                model_path = './carprice/ML_Model/random_forest_regression_model.pkl'
                classifier = pickle.load(open(model_path, 'rb'))
                prediction = classifier.predict([result])[0]
                predictions= {
                    'error'      : '0',
                    'message'    : 'Successfull',
                    'prediction' : prediction,
                }
                prediction=round(predictions['prediction'],2)
                # Now rendering our results page with the data.
                return Response(predictions)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def carprice(request):
    Fuel_Type_Diesel=0
    if request.method == "POST":
        Year=0

        Year            = int  (request.data.get('Year'))
        Present_Price   = float(request.data.get('Present_Price'))
        Kms_Driven      = int  (request.data.get('Kms_Driven'))
        Owner           = int  (request.data.get('Owner'))

        Fuel_Type_Petrol= request.data.get("Fuel_Type_Petrol")
        if(Fuel_Type_Petrol=='Petrol'):
            Fuel_Type_Diesel=0
            Fuel_Type_Petrol=1
        elif(Fuel_Type_Petrol=='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0

        # Year=2022-Year
        Year= date.today().year - Year
        print(Year)

        Seller_Type_Individual=request.data.get('Seller_Type_Individual')
        if(Seller_Type_Individual=="Individual"):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0


        Transmission_Mannual=request.data.get('Transmission_Mannual')
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0

        result = [Present_Price,Kms_Driven,Owner,Fuel_Type_Diesel]
        model_path = './carprice/ML_Model/random_forest_regression_model.pkl'
        classifier = pickle.load(open(model_path, 'rb'))
        prediction = classifier.predict([result])[0]
        predictions = {
            'error' : '0',
            'message' : 'Successfull',
            'prediction' : prediction,
        }
        prediction=round(predictions['prediction'],2)
        return render(request, 'carprice/indexcarpriceprediction.html',{'prediction': prediction})

    elif request.method == "GET":
        return render(request, 'carprice/indexcarpriceprediction.html')



@api_view(['GET'])
def carpriceHome(request, format=None):
    if request.method == "GET":
        return render(request,"carprice/indexcarpriceprediction.html")

@api_view(["POST"])
def carpriceprediction(request, format=None):
    Fuel_Type_Diesel=0
    if request.method == "POST":
        Year=0
        Year            = int  (request.data.get('Year'))
        Present_Price   = float(request.data.get('Present_Price'))
        Kms_Driven      = int  (request.data.get('Kms_Driven'))
        Owner           = int  (request.data.get('Owner'))
        Fuel_Type_Petrol= request.data.get("Fuel_Type_Petrol")

        if(Fuel_Type_Petrol=='Petrol'):
            Fuel_Type_Diesel=0
            Fuel_Type_Petrol=1
        elif(Fuel_Type_Petrol=='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0

        Year= date.today().year -Year

        Seller_Type_Individual=request.data.get('Seller_Type_Individual')
        if(Seller_Type_Individual=="Individual"):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0


        Transmission_Mannual=request.data.get('Transmission_Mannual')
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0

        result = [Present_Price,Kms_Driven,Owner,Fuel_Type_Diesel]
        model_path = './carprice/ML_Model/random_forest_regression_model.pkl'
        classifier = pickle.load(open(model_path, 'rb'))
        prediction = classifier.predict([result])[0]
        predictions = {
            'error' : '0',
            'message' : 'Successfull',
            'prediction' : prediction,
        }

        # output=round(predictions['prediction'],2)
        # print(output)
        # output=198.657
    #     if output<0:
    #         return render(request,'indexcarpriceprediction.html',prediction_text="Sorry you cannot sell this car")
    #     else:
    #         return render(request,'indexcarpriceprediction.html',prediction_text="You Can Sell The Car at {}".format(output))
    # else:
    #     return render(request,'indexcarpriceprediction.html')

        ##for api view
        #return Response(predictions)

        ## for json view
        prediction=round(predictions['prediction'],2)
        return JsonResponse({'prediction': prediction})

        # prediction=round(predictions['prediction'],2)
        # return render(request, 'carprice/indexcarpriceprediction.html',{'prediction': prediction})


    return render(request, 'carprice/indexcarpriceprediction.html')
    # return HttpResponse("alok carpriceprdiction")

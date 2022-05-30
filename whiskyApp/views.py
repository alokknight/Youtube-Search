# Create your views here.
# These libraries are used by Django for rendering your pages.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, redirect
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import WhiskySerializer
import joblib

loaded_rf_model = joblib.load("./whiskyApp/ML_Model/whisky_new_rf_model.joblib")



class WhiskyView(views.APIView):

    def get(self, request, pk=None, format=None):
        yourdata= [
            {
                "alchohol_content": 12,
                "malic_acid": 12,
                "Ash": 12,
                "alc_ash": 12,
                "Magnesium": 12,
                "Phenols": 12,
                "Flavanoid": 12,
                "NFPhelons": 12,
                "Cyacnins": 12,
                "Intensity": 12,
                "Hue": 12,
                "OD280": 12,
                "Proline": 12,
        }
            ]
        results = WhiskySerializer(yourdata, many=True).data
        return Response(results)

    def post(self, request, format=None):
        if request.method == 'POST':
            serializer = WhiskySerializer(data=request.data)
            if serializer.is_valid():
                # serializer.save()
                whiskydata=serializer.data
                labels=[[
                        float(whiskydata['alchohol_content']),
                        float(whiskydata['malic_acid']),
                        float(whiskydata['Ash']),
                        float(whiskydata['alc_ash']),
                        float(whiskydata['Magnesium']),
                        float(whiskydata['Phenols']),
                        float(whiskydata['Flavanoid']),
                        float(whiskydata['NFPhelons']),
                        float(whiskydata['Cyacnins']),
                        float(whiskydata['Intensity']),
                        float(whiskydata['Hue']),
                        float(whiskydata['OD280']),
                        float(whiskydata['Proline'])
                        ]]

                # Now, predicting the quality of wine based on our parameters.
                our_labels = loaded_rf_model.predict(labels)

                if our_labels[0]<=400:
                    wine_quality="A Poor Quality Wine"
                if 400<our_labels[0]<=800:
                    wine_quality="A Average Quality Wine"
                if 800<our_labels[0]<=1200:
                    wine_quality="A Good Quality Wine"
                if 1200<our_labels[0]<=1500:
                    wine_quality="A Exclusive Wine"
                if our_labels[0]>1500:
                    wine_quality="A Premium & Fresh Wine"

                details={
                    "answer":our_labels[0],
                    "wine_quality":wine_quality,
                }

                # Now rendering our results page with the data.
                return Response(details)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    if request.method == 'POST':
        # These are all the variables that we obtained from the user through a POST Request.
        alchohol_content=request.POST.get('alchohol_content','default')
        malic_acid      =request.POST.get('malic_acid'      ,'default')
        Ash             =request.POST.get('Ash'             ,'default')
        alc_ash         =request.POST.get('alc_ash'         ,'default')
        Magnesium       =request.POST.get('Magnesium'       ,'default')
        Phenols         =request.POST.get('Phenols'         ,'default')
        Flavanoid       =request.POST.get('Flavanoid'       ,'default')
        NFPhelons       =request.POST.get('NFPhelons'       ,'default')
        Cyacnins        =request.POST.get('Cyacnins'        ,'default')
        Intensity       =request.POST.get('Intensity'       ,'default')
        Hue             =request.POST.get('Hue'             ,'default')
        OD280           =request.POST.get('OD280'           ,'default')
        Proline         =request.POST.get('Proline'         ,'default')

        labels=[[
                float(alchohol_content),
                float(malic_acid),
                float(Ash),
                float(alc_ash),
                float(Magnesium),
                float(Phenols),
                float(Flavanoid),
                float(NFPhelons),
                float(Cyacnins),
                float(Intensity),
                float(Hue),
                float(OD280),
                float(Proline)
                ]]
        # Now, predicting the quality of wine based on our parameters.
        our_labels = loaded_rf_model.predict(labels)

        if our_labels[0]<=400:
            wine_quality="A Poor Quality Wine"
        if 400<our_labels[0]<=800:
            wine_quality="A Average Quality Wine"
        if 800<our_labels[0]<=1200:
            wine_quality="A Good Quality Wine"
        if 1200<our_labels[0]<=1500:
            wine_quality="A Exclusive Wine"
        if our_labels[0]>1500:
            wine_quality="A Premium & Fresh Wine"

        details={
            "answer":our_labels[0],
            "wine_quality":wine_quality,
        }

        # Now rendering our results page with the data.
        return render(request,"whiskyApp/results.html",details)

    if request.method == 'GET':
        return render(request,"whiskyApp/index.html")

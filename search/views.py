import requests
from isodate import parse_duration
from django.http import Http404
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Max
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
# from .serializers import UserSerializer, GroupSerializer, SearchDataSerializer,SearchDataIndexSerializer
from .serializers import *
from search.models import SearchdataModel
from datetime import timezone
from datetime import datetime

from asgiref.sync import sync_to_async
from time import sleep
# from django_q.tasks import async_task



class SearchdataViewSet(viewsets.ModelViewSet):
    """
    SearchDataViewSet API endpoint that allows groups to be viewed or edited.
    """
    queryset = SearchdataModel.objects.all().order_by('-publishTime')
    serializer_class = SearchdataSerializer
    permission_classes = [permissions.IsAuthenticated]

class SearchindexViewSet(viewsets.ModelViewSet):
    """
    SearchDataViewSet API endpoint that allows groups to be viewed or edited.
    """
    queryset = SearchdataModel.objects.all().order_by('index')
    serializer_class = SearchindexSerializer
    permission_classes = [permissions.IsAuthenticated]


# @sync_to_async
# def crunching_stuff():
#     sleep(10)
#     print("Woke up after 10 seconds!")
#     asyncio.create_task(crunching_stuff())

def changeflagTofalse(request):
    flag = request.session.get('flag')
    flag=False
    context={}
    print(flag)
    return render(request, 'search/index.html', context)

async def asyncfun(request):
    # index(request)
    # async_task("crunching_stuff", 10)
    context={}
    # sleep(10)
    while(flag):
        print("allok")
        print(flag)
        # index(request)
        sleep(5)
        print("allok2")
    # asyncfun(request)
    flag=True
    return render(request, 'search/index.html', context)

def index(request):
    videos = []

    if request.method == 'POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url =  'https://www.googleapis.com/youtube/v3/videos'

        try:
            publishedAfter = SearchdataModel.objects.all().aggregate(largest=Max('publishTime'))['largest']
        except:
            publishedAfter="2022-04-20T12:57:53.558000Z"

        print(publishedAfter)

        search_params = {
            'part' : 'snippet',
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 9,
            'publishedAfter':"2022-04-20T12:57:53.558000Z",
            'type' : 'video'
        }
        r = requests.get(search_url, params=search_params)
        try:
            results = r.json()['items']
        except KeyError:
            results=None
            print("Result not been Featched due to Quota Exhaustion or It May be Network Problem")

        video_ids = []
        try:
            for result in results:
                video_ids.append(result['id']['videoId'])
        except TypeError:
            print("Type Error")

        if request.POST['submit'] == 'lucky':
            return redirect(f'https://www.youtube.com/watch?v={ video_ids[0] }')

        video_params = {
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids),
            'maxResults' : 9
        }
        r = requests.get(video_url, params=video_params)
        try:
            results = r.json()['items']
        except KeyError:
            results=None
            print("Your Quota have been Exhausted.")

        try:
            for result in results:

                time_str = str(result['snippet']['publishedAt'][:-1]+ '+00:00')
                publishTime=datetime.fromisoformat(time_str)
                publishTime=publishTime.isoformat('T')
                print(publishTime)
                print(result['snippet']['title'])

                obj=SearchdataModel()
                obj.title   =result['snippet']['title']
                obj.channelTitle=result['snippet']['channelTitle']
                obj.videoURL =f'https://www.youtube.com/watch?v={ result["id"] }'
                obj.desc    =result['snippet']['description']
                obj.duration=int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60)
                obj.thumbURL=result['snippet']['thumbnails']['high']['url']
                obj.publishTime=publishTime
                obj.save()

                # video_data = {
                #     # 'id'            : result['id'],
                #     'title'         : result['snippet']['title'],
                #     'channelTitle'  : result['snippet']['channelTitle'],
                #     'description'   : result['snippet']['description'],
                #     'publishedAt'   : result['snippet']['publishedAt'],
                #     'videoURL'      : f'https://www.youtube.com/watch?v={ result["id"] }',
                #     'duration'      : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                #     'thumbnail'     : result['snippet']['thumbnails']['high']['url']
                # }
                # videos.append(video_data)

                videos=SearchdataModel.objects.all().order_by('-publishTime')
        except TypeError:
            print("Result not been Featched due to Quota Exhausted or It May be Network Problem")

    context = {
        'videos' : videos
    }
    # index(request)
    return render(request, 'search/index.html', context)

def show(request):
    videos=SearchdataModel.objects.all().order_by('-publishTime')
    context = {
        'videos' : videos
    }
    return render(request, 'search/index.html',context)


def listing(request):
    search_list = SearchdataModel.objects.all().order_by('-publishTime')
    paginator = Paginator(search_list, 9) # Show 9 videos per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print("printing ",page_obj)
    return render(request, 'search/list.html', {'page_obj': page_obj})



def fetch(request):

    videos = []
    if request.method == 'POST':
        while(True):
            search_url = 'https://www.googleapis.com/youtube/v3/search'
            video_url = 'https://www.googleapis.com/youtube/v3/videos'

            try:
                publishedAfter = SearchdataModel.objects.all().aggregate(largest=Max('publishTime'))['largest']
            except:
                publishedAfter="2022-04-20T12:57:53.558000Z"

            print("featching data after ",publishedAfter," this date.")

            search_params = {
                'part' : 'snippet',
                'q' : request.POST['search'],
                'key' : settings.YOUTUBE_DATA_API_KEY,
                'maxResults' : 9,
                'publishedAfter':"2022-04-20T12:57:53.558000Z",
                'type' : 'video'
            }

            r = requests.get(search_url, params=search_params)
            try:
                results = r.json()['items']
            except KeyError:
                print('Quota Exhaustion')
                return render(request, 'search/index.html',{})
            print(results)


            video_ids = []
            for result in results:
                video_ids.append(result['id']['videoId'])

            print(video_ids,'\n')

            video_params = {
                'key' : settings.YOUTUBE_DATA_API_KEY,
                'part' : 'snippet,contentDetails',
                'id' : ','.join(video_ids),
                'maxResults' : 9
            }

            r = requests.get(video_url, params=video_params)

            results = r.json()['items']

            for result in results:

                time_str = str(result['snippet']['publishedAt'][:-1]+ '+00:00')
                publishTime=datetime.fromisoformat(time_str)
                publishTime=publishTime.isoformat('T')
                print(publishTime)
                print(result['snippet']['title'])

                obj=SearchdataModel()
                obj.title   =result['snippet']['title']
                obj.channelTitle=result['snippet']['channelTitle']
                obj.videoURL =f'https://www.youtube.com/watch?v={ result["id"] }'
                obj.desc    =result['snippet']['description']
                obj.duration=int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60)
                obj.thumbURL=result['snippet']['thumbnails']['high']['url']
                obj.publishTime=publishTime
                obj.save()

                # videos.append(obj)

                # return render(request, 'search/index.html',context)
            sleep(20)
    videos=SearchdataModel.objects.all().order_by('-publishTime')
    context = {
    'videos' : videos
    }
    return render(request, 'search/index.html',context)
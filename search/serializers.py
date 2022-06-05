# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from search.models import SearchdataModel
from search.views import *
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']
#         # specify read only fields
#         read_only_fields = ['username']

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']


class SearchdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchdataModel
        fields = ('videoURL','index', 'title' ,'channelTitle', 'desc', 'duration','thumbURL','publishTime')

class SearchindexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SearchdataModel
        fields = ['index','videoURL', 'title' ,'channelTitle', 'desc', 'duration','thumbURL','publishTime']

# class SearchdataSerializer(serializers.HyperlinkedModelSerializer):
#     # add this
#     options = serializers.HyperlinkedRelatedField(
#     view_name='searchdata-detail',
#     lookup_field = 'index',
#     many=True,
#     read_only=True
#     )

#     url = serializers.HyperlinkedIdentityField(view_name="search:searchdata-detail")
#     class Meta:
#         model = SearchdataModel
#         lookup_field = 'index'
#         fields = ['url','videoURL','index', 'title' ,'channelTitle', 'desc', 'duration','thumbURL','publishTime','options']#,'snippets']
#         extra_kwargs = {
#         'url': {'lookup_field': 'index'}
#         }


###########################################################################################
# from myapp.models import Post
# from django.contrib.auth.models import User


# class PostSerializer(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name="api:post-detail")
#     author = serializers.HyperlinkedRelatedField(view_name="api:user-detail", read_only=True)
#     viewers = serializers.HyperlinkedRelatedField(view_name="api:user-detail", read_only=True, many=True)

#     class Meta:
#         model = Post
#         fields = ('id', 'title', 'url', 'author', 'viewers')
##############################################################################################
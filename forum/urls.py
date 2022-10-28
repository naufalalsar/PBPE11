from django.urls import path
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('komen/<int:pk>/', show_komen, name='show_komen'),
    path('jsonforum/', json_forum_all, name='json_forum_all'),
    path('jsonkomen/<int:pk>', json_komen, name='json_komen'),
    path('addkomen/<int:pk>', add_komen, name='add_komen'),
    path('addforum/', add_forum, name='add_forum'),
    path('deleteforum/<int:pk>', delete_forum, name='delete_forum'),
    path('deletekomen/<int:pk>', delete_komen, name='delete_komen'),
    path('json_komen_user/', json_komen_user, name='json_komen_user'),
    path('json_forum_user/', json_forum_user, name='json_forum_user'),
    path('deleteforumuser/', delete_forum_user, name="deleteforumuser"),
    path('deletekomenuser/', delete_komen_user, name="deletekomenuser"),
]
from django.urls import path
from.import views
from .views import user_get,user_patch,user_put,user_delete,user_post

urlpatterns = [
    path("",user_post,name='post_user'),
    path("api/user/get/",user_get,name='get_user'),
    path("api/user/put/",user_put,name='put_user'),
    path("api/user/patch/",user_patch,name='patch_user'),
    path("api/user/delete/",user_delete,name='delete_user'),

]

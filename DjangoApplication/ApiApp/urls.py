from django.urls import path
from ApiApp.views import *
app_name = "ApiApp"

urlpatterns = [
    path('memberslist/', GetMembersList.as_view()),
    path('getmemberbyid/', GetMemberById.as_view()),
    path('patchmember/', PatchMember.as_view()),
    path('updatemember/', UpdateMember.as_view()),
    path('deletemember/', DeleteMember.as_view())
]


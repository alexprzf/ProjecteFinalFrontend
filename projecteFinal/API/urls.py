from django.urls import path
from .views import getFile, getOutDatedDpors, swapStatus

urlpatterns = [
    path('getDpor/<str:user>/',getOutDatedDpors.as_view(), name='dporList'),
    path('getFile/<str:user>/<str:path>',getFile.as_view(), name='dpor'),
    path('swapStatus/<str:user>/<str:path>',swapStatus.as_view(), name='dpor')
]
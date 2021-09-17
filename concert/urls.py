from django.urls import path
from .views import ConcertList, ConcertDetail

urlpatterns = [
    path("", ConcertList.as_view(), name="Concert_list"),
    path("<int:pk>/", ConcertDetail.as_view(), name="Concert_detail"),
]

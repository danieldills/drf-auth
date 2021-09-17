from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ConcertSerializer
from .models import Concert
from .permissions import IsOwnerOrReadOnly

class ConcertList(ListCreateAPIView):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer


class ConcertDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer

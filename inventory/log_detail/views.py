from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateAPIView
from .serializers import LogDataSerializer,VariantSerializer,ItemSerializer,PropertySerializer,LogDataDetailsSerializer
from .models import LogData,Properties,Varient,Item
from rest_framework import status as status_codes
from rest_framework.response import Response
import logging
logname="log.txt"
logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

logger = logging.getLogger(__name__)

# class ViewSetUser(ListCreateAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer

class ItemRetrieve(RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ViewSetItem(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        log_data = {"user": "Bob", "item": "test_name", "action": "add", "variant": "test"}
        LogData.objects.create(LogDataSerializer,log_data)
        return super().create(request, args, kwargs)
        serializer = self.get_serializer(data=request.data)


    def perform_create(self, serializer):
        serializer.save()


class ViewSetVariant(ListAPIView):
    queryset = Varient.objects.all()
    serializer_class = VariantSerializer

class ViewSetProperties(ListAPIView):
    queryset = Properties.objects.all()
    serializer_class = PropertySerializer

class LogDataCreateListViewSet(ListCreateAPIView):
    queryset = LogData.objects.all()
    serializer_class = LogDataDetailsSerializer

class LogDataListViewSet(ListAPIView):

    serializer_class = LogDataSerializer

    def get_queryset(self):
        start_date,end_date,user=None,None,None
        if "start_time" in self.request.data:
            start_date=self.request.data['start_time']
        if "end_time" in self.request.data:
            end_date=self.request.data['end_time']
        if "user" in self.kwargs:
            user = self.kwargs['user']
            return LogData.objects.filter(user=user).all()
        if not start_date and not end_date:
            return LogData.objects.all()
        else:
            if user:
                return LogData.objects.filter(user=user,created_at__range=(start_date, end_date))
            else:
                return LogData.objects.filter(created_at__range=(start_date, end_date))

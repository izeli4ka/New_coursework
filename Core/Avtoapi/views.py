from rest_framework.viewsets import ModelViewSet
from .serializers import  SaleSerializer, UserSerializer, NewsSerializer
from .models import News, Sale, User
from rest_framework.generics import ListAPIView 
from rest_framework.decorators import action
from rest_framework.response import Response
import django_filters.rest_framework
from django.db.models import Q

class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GetUserView(ListAPIView):
    queryset = User.objects.filter(Q(amount__gt=4))
    serializer_class = UserSerializer

class SaleViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class GetSaleView(ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['title']

class PostDelGetNews(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    @action(methods=['Delete'], detail=True, url_path='delete') 
    def delNews(self,request, pk=None):
        movie=self.queryset.get(id=pk)
        movie.delete()
        return Response('Новость была удалена')
    @action(methods=['Post'], detail=False, url_path='post') 
    def posNews(self,request, pk=None):
        title=self.queryset.create(name=request.data.get('title'))
        title.save()
        return Response('Новость была создана')
    @action(methods=['GET'], detail=False,
            url_path='newsget')
    def news(self, request):
        news = request.news
        data = NewsSerializer(news).data
        return Response(data)



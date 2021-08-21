from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import CountriesSerializer, CitySerializer
from .models import Countrie

# Create your views here.

class CountriesView(APIView):
    '''
    This class will represent CRUD about api
    '''
    serializer_class = CountriesSerializer

    def get(self, request, format=None) -> Response:
        '''
        Method for get countries
        '''
        countries = Countrie.objects.all().values()            
        return Response({
            'status' : True, 
            'message': 'successful query',
            'data'   : countries
        })


    def post(self, request):
        '''
        Method for create new country
        '''
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            city = serializer.validated_data.get('city')
            state = serializer.validated_data.get('state')
            population = serializer.validated_data.get('population')
            Countrie.objects.create(name_countrie=name, city=city, state=state, population=population)
            return Response({'status': True, 'message': 'Item Created'})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    
    def put(self, request):
        '''
        Methos for modify a item
        '''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            id = serializer.validated_data.get('id')
            name = serializer.validated_data.get('name')
            city = serializer.validated_data.get('city')
            state = serializer.validated_data.get('state')
            population = serializer.validated_data.get('population')
            Countrie.objects.filter(id=id).update(name_countrie=name, city=city, state=state, population=population)
            return Response({'status': True, 'message': 'Item Updated'})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request):
        '''
        Method for delete
        '''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            id = serializer.validated_data.get('id')
            Countrie.objects.delete(id=id)
            return Response({'status': True, 'message': 'Item deleted'})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )


class CountriesFiltersCity(APIView):
    '''
    This class will represent filter per city
    '''

    serializer_class = CitySerializer

    def get(self, request) -> Response:
        '''
        Method for get countries
        '''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():    
            city = serializer.validated_data.get('city')
            countries = Countrie.objects.filter(city=city).values() 
            return Response({
                'status' : True, 
                'message': 'successful query',
                'data'   : countries
            })
        else:
            return Response(
                status = status.HTTP_400_BAD_REQUEST
            )
        

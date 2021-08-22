from rest_framework import serializers

class CountriesSerializer(serializers.Serializer):
    '''
    This class will serializae own petiton
    '''
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=60)
    city = serializers.CharField(max_length=60)
    state = serializers.CharField(max_length=60)
    population = serializers.IntegerField()


class StateSerializer(serializers.Serializer):
    '''
    This class will serializae own petiton
    '''
    state = serializers.CharField(max_length=60)


class CitySerializer(serializers.Serializer):
    '''
    This class will serializae own petiton
    '''
    city = serializers.CharField(max_length=60)

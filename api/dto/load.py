from rest_framework import serializers

from apps.load.models import (
    Load, LoadTags, Driver, DriverTags, Trailer, 
    TrailerTags, TruckTags, Truck, Dispatcher,
    DispatcherTags, EmployeeTags, CustomerBroker, 
    Stops, Employee, OtherPay, Commodities)

class LoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Load
        fields = "__all__"

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"

class TrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        fields = "__all__"

class TrailerTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrailerTags
        fields = "__all__"

class DriverTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverTags
        fields = "__all__"

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = "__all__"

class TruckTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckTags
        fields = "__all__"

class DispatcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatcher
        fields = "__all__"

class DispatcherTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatcherTags
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class EmployeeTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTags
        fields = "__all__"

class CustomerBrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerBroker
        fields = "__all__"
    
class LoadTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadTags
        fields = "__all__"

class StopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stops
        fields = "__all__"

class OtherPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherPay
        fields = "__all__"

class CommoditiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodities
        fields = "__all__"


        
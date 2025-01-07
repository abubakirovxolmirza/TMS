from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.load.models import Load, Driver, DriverTags, Trailer, TrailerTags, Truck, TruckTags, Dispatcher, DispatcherTags, Employee, EmployeeTags, CustomerBroker, Commodities, OtherPay, LoadTags, Stops
from api.dto.load import LoadSerializer, DriverSerializer, DriverTagsSerializer, TrailerSerializer, TrailerTagsSerializer, TruckSerializer, TruckTagsSerializer, DispatcherSerializer, DispatcherTagsSerializer, EmployeeSerializer, EmployeeTagsSerializer, CustomerBrokerSerializer, LoadTagsSerializer, StopsSerializer, OtherPaySerializer, CommoditiesSerializer
from rest_framework import generics
class LoadListView(APIView):
    def get(self, request):
        loads = Load.objects.all()
        serializer = LoadSerializer(loads, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LoadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer


class DriverListView(APIView):
    def get(self, request):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DriverDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class DriverTagsListView(APIView):
    def get(self, request):
        driver_tags = DriverTags.objects.all()
        serializer = DriverTagsSerializer(driver_tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = DriverTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DriverTagsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DriverTags.objects.all()
    serializer_class = DriverTagsSerializer

class TrailerListView(APIView):
    def get(self, request):
        trailers = Trailer.objects.all()
        serializer = TrailerSerializer(trailers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TrailerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TrailerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer

class TrailerTagsListView(APIView):
    def get(self, request):
        trailer_tags = TrailerTags.objects.all()
        serializer = TrailerTagsSerializer(trailer_tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TrailerTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TrailerTagsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrailerTags.objects.all()
    serializer_class = TrailerTagsSerializer

class TruckListView(APIView):
    def get(self, request):
        trucks = Truck.objects.all()
        serializer = TruckSerializer(trucks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TruckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TruckDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer

class TruckTagsListView(APIView):
    def get(self, request):
        truck_tags = TruckTags.objects.all()
        serializer = TruckTagsSerializer(truck_tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TruckTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TruckTagsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TruckTags.objects.all()
    serializer_class = TruckTagsSerializer

class DispatcherListView(APIView):
    def get(self, request):
        dispatchers = Dispatcher.objects.all()
        serializer = DispatcherSerializer(dispatchers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = DispatcherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DispatcherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dispatcher.objects.all()
    serializer_class = DispatcherSerializer

class DispatcherTagsListView(APIView):
    def get(self, request):
        dispatcher_tags = DispatcherTags.objects.all()
        serializer = DispatcherTagsSerializer(dispatcher_tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = DispatcherTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DispatcherTagsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DispatcherTags.objects.all()
    serializer_class = DispatcherTagsSerializer

class EmployeeListView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeTagsListView(APIView):
    def get(self, request):
        employee_tags = EmployeeTags.objects.all()
        serializer = EmployeeTagsSerializer(employee_tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmployeeTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeTagsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeTags.objects.all()
    serializer_class = EmployeeTagsSerializer
    
class CustomerBrokerListView(APIView):
    def get(self, request):
        custom_brokers = CustomerBroker.objects.all()
        serializer = CustomerBrokerSerializer(custom_brokers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CustomerBrokerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomerBrokerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerBroker.objects.all()
    serializer_class = CustomerBrokerSerializer

class CommoditiesListView(APIView):
    def get(self, request):
        commodities = Commodities.objects.all()
        serializer = CommoditiesSerializer(commodities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CommoditiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommoditiesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commodities.objects.all()
    serializer_class = CommoditiesSerializer

class OtherPayListView(APIView):
    def get(self, request):
        other_pays = OtherPay.objects.all()
        serializer = OtherPaySerializer(other_pays, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = OtherPaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OtherPayDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OtherPay.objects.all()
    serializer_class = OtherPaySerializer

class StopsListView(APIView):
    def get(self, request):
        stops = Stops.objects.all()
        serializer = StopsSerializer(stops, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StopsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StopsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stops.objects.all()
    serializer_class = StopsSerializer

class LoadTagsListView(APIView):
    def get(self, request):
        load_tags = LoadTags.objects.all()
        serializer = LoadTagsSerializer(load_tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = LoadTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoadTagsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoadTags.objects.all()
    serializer_class = LoadTagsSerializer



from django.contrib import admin
from apps.load.models import Load, Driver, DriverTags, Trailer, TrailerTags, TruckTags, Truck, Dispatcher, DispatcherTags, EmployeeTags, CustomerBroker, Stops, Employee, OtherPay
# Register your models here.
admin.site.register(Load)

admin.site.register(Driver)

admin.site.register(DriverTags)

admin.site.register(Trailer)

admin.site.register(TrailerTags)

admin.site.register(TruckTags)

admin.site.register(Truck)

admin.site.register(Dispatcher)

admin.site.register(DispatcherTags)

# admin.site.register(Employee)

admin.site.register(EmployeeTags)

admin.site.register(CustomerBroker)

admin.site.register(Stops)

admin.site.register(Employee)

admin.site.register(OtherPay)
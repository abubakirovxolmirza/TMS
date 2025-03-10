from django.contrib import admin

from apps.load.models import (
    Load, LoadTags, Driver, DriverTags, Trailer, 
    TrailerTags, TruckTags, Truck, Dispatcher,
    DispatcherTags, EmployeeTags, CustomerBroker, 
    Stops, Employee, OtherPay, Commodities)


admin.site.register(Load)

admin.site.register(LoadTags)

admin.site.register(Driver)

admin.site.register(DriverTags)

admin.site.register(Trailer)

admin.site.register(TrailerTags)

admin.site.register(TruckTags)

admin.site.register(Truck)

admin.site.register(Dispatcher)

admin.site.register(DispatcherTags)

admin.site.register(EmployeeTags)

admin.site.register(CustomerBroker)

admin.site.register(Stops)

admin.site.register(Employee)

admin.site.register(OtherPay)

admin.site.register(Commodities)
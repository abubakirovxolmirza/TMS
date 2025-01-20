from django.db import models

from .truck import Truck
from .trailer import Trailer
from .dispatcher import Dispatcher

class DriverTags(models.Model):
    tag = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.tag
    

class Driver(models.Model):

    EMPLOYMENT_STATUS_CHOICES = [
        ('ACTIVE (DF)', 'ACTIVE (DF)'),
        ('Terminate', 'Terminate'),
        ('Applicant', 'Applicant'),

    ]

    DRIVER_STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Home', 'Home'),
        ('In-Transit', 'In-Transit'),
        ('Inactive', 'Inactive'),
        ('Shop', 'Shop'),
        ('Rest', 'Rest'),
        ('Dispatched', 'Dispatched'),

    ]

    DL_CLASS_STATUS_CHOICES = [
        ('Unknown', 'Unknown'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('Other', 'Other'),
    ]

    DRIVER_TYPE_CHOICES = [
        ('COMPANY_DRIVER', 'Company_driver'),
        ('OWNER_OPERATOR', 'Owner_operator'),
        ('LEASE', 'Lease'),
        ('RENTAL', 'Rental'),
    ]

    TEAM_DRIVER_CHOICES = [
        ('DRIVER_2', 'Driver_2'),
        ('ASSIGNED_DISPATCHER', 'Assigned_dispatcher'),
        ('PERCENT_SALARY', 'Percent_salary'),
    ]
    STATE_CHOICES = [
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    ]
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    employment_status = models.CharField(max_length=50, choices=EMPLOYMENT_STATUS_CHOICES, blank=True, null=True)
    telegram_username = models.CharField(max_length=100, blank=True, null=True)
    driver_status = models.CharField(max_length=50, choices=DRIVER_STATUS_CHOICES, blank=True, null=True) #search
    company_name = models.CharField(max_length=100, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    driver_license_id = models.CharField(max_length=50, blank=True, null=True)
    dl_class = models.CharField(max_length=10, choices=DL_CLASS_STATUS_CHOICES, blank=True, null=True)
    driver_type = models.CharField(max_length=50, blank=True, null=True, choices=DRIVER_TYPE_CHOICES)
    driver_license_state = models.CharField(max_length=50, choices=STATE_CHOICES, blank=True, null=True)
    driver_license_expiration = models.DateField(blank=True, null=True)

    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, choices=STATE_CHOICES, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)

    assigned_truck = models.ForeignKey(Truck, related_name='TRUCK_DRIVERS', on_delete=models.CASCADE, blank=True, null=True)
    assigned_trailer = models.ForeignKey(Trailer,  related_name='TRailer_DRIVERS', on_delete=models.CASCADE, blank=True, null=True)
    assigned_dispatcher = models.ForeignKey(Dispatcher, related_name='dispatcher_drivers', on_delete=models.CASCADE, blank=True, null=True)
    other_id = models.CharField(max_length=100, blank=True, null=True)

    notes = models.TextField(blank=True, null=True)
    tariff = models.FloatField(blank=True, null=True)
    mc_number = models.CharField(max_length=50, blank=True, null=True)
    driver_tags = models.ForeignKey(DriverTags, related_name='drivertags', on_delete=models.CASCADE, blank=True, null=True)
    team_driver = models.CharField(max_length=50, choices=TEAM_DRIVER_CHOICES, blank=True, null=True)
    permile = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    payd = models.FloatField(blank=True, null=True)


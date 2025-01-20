from django.db import models

from .load import Load

class OtherPay(models.Model):
    PAY_CHOICES = [
        ('ACCESSORIALS', 'Accessorials'),
        ('PAYAMOUNT', 'PayAmount'),
        ('OTHERCHARGES', 'OtherCharges'),
        ('FUEL', 'Fuel'),
        ('BROKERFEE', 'BrokerFee'),
    ]

    TYPE_CHOICES = [
        ('DETENTION', 'Detention'),
        ('EMPTYMILES', 'EmptyMiles'),
        ('EXTRAMILES', 'ExtraMiles'),
        ('FLAT', 'Flat'),
        ('LAYOVER', 'Layover'),
        ('LINEHOUL', 'Linehoul'),
        ('FUELSURCHARGE', 'FuelSurcharge'),
        ('LUMPER', 'Lumper'),
        ('EXTRASTOP', 'ExtraStop'),
        ('TONU', 'TONU'),
        ('BONUS', 'Bonus'),
        ('OTHER', 'Other'),
    ]
    load = models.ForeignKey(Load, on_delete=models.CASCADE, related_name='otherpay', blank=True, null=True)
    pay = models.CharField(max_length=50, choices=PAY_CHOICES, blank=True, null=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)



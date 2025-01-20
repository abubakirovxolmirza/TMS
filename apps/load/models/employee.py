from django.db import models

class EmployeeTags(models.Model):
    tag = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.tag


class Employee(models.Model):

    EMPLOYMENT_STATUS_CHOICES = [
        ('ACTIVE (DF)', 'ACTIVE (DF)'),
        ('Terminate', 'Terminate'),
        ('Applicant', 'Applicant'),
    ]

    POSITION_CHOICES = [
        ('ACCOUNTING', 'Accounting'),
        ('FLEET MANAGMENT', 'Fleet Managment'),
        ('SAFETY', 'Safety'),
        ('HR', 'hr'),
        ('UPDATER', 'Updater'),
        ('ELD TEAM', 'ELD team'),
        ('OTHER', 'Other'),
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
    company_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    employee_tags = models.ForeignKey(EmployeeTags, related_name='employeetags', on_delete=models.CASCADE, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, blank=True, null=True)
    contact_number = models.CharField(max_length=50, blank=True, null=True)
    employee_status = models.CharField(max_length=50, choices=EMPLOYMENT_STATUS_CHOICES, blank=True, null=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=50, default='USA', blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=50, choices=STATE_CHOICES, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    note = models.CharField(max_length=50, blank=True, null=True)


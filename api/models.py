from django.db import models

# Create your models here.
# Company Api start here


class Company(models.Model):
    company_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    about = models.TextField()
    company_type = models.CharField(max_length=100,choices=(('IT','IT'),
                                                            ('None IT','None IT'),
                                                            ('Contact_no','Contact_no')
                                                            ))
    added_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Employee Api Here

class Employee(models.Model):
    emp_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    about = models.TextField()
    position = models.CharField(max_length=50 ,choices=(('Manager','Manager'),
                                    ('Softwere developer','SD'),
                                    ('Project Leader','Project Leader')
                                    ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name
from django.db import models
import re
# Create your models here.
class Employee(models.Model):
    @property
    def _advance_payment_calculate(self):
        sum_p = 0
        for n in re.findall(r'\([-+]\d+\)',self.advance_payment):
            sum_p += int(n[1:-1])

        return sum_p
    
    @property
    def _payment_calculate(self):
        sum_p = 0
        for n in re.findall(r'\([-+]\d+\)',self.advance_payment_check):
            sum_p += int(n[2:-1])

        return sum_p
    id = models.CharField(max_length=100, primary_key=True)
    full_name = models.CharField(max_length=150)
    car_number = models.CharField(max_length=150)
    
    paycheck = models.CharField(max_length=150)
    advance_payment = models.TextField(blank=True)
    advance_payment_check = models.TextField(blank=True)
    def __str__(self):
        return self.full_name


    
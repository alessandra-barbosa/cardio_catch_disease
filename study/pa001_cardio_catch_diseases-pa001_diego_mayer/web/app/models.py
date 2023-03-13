
from django.db import models


class Patients(models.Model):
    
    
    CHOLESTEROL = (
        (1, 1), 
        (2, 2), 
        (3, 3),
    )
    GLUCOSE = (
        (1, 1), 
        (2, 2), 
        (3, 3),
    )
    SMOKER = (
        (0, "No"), 
        (1, "YES"),
    )
    ALCOHOL = (
        (0, "NO"), 
        (1, "YES"),
    )
    ACTIVE = (
        (0, "Sedentary"), 
        (1, "Active Person"),
    )
    
    GENDER = (
        (0, 'Man'),
        (1, 'Woman'),
    )

    id = models.AutoField(auto_created=True, blank=True, null=False, primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=False)
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True, choices=GENDER)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    hight_pressure = models.IntegerField(blank=True, null=True, 
                                         help_text='Your Hight Blood Pressure like: 120')
    low_pressure = models.IntegerField(blank=True, null=True, 
                                         help_text='Your Low Blood Pressure like: 80')
    cholesterol = models.IntegerField(blank=True, null=True, choices=CHOLESTEROL)
    glucose = models.IntegerField(blank=True, null=True, choices=GLUCOSE)
    smoker = models.IntegerField(blank=True, null=True, choices=SMOKER)
    alcohol = models.IntegerField(blank=True, null=True, choices=ALCOHOL)
    active = models.IntegerField(blank=True, null=True, choices=ACTIVE)
    cardio = models.IntegerField(blank=True, null=True)

    def __str__(self):
        if self.cardio == 1:
            return self.name + " - " + " Teste - POSITIVO "
        else:
            return self.name + " - " + " Teste - NEGATIVO "
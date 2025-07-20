from django.db import models


class Main(models.Model):
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    hypertension = models.IntegerField()
    heart_disease = models.IntegerField()
    ever_married = models.BooleanField()
    work_type = models.CharField(max_length=50)
    residence_type = models.CharField(max_length=50)
    avg_glucose_level = models.FloatField()
    bmi = models.FloatField()
    smoking_status = models.CharField(max_length=20)
    stroke_prediction = models.FloatField()

    # def __str__(self):
    #     return f"{self.gender}, Age: {self.age}"

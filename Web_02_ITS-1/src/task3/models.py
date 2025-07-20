from django.db import models



# class Trials(models.Model):
#     trial_id = models.AutoField(primary_key=True)
#     trial_name = models.CharField(max_length=100, null=True, blank=True)
#     start_date = models.DateField(null=True, blank=True)
#     end_date = models.DateField(null=True, blank=True)
#     med = models.CharField(max_length=100, null=True, blank=True)

#     class Meta:
#         db_table = 'trials'
#         managed = False
    
#     def __str__(self):
#         return self.trial_name
    
# class Patients(models.Model):
#     patient_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100, null=True, blank=True)
#     age = models.IntegerField(null=True, blank=True)
#     gender = models.CharField(max_length=10, null=True, blank=True)
#     condition = models.CharField(max_length=100, null=True, blank=True)

#     class Meta:
#         db_table = 'patients'
#         managed = False

#     def __str__(self):
#         return self.patient_id
    
# class Measurements(models.Model):
#     measurement_id = models.AutoField(primary_key=True)
#     patient = models.ForeignKey('Patients', on_delete=models.SET_NULL, null=True, blank=True)
#     trial = models.ForeignKey('Trials', on_delete=models.SET_NULL, null=True, blank=True)
#     measurement_date = models.DateField(null=True, blank=True)
#     drug = models.CharField(max_length=100, null=True, blank=True)
#     condition_score = models.IntegerField(null=True, blank=True)

#     class Meta:
#         db_table = 'measurements'
#         managed = False

#     def __str__(self):
#         return str(self.measurement_id)
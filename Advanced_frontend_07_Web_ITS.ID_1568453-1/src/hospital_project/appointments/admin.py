from django.contrib import admin
from .models import Doctor, Patient, Room, Appointment, CustomUser

class AllFieldsAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]

admin.site.register(Doctor, AllFieldsAdmin)
admin.site.register(Patient, AllFieldsAdmin)
admin.site.register(Room, AllFieldsAdmin)
admin.site.register(Appointment, AllFieldsAdmin)
admin.site.register(CustomUser, AllFieldsAdmin)

from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Package)
admin.site.register(Participant)
admin.site.register(Review)
admin.site.register(ActivePackage)

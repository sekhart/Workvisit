from django.contrib import admin

# Register your models here.
from .models import Ibx, Cage, Cabinets, Visitors

admin.site.register(Ibx)
admin.site.register(Cage)
admin.site.register(Cabinets)
admin.site.register(Visitors)
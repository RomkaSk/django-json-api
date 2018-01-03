from django.contrib import admin
from .models import Entry
from dashboard.models import ExcelFile, Result, Algorithm

# Register your models here.
admin.site.register(Entry)
admin.site.register([ExcelFile, Result, Algorithm])

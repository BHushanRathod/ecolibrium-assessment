from django.contrib import admin
from task_based_app.models import TaskType, CountryList, DayOfWeek, ExecutionList

# Register your models here.
admin.site.register(TaskType)
admin.site.register(CountryList)
admin.site.register(DayOfWeek)
admin.site.register(ExecutionList)

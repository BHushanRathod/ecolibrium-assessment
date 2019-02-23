import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone


class TaskType(models.Model):
    id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)

    create_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Task Type'

    def __str__(self):
        return self.task_name


class CountryList(models.Model):
    id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=100)

    create_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Country List'

    def __str__(self):
        return self.country_name


class DayOfWeek(models.Model):
    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=100)

    create_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.day

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Days'


class ExecutionList(models.Model):
    id = models.AutoField(primary_key=True)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(CountryList, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    day_of_week = models.ForeignKey(DayOfWeek, on_delete=models.CASCADE, null=True, blank=True)

    create_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        if self.day_of_week:
            if str(self.day_of_week).lower() == str(
                    datetime.date.today().strftime("%A").lower()) and self.start_time < timezone.now() < self.end_time:
                return 'Status: True'
            else:
                start_dt = timezone.localtime(self.start_time).strftime("%Y-%m-%d %H:%M:%S")
                return 'Status: False | Next Execution at: %s %s' % (start_dt, self.day_of_week)
        else:
            if self.start_time < timezone.now() < self.end_time:
                return 'Status: True'
            else:
                start_dt = timezone.localtime(self.start_time).strftime("%Y-%m-%d %H:%M:%S")
                return 'Status: False | Next Execution at: %s ' % start_dt

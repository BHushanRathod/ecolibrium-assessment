import datetime

import nose.tools as nt
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from task_based_app.models import TaskType, CountryList, DayOfWeek, ExecutionList


class TaskTypeTestCheck(TestCase):
    def setUp(self):
        self.task_obj = TaskType.objects.create(id=1, task_name='Email')

    def tearDown(self):
        self.task_obj.delete()

    def test_task_created(self):
        nt.eq_(self.task_obj, TaskType.objects.get(task_name=self.task_obj))
        nt.assert_equal(self.task_obj.task_name, 'Email')
        nt.eq_(TaskType.objects.count(), 1)


class CountryListTestCheck(TestCase):
    def setUp(self):
        data = [CountryList(country_name='USA'), CountryList(country_name='India')]
        CountryList.objects.bulk_create(data)
        self.country_obj = CountryList.objects.all()

    def tearDown(self):
        self.country_obj.delete()

    @staticmethod
    def test_countries_created():
        nt.eq_(CountryList.objects.count(), 2)
        nt.eq_(list(CountryList.objects.filter(country_name='USA').values_list('country_name', flat=True)), ['USA'])


class DayofWeeksTestCases(TestCase):
    def setUp(self):
        data = [DayOfWeek(day='Monday'),
                DayOfWeek(day='Tuesday'),
                DayOfWeek(day='Wednesday'),
                DayOfWeek(day='Thursday'),
                DayOfWeek(day='Friday'),
                DayOfWeek(day='Saturday'),
                DayOfWeek(day='Sunday')]
        DayOfWeek.objects.bulk_create(data)
        self.days_obj = DayOfWeek.objects.all()

    def tearDown(self):
        self.days_obj.delete()

    def days_check_testlist(self):
        nt.eq_(self.days_obj.count(), 7)
        nt.eq_(list(self.days_obj.filter(day='Thursday').values_list('day', flat=True)), ['Thursday'])


class ExecutionTestCases(TestCase):
    def setUp(self):
        self.task_obj = TaskType.objects.create(id=1, task_name='Email')
        self.country_obj = CountryList.objects.create(country_name='USA')
        self.dayofweek = DayOfWeek.objects.create(day='Monday')
        self.user = User.objects.create(username='U1', first_name='U1')

        start_dt = timezone.now()
        end_dt = start_dt + datetime.timedelta(days=1)

        ExecutionList(task_type=self.task_obj,
                      user=self.user,
                      country=self.country_obj,
                      start_time=start_dt,
                      end_time=end_dt,
                      day_of_week=self.dayofweek).save()
        self.execution_obj = ExecutionList.objects.all()

    def tearDown(self):
        self.execution_obj.delete()

    def execution_test(self):
        nt.eq_(self.execution_obj.count(), 1)

from django.db import models

# Create your models here.
from auth_person.models import Person


class Task(models.Model):
    customerId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='TaskCustomer'
    )
    implementerId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='TaskImplementer'
    )
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=4000, null=True)
    priority = models.CharField(max_length=20)
    taskData = models.FileField(upload_to='files/file_work/work/%Y-%m-%d/', null=True, blank=True)
    payment = models.DecimalField(
        max_digits=19, decimal_places=10
    )
    startDate = models.DateTimeField()
    finishDate = models.DateTimeField()


class Event(models.Model):
    title = models.CharField(max_length=99)
    startDate = models.DateField()
    startTime = models.TimeField()
    duration = models.TimeField()
    finishDate = models.DateField()
    description = models.CharField(max_length=999)
    caster = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    location = models.CharField(max_length=99)
    img = models.ImageField(upload_to='files/event_img/event/%Y-%m-%d/')


class GoingEvent(models.Model):
    id_event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )
    id_person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )


from django.db import models
from yahoo_finance import Share
import logging


# Create your models here.

from django.db import models
from mysite.utils import data

DEFAULT_SUPER_ID = 1

class ShareModel(models.Model):
    name_ref = models.CharField(max_length=100)


    def get_feed(self):
        writer = data.WriterCSV(self.name_ref)
        yahoo_listener = Share(self.name_ref)
        yahoo_listener.refresh()
        writer.write(yahoo_listener.get_trade_datetime(), yahoo_listener.get_price())


    # def get_read(self):
    #     reader = data.ReaderCSV()
    #     return reader.read()


    def __str__(self):
        return str(self.name_ref)

    class Meta:
        ordering = ['name_ref']

class ViewModel(models.Model):
    name_ref = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name_ref)

    class Meta:
        ordering = ['name_ref']

class DataModel(models.Model):
    name_ref = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name_ref)

    class Meta:
        ordering = ['name_ref']

class ActionModel(models.Model):
    name_ref = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name_ref)

    class Meta:
        ordering = ['name_ref']

class SuperModel(models.Model):
    name_ref = models.CharField(max_length=100)
    view_ref = models.ManyToManyField(ViewModel)
    data_ref = models.ManyToManyField(DataModel)
    action_ref = models.ManyToManyField(ActionModel)
    peer_ref = models.ManyToManyField('self')

    def __str__(self):
        return str(self.name_ref)

    class Meta:
        ordering = ['name_ref']



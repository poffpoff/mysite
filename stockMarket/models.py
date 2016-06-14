from django.db import models
from yahoo_finance import Share
import logging


# Create your models here.

from django.db import models
from mysite.utils import data


class ShareModel(models.Model):
    name_ref = models.CharField(max_length=100)


    def get_feed(self):
        writer = data.WriterCSV(self.name_ref)
        yahoo_listener = Share(self.name_ref)
        yahoo_listener.refresh()
        writer.write(yahoo_listener.get_trade_datetime(), yahoo_listener.get_price())


    def get_read(self):
        reader = data.ReaderCSV(self.name_ref)
        return reader.read()


    def __str__(self):
        return str(self.name_ref)

    class Meta:
        ordering = ['name_ref']
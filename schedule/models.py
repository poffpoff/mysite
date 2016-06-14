# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import cities_light.models
from django.core.urlresolvers import reverse
from colorful.fields import RGBColorField

class MySpecialUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    city = models.ForeignKey(cities_light.models.City, default=0)
    color = RGBColorField()

class Calendar(models.Model):
    name = models.CharField(_('name'), max_length=50)
    slug = models.SlugField(_('slug'), unique=True)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _('calendar')
        ordering = ['name']


class Event(models.Model):
    title = models.CharField(_('title'), max_length=100)
    start = models.DateTimeField(_('start'))
    end = models.DateTimeField(_('end'))
    is_cancelled = models.BooleanField(_('Cancelled?'), default=False, blank=True)
    calendar = models.ForeignKey(Calendar)

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = _('event')
        ordering = ['start', 'end']




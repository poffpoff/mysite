from django.http import Http404, HttpResponse, HttpRequest
from chartit import DataPool, Chart
import datetime
from django.shortcuts import render_to_response
from stockMarket.models import ShareModel
from django.template import Template, Context
import random
from highcharts.views import HighChartsBarView, HighChartsLineView
import re

def hello(request):
    return HttpResponse("Hello world")

def root(request):
    return HttpResponse("Root world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset, onset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s, and %s.</body></html>" % (offset, dt, onset)
    return HttpResponse(html)

def share_chart_view(request):
    return render_to_response('sharechart.html')



class BarView(HighChartsLineView):
    categories = ['Orange', 'Bananas', 'Apples']

    @property
    def series(self):
        result = []
        for name in ('Joe', 'Jack', 'William', 'Averell'):
            data = []
            for x in range(len(self.categories)):
                data.append(random.randint(0, 10))
            result.append({'name': name, "data": data})
        return result


class LineView(HighChartsLineView):
    title = None
    subtitle = None
    tooltip_point_format = None
    plot_options = {}
    y_axis_title = ""


    share_model = ShareModel()
    # data_set = share_model.get_read()

    #categories = ['Orange', 'Bananas', 'Apples']

    @property
    def series(self):
        result = []
        for name in ('Joe', 'Jack', 'William', 'Averell'):
            data = []
            for x in range(40):
                data.append(random.randint(0, 10))
            result.append({'name': name, "data": data})
        return result
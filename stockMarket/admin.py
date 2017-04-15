from django.contrib import admin
from stockMarket.models import ShareModel, ActionModel, DataModel, SuperModel, ViewModel

admin.site.register(SuperModel)
admin.site.register(ShareModel)
admin.site.register(ActionModel)
admin.site.register(DataModel)
admin.site.register(ViewModel)

# Register your models here.

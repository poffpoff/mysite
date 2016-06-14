from django.forms import ModelForm
from schedule.models import MySpecialUser, Event
from colorful.widgets import ColorFieldWidget


class MySpecialUserForm(ModelForm):
    class Meta:
        model = MySpecialUser
        fields = '__all__'

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
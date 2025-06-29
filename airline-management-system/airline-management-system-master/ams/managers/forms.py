from django import forms
from airlines.models import Airport, Flight, Trip, AirplaneType

airport = Airport.objects.all().order_by('name')

airport_list = []

days = [
    ('sunday', 'Sunday'),
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday')
]

Days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


class SearchForm(forms.Form):
    from_airport = forms.ModelChoiceField(label="From Airport", queryset=Airport.objects.all(), to_field_name="name")
    to_airport = forms.ModelChoiceField(label="To Airport", queryset=Airport.objects.all(), to_field_name="name")
    # from_airport = forms.CharField(label='What is from airport?', widget=forms.Select(choices=airport_list))
    # to_airport = forms.CharField(label='What is to airport?', widget=forms.Select(choices=airport_list))
    day = forms.CharField(label='What is day?', widget=forms.Select(choices=days))


class SearchForm1(forms.Form):
    from_airport = forms.ModelChoiceField(label="From Airport", queryset=Airport.objects.all(), to_field_name="name")
    to_airport = forms.ModelChoiceField(label="To Airport", queryset=Airport.objects.all(), to_field_name="name")
    # from_airport = forms.CharField(label='What is from airport?', widget=forms.Select(choices=airport_list))
    # to_airport = forms.CharField(label='What is to airport?', widget=forms.Select(choices=airport_list))
    day = forms.CharField(label='What is day?', widget=forms.Select(choices=days))


class DateInput(forms.DateInput):
    input_type = 'date'


class SelectTypeForm(forms.Form):
    choice = forms.ModelChoiceField(label="Edit Type", queryset=AirplaneType.objects.all(), to_field_name="airplane_type")


class IntervalForm(forms.Form):
    from_date = forms.DateField(label="From Date", widget=DateInput)
    to_date = forms.DateField(label="To Date", widget=DateInput)


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['from_airport', 'to_airport', 'type', 'arrival_time', 'departure_time', 'day', 'distance']


class TypeForm(forms.ModelForm):
    class Meta:
        model = AirplaneType
        fields = ['cost_per_km', 'fare_per_km', 'basic_cost']
        # 'airplane_type','first_class', 'economy_class', 'business_class', 'count'
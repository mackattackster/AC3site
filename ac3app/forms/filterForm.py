from django import forms

'''
Currently the way that FilterForm is defined the fields for the form
will be initialized on a server start. So any changes to our choice
fields will not be displayed (ie if a user was added to the DB that
user will not show up until the server restarts). This can be fixed
by calling the def __init__ method of the parent class(Form).

class FilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.fields['user_field'] = forms.ChoiceField(choices=get_choices())

This will allow the form to be initialized each time the form is loaded.
Depending on how often it is called it may cause performance issues.
'''


class FilterForm(forms.Form):
    user_choices = forms.ChoiceField()
    date1 = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'datepicker'}
    ))
    date2 = forms.DateField(widge=forms.TextInput(
        attrs={'class': 'datepicker'}
    ))
    event_choices = forms.ChoiceField()
    sensor_choices = forms.ChoiceField()


def get_user_choices():
    #TODO Add logic for getting user choices
    return None


def get_sensor_choices():
    #TODO Add logic for getting sensor choices
    return None


def get_event_choices():
    #TODO Add logic for getting event choices
    return None
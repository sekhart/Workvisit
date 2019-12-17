from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Layout, Column, Submit, Fieldset
from django import forms

from WorkVisits import models

from WorkVisits.models import Ibx, Cage, Cabinets, Visitors, WorkVisit


class IbxForm(forms.ModelForm):
    class Meta:
        model = Ibx
        fields = ['ibx_name']
        labels = {'ibx_name': 'IBX'}


class CageForm(forms.ModelForm):
    class Meta:
        model = Cage
        fields = ['ibx_name', 'cage_name']
        labels = {'ibx_name': 'IBX', 'cage_name': 'Cage'}


class CabinetsForm(forms.ModelForm):
    class Meta:
        model = Cabinets
        fields = ['cage_name', 'cabinet_name']
        labels = {'cage_name': 'Cage', 'cabinet_name': 'Cabinet'}


class VisitorsForm(forms.ModelForm):
    class Meta:
        model = Visitors

        fields = ['visitor_fname', 'visitor_lname', 'visitor_uname', 'visitor_age', 'visitor_address',
                  'visitor_company', 'photo']
        labels = {'visitor_fname': 'First Name', 'visitor_lname': 'Last Name', 'visitor_uname': 'User Name',
                  'visitor_age': 'Age', 'visitor_address': 'Address', 'visitor_company': 'Company', 'photo': 'Picture'}

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)


class WorkVisitRequestForm(forms.Form):
    ibx = forms.ModelChoiceField(queryset=models.Ibx.objects.all())
    cage = forms.ModelChoiceField(queryset=models.Cage.objects.none())  # Need to populate this using jquery
    cabinet = forms.ModelChoiceField(queryset=models.Cabinets.objects.none())  # Need to populate this using jquery

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('IBX Information',
                     Row(
                         Column('ibx', css_class='form-group col-md-4 mb-0'),
                         Column('cage', css_class='form-group col-md-4 mb-0'),
                         Column('cabinet', css_class='form-group col-md-4 mb-0'),
                         css_class='form-row'
                     )),
            Fieldset('Visitor(s)',
                     Row(
                         Column('ibx', css_class='form-group col-md-8 mb-0'),

                         css_class='form-row'
                     )),
            Fieldset('Scheduling Details',
                     Row(
                         Column('ibx', css_class='form-group col-md-6 mb-0'),
                         Column('cage', css_class='form-group col-md-6 mb-0'),
                         css_class='form-row'
                     )),
            Submit('submit', 'Sign in')
        )



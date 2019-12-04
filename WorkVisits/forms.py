from django import forms

from WorkVisits.models import Ibx, Cage, Cabinets, Visitors


class IbxForm(forms.ModelForm):
    class Meta:
        model = Ibx
        fields = ['ibx_name']
        labels = {'ibx_name': ''}


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
        fields = ['visitor_fname', 'visitor_lname', 'visitor_uname', 'visitor_age', 'visitor_address', 'visitor_company']
        labels = {'visitor_fname': 'First Name', 'visitor_lname': 'Last Name', 'visitor_uname': 'User Name', 'visitor_age': 'Age', 'visitor_address': 'Address', 'visitor_company': 'Company'}

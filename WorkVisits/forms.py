from django import forms

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
        fields = ['visitor_fname', 'visitor_lname', 'visitor_uname', 'visitor_age', 'visitor_address', 'visitor_company']
        labels = {'visitor_fname': 'First Name', 'visitor_lname': 'Last Name', 'visitor_uname': 'User Name', 'visitor_age': 'Age', 'visitor_address': 'Address', 'visitor_company': 'Company'}


class WorkVisitRequestForm(forms.ModelForm):
    class Meta:
        model = WorkVisit
        fields = ['wv_ibx', 'wv_cage', 'wv_cabinet', 'wv_visitors', 'wv_start_date_time', 'wv_end_date_time']
        labels = {'wv_ibx': 'IBX', 'wv_cage': 'Cage', 'wv_cabinet': 'Cabinet', 'wv_visitors': 'Visitors', 'wv_start_date_time': 'Start Date Time',
                  'wv_end_date_time': 'End Date Time'}

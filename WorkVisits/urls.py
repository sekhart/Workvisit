from django.conf.urls import url
from . import views

app_name = 'WorkVisit'

urlpatterns = [
    url('^$', views.home, name='home'),
    url('^ibxview', views.ibxview, name='ibxview'),
    url('^cageview', views.cageview, name='cageview'),
    url('^cabinetview', views.cabinetview, name='cabinetview'),
    url('^visitorsview', views.visitorsview, name='visitorsview'),
    url('^new_ibx', views.new_ibx, name='new_ibx'),
    url('^new_cage', views.new_cage, name='new_cage'),
    url('^new_cabinet', views.new_cabinet, name='new_cabinet'),
    url('^new_visitor', views.new_visitor, name='new_visitor'),
    url('visitor_details/(?P<visitor_id>\d+)/$', views.visitor_details, name='visitor_details'),
]
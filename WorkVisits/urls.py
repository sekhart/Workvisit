from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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
    url('^workvisit_request', views.workvisit_request, name='workvisit_request'),
    url('get_cages/(?P<ibx_id>\d+)/$', views.get_cages, name='get_cages'),
    url('load-ccages/', views.load_cages, name='load_cages'),  # <-- this one here
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

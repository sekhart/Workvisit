import simplejson as simplejson
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from WorkVisits import models

from .forms import IbxForm, CageForm, CabinetsForm, VisitorsForm, WorkVisitRequestForm
from WorkVisits.models import Ibx, Cage, Cabinets, Visitors


def home(request):
    """Home page for WorkVisit app"""
    return render(request, 'WorkVisits/home.html')


@login_required
def ibxview(request):
    """view ibx """
    ibx = Ibx.objects.order_by('date_added')
    context = {'ibxs': ibx}
    return render(request, 'WorkVisits/ibxview.html', context)


@login_required
def cageview(request):
    """view cage """
    cage = Cage.objects.order_by('date_added')
    context = {'cages': cage}
    return render(request, 'WorkVisits/cageview.html', context)


@login_required
def cabinetview(request):
    """view cabinet """
    cabinet = Cabinets.objects.order_by('date_added')
    context = {'cabinets': cabinet}
    return render(request, 'WorkVisits/cabinetview.html', context)


@login_required
def visitorsview(request):
    """view visitors """
    visitors = Visitors.objects.order_by('date_added')
    context = {'visitors': visitors}
    return render(request, 'WorkVisits/visitorsview.html', context)


@login_required
def new_ibx(request):
    """add new ibx"""
    if request.method != 'POST':
        form = IbxForm()
    else:
        form = IbxForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('workvisits:ibxview'))
    context = {'form': form}
    return render(request, 'workvisits/new_ibx.html', context)


@login_required
def new_cage(request):
    """add new Cage"""
    if request.method != 'POST':
        form = CageForm()
    else:
        form = CageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('workvisits:cageview'))
    context = {'form': form}
    return render(request, 'workvisits/new_cage.html', context)


@login_required
def new_cabinet(request):
    """add new Cabinet"""
    if request.method != 'POST':
        form = CabinetsForm()
    else:
        form = CabinetsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('workvisits:cabinetview'))
    context = {'form': form}
    return render(request, 'workvisits/new_cabinet.html', context)


@login_required
def new_visitor(request):
    """add new Cabinet"""
    if request.method != 'POST':
        form = VisitorsForm()
    else:
        form = VisitorsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('workvisits:visitorsview'))
    context = {'form': form}
    return render(request, 'workvisits/new_visitor.html', context)


@login_required
def visitor_details(request, visitor_id):
    """display visitor details"""
    vd = Visitors.objects.get(id=visitor_id)
    context = {'vd': vd}
    return render(request, 'workvisits/visitor_details.html', context)


@login_required
def workvisit_request(request):
    """Add Work visitor entry"""
    if request.method != 'POST':
        form = WorkVisitRequestForm()
    else:
        form = WorkVisitRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('workvisits:home'))
    context = {'form': form}
    return render(request, 'workvisits/workvisit_request.html', context)


def get_cages(request, ibx_id):
    ibx = models.Ibx.objects.get(pk=ibx_id)
    cages = models.Cage.objects.filter(ibx_name=ibx)
    print('getting Cages----')
    cage_dict = {}
    for cage in cages:
        cage_dict[cage.id] = cage.cage_name
    print(cage_dict)
    return HttpResponse(simplejson.dumps(cage_dict))


def load_cages(request):
    ibx_id = request.GET.get('wv_ibx')
    cages = Cage.objects.filter(ibx_id=ibx_id).order_by('cage_name')
    print(cages)
    return render(request, 'workvisits/cage_dropdown_list_options.html', {'cages': cages})

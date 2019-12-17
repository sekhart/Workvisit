from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ibx(models.Model):
    """ibx model drop down to select"""
    ibx_name = models.CharField('IBX Name', max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ibx_name


class Cage(models.Model):
    """Cage to select drop down box"""
    ibx_name = models.ForeignKey(Ibx, on_delete=models.PROTECT)
    cage_name = models.CharField('Cage Name', max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'cages'

    def __str__(self):
        return self.cage_name[:250]


class Cabinets(models.Model):
    """cabinets to select drop down"""
    cage_name = models.ForeignKey(Cage, on_delete=models.PROTECT)
    cabinet_name = models.CharField('Cabinet Name', max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'cabinets'

    def __str__(self):
        return self.cabinet_name[:250]


class Visitors(models.Model):
    """visitors who visit the workvisit"""
    visitor_fname = models.CharField('first name', max_length=250)
    visitor_lname = models.CharField('last name', max_length=250)
    visitor_uname = models.CharField('user name', max_length=250)
    visitor_age = models.IntegerField('Age')
    visitor_address = models.CharField('Address', max_length=250)
    visitor_company = models.CharField('Company', max_length=250)
    photo = models.FileField(upload_to="gallery")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.visitor_fname[:250] + " "+self.visitor_lname[:250]


class WorkVisit(models.Model):
    """Request Workvisit who visit """
    wv_ibx = models.ForeignKey(Ibx, on_delete=models.CASCADE)
    wv_cage = models.ForeignKey(Cage, on_delete=models.CASCADE)
    wv_cabinet = models.ForeignKey(Cabinets, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.wv_ibx[:250] + " "+self.wv_cage[:250]

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Custom(models.Model):
    owner = models.ForeignKey(User, blank=False)
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    create_date = models.DateTimeField('Create Date', auto_now=True)

    class Meta:
        ordering = ('-create_date',)

    def __str__(self):
        return  self.name

class Pack1(models.Model):
    custom = models.ForeignKey(Custom, blank=False, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    p1 = models.CharField(max_length=100, blank=True)
    p2 = models.CharField(max_length=100, blank=True)
    p3 = models.CharField(max_length=100, blank=True)
    p4 = models.CharField(max_length=100, blank=True)
    p5 = models.CharField(max_length=100, blank=True)
    p6 = models.CharField(max_length=100, blank=True)
    p7 = models.CharField(max_length=100, blank=True)
    p8 = models.CharField(max_length=100, blank=True)
    p9 = models.CharField(max_length=100, blank=True)
    p10 = models.CharField(max_length=100, blank=True)
    p11 = models.CharField(max_length=100, blank=True)
    p12 = models.CharField(max_length=100, blank=True)
    p13 = models.CharField(max_length=100, blank=True)
    p14 = models.CharField(max_length=100, blank=True)
    p15 = models.CharField(max_length=100, blank=True)
    p16 = models.CharField(max_length=100, blank=True)
    p17 = models.CharField(max_length=100, blank=True)
    p18 = models.CharField(max_length=100, blank=True)
    p19 = models.CharField(max_length=100, blank=True)
    p20 = models.CharField(max_length=100, blank=True)
    p21 = models.CharField(max_length=100, blank=True)
    p22 = models.CharField(max_length=100, blank=True)
    create_date = models.DateTimeField('Create Date', auto_now=True)

    class Meta:
        ordering = ('-create_date',)

    def __str__(self):
        return self.title

class Pack2(models.Model):
    custom = models.ForeignKey(Custom, blank=False, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    p23 = models.CharField(max_length=100, blank=True)
    r23 = models.CharField(max_length=100, blank=True)
    p24 = models.CharField(max_length=100, blank=True)
    r24 = models.CharField(max_length=100, blank=True)
    p25 = models.CharField(max_length=100, blank=True)
    r25 = models.CharField(max_length=100, blank=True)
    p26 = models.CharField(max_length=100, blank=True)
    r26 = models.CharField(max_length=100, blank=True)
    p27 = models.CharField(max_length=100, blank=True)
    r27 = models.CharField(max_length=100, blank=True)
    p28 = models.CharField(max_length=100, blank=True)
    r28 = models.CharField(max_length=100, blank=True)
    p29 = models.CharField(max_length=100, blank=True)
    r29 = models.CharField(max_length=100, blank=True)
    p30 = models.CharField(max_length=100, blank=True)
    r30 = models.CharField(max_length=100, blank=True)
    p31 = models.CharField(max_length=100, blank=True)
    r31 = models.CharField(max_length=100, blank=True)
    p32 = models.CharField(max_length=100, blank=True)
    r32 = models.CharField(max_length=100, blank=True)
    p33 = models.CharField(max_length=100, blank=True)
    r33 = models.CharField(max_length=100, blank=True)
    p34 = models.CharField(max_length=100, blank=True)
    r34 = models.CharField(max_length=100, blank=True)
    p35 = models.CharField(max_length=100, blank=True)
    r35 = models.CharField(max_length=100, blank=True)
    p36 = models.CharField(max_length=100, blank=True)
    r36 = models.CharField(max_length=100, blank=True)
    create_date = models.DateTimeField('Create Date', auto_now=True)

    class Meta:
        ordering = ('-create_date',)

    def __str__(self):
        return self.title


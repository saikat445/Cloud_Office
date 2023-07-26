from django.db import models
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import datetime,date
# Create your models here.

class trialdata(models.Model):
 setno = models.CharField(max_length=5)
 trialdate = models.DateField(null=True)
 batterytype = models.CharField(max_length=9)
 trial_location = models.CharField(max_length=9)
 description = models.CharField(max_length=25)
 receivedate = models.DateTimeField(null=True)

 def __str__(self):
   return self.setno

class marketsample(models.Model):
 batterytype = models.CharField(max_length=5)
 name = models.CharField(max_length=9)
 description = models.CharField(max_length=99)
 mfg = models.CharField(max_length=9)
 price = models.IntegerField()
 shelflife = models.CharField(max_length=9)
 receivedate = models.DateField(auto_now_add=True,null=True)

 def __str__(self):
  return self.name

class market_image(models.Model):
 name = models.CharField(max_length=50)
 Mfg = models.CharField(max_length=50)
 market_sample_img = models.ImageField(upload_to='static/')
 receivedate = models.DateTimeField(default=timezone.now)

 def __str__(self):
  return self.name

class complaint(models.Model):
 complaint_no = models.CharField(max_length=5)
 complainer = models.CharField(max_length=25)
 battery_type = models.CharField(max_length=9)
 description = models.CharField(max_length=99)
 mfg = models.CharField(max_length=9)
 status = models.CharField(max_length=99)
 receivedate = models.DateField(null=True)

 def __str__(self):
  return self.complaint_no

class testsample(models.Model):
 receivedno = models.CharField(max_length=5)
 samplename = models.CharField(max_length=99)
 description = models.CharField(max_length=99)
 mfg = models.CharField(max_length=9)
 teststatus = models.CharField(max_length=20)
 receivedate = models.DateField(null=True)

 def __str__(self):
  return self.receivedno

class test_image(models.Model):
 receivedno = models.CharField(max_length=50)
 samplename = models.CharField(max_length=50)
 receivedfrom = models.CharField(max_length=50)
 Mfg = models.CharField(max_length=50)
 test_sample_img = models.ImageField(upload_to='static/')
 receivedate = models.DateTimeField(default=timezone.now)

 def __str__(self):
  return self.samplename


class accounts(models.Model):
 po_no = models.CharField(max_length=5)
 date = models.CharField(max_length=9)
 suppliername = models.CharField(max_length=99)
 amount = models.CharField(max_length=9)
 description = models.CharField(max_length=200)

 def __str__(self):
  return self.po_no

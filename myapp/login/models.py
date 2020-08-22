from django.db import models

# Create your models here.
class Destination(models.Model):

    name = models.CharField(max_length=100)
    pw = models.CharField(max_length=20)

class mlmodel(models.Model):

    USERID_x = models.IntegerField()
    DayDiff = models.FloatField()
    DayDiff1 = models.FloatField()
    DayDiff2 = models.FloatField()
    DayDiffMean = models.FloatField()
    DayDiffStd = models.FloatField()
    NextPurchaseDayRange = models.FloatField()

class mlmodel1(models.Model):

    userid = models.IntegerField()
    date = models.IntegerField()
    rqid = models.IntegerField()
    pth = models.IntegerField()
    values = models.IntegerField()

class mlmodel2(models.Model):

    userid = models.IntegerField()
    date = models.IntegerField()
    rqid = models.IntegerField()
    pth_count = models.IntegerField()




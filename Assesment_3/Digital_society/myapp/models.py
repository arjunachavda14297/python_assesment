from django.db import models
from django.utils import timezone
# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    usertype=models.CharField(max_length=100,default='user')
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    mobile=models.PositiveBigIntegerField()
    email=models.EmailField()
    profile_pic=models.ImageField(upload_to='profile_pic/')
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.fname+" "+self.lname+" - "+str(self.mobile)

class Society_Member(models.Model):
    member_type=models.CharField(max_length=100,default='house_owner')
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    mobile=models.PositiveBigIntegerField()
    email=models.EmailField()
    block=models.CharField(max_length=50)
    house=models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to='profile_pic/')
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.fname+" "+self.lname+" - "+self.block+" / "+self.house
        
class Event(models.Model):
    user=models.ForeignKey(Society_Member,on_delete=models.CASCADE)
    event_name=models.CharField(max_length=100)
    location=models.TextField()
    date=models.DateTimeField()

    def __str__(self):
        return self.user.fname+" "+self.user.lname

class Notice(models.Model):
    notice=models.CharField(max_length=300)
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.notice

class Special_Team(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    mobile=models.PositiveBigIntegerField()
    email=models.EmailField()
    profile_pic=models.ImageField(upload_to='profile_pic/')
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.fname+" - "+self.post

class Visitors(models.Model):
    member=models.ForeignKey(Society_Member,on_delete=models.CASCADE)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    person=models.PositiveIntegerField()
    mobile=models.PositiveBigIntegerField()
    vehicle_no=models.CharField(max_length=100,default=None)
    datetime=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.fname+" "+self.lname+" / House Owner :"+self.member.fname+" "+self.member.lname
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

user = settings.AUTH_USER_MODEL

class CaseDetail(models.Model):
    user = models.ForeignKey(user, default = 1 ,null=True, on_delete=models.SET_NULL)
    case_name = models.CharField(default='Unknown' ,max_length=150 , null = True , blank = True)
    case_number = models.CharField(default='Unknown' , max_length=10 , null=True , blank=True)
    case_address = models.TextField(default='Unknown' ,null = True , blank = True)
    case_last_seen = models.TextField(default='Unknown' ,null = True , blank = True)
    case_image = models.ImageField(upload_to='cases_pics',default='default.jpeg')
    case_last_seen_date = models.DateTimeField(auto_now=False, auto_now_add = False, null=True , blank=True)
    time_entered = models.DateTimeField(auto_now_add=True)
    date_entered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.case_name

    def get_absolute_url(self):
        return reverse('home')

    class Meta :
        ordering=['-date_entered','-time_entered']

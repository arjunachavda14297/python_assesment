from django.contrib import admin
from .models import Contact,User,Event,Notice,Special_Team,Society_Member,Visitors

# Register your models here.
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Notice)
admin.site.register(Special_Team)
admin.site.register(Society_Member)
admin.site.register(Visitors)
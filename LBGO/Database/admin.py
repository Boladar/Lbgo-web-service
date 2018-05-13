from django.contrib import admin

from Database.models import Question,Objective,Team,Event
# Register your models here.
admin.site.register(Question)
admin.site.register(Objective)
admin.site.register(Team)
admin.site.register(Event)
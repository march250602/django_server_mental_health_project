from django.contrib import admin
from .models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name']

admin.site.register(User,UserAdmin)

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'Question_1', 'Question_2', 'Question_3')
    ordering = ['id']
admin.site.register(Survey,SurveyAdmin)

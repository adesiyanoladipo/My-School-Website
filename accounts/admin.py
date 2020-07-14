from django.contrib import admin
from home.models import Contact, Profile, Result

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['name', 'Class', 'Class_teacher']
	list_filter = ['name', 'Class', 'Class_teacher']

class ResultAdmin(admin.ModelAdmin):
	search_fields = ('name', 'Class')
	list_display = ['name', 'Class']

admin.site.register(Contact)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.site_header = 'Messiah High School'



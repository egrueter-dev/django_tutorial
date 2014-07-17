from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 4


class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				 {'fields': ['question']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
		]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['question']



admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)

# Register your models here.
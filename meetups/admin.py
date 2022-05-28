from django.contrib import admin
from .models import Meetup , Location, Participants


#control how your meetup lists are displayed
class MeetUpAdmin(admin.ModelAdmin):
    list_display = ('title','slug','date' )
    list_filter = ('date','location')
    #to prepopulate a field using some values
    prepopulated_fields = {
        'slug' : ('title',)
    }
admin.site.register(Meetup, MeetUpAdmin)
admin.site.register(Location)
admin.site.register(Participants)

# Register your models here.

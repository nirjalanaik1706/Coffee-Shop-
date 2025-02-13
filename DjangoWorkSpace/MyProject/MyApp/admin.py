from django.contrib import admin
from MyApp.models import Contact, Signup, Schedule

# Contact Model Admin
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']

admin.site.register(Contact, ContactAdmin)
 # Add filter for location



admin.site.register(Signup)
admin.site.register(Schedule)

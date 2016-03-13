from django.contrib import admin
from academy.models import Invite

# Here's how to tell the admin how to display - look at Django admin docs
class InviteAdmin(admin.ModelAdmin):
	list_display = ("name", "branch", "gender", "date_of_birth", "race")
	list_filter = ("branch", "gender", "race")
	search_fields = ("name",) # needs that comma at the end for a search field with only one item







# Register your models here.
admin.site.register(Invite, InviteAdmin)
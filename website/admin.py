from django.contrib import admin
from website.models import Goal, Link, Mentorship
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User



class GoalAdmin(admin.ModelAdmin):
    list_display=('user','name','progress','created','modified')

class LinkAdmin(admin.ModelAdmin):
    list_display=('goal','sender','recipient','link','clicked','learned','completed','modified')

class MentorshipAdmin(admin.ModelAdmin):
    list_display=('mentor','mentee','created','modified')

admin.site.unregister(User)

UserAdmin.list_display = ('id','username','email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')

admin.site.register(User, UserAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Mentorship, MentorshipAdmin)

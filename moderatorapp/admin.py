from django.contrib import admin

from moderatorapp.models import ModUser, Forum, MyRating, Comment, Post

'''
class ModUserAdmin(admin.ModelAdmin):
    list_display = ('user__last_name', 'user__first_name', 'job', 'user__email')
    list_filter = ('user__last_name', 'user__first_name', 'job', 'user__email')
'''

admin.site.register(ModUser)
admin.site.register(Forum)
admin.site.register(MyRating)
admin.site.register(Comment)
admin.site.register(Post)
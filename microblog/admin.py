from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from microblog.models import Profile, Post

class ProfileAdmin(AdminImageMixin, admin.ModelAdmin):
	filter_horizontal = ('following',)
	list_display = ('user', 'bio', 'pic',)

class PostAdmin(admin.ModelAdmin):
	list_display = ('profile', 'message', 'pub_date',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)

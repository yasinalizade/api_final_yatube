from django.contrib import admin

from .models import Comment, Follow, Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
        'image',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug',
        'description'
    )
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'post',
        'author',
        'created'
    )
    search_fields = ('text',)
    list_filter = ('created',)


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'following',
        'user',
    )


admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)

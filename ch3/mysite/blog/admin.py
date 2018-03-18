from django.contrib import admin
from .models import Post, Comment

# Register your models here.
# 重定向admin的显示
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',
                    'status')
    list_filter = ('status', 'created', 'publish', 'author') # 右侧边
    search_fields = ('title', 'body')  #搜索序列
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

# 注册站点



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)

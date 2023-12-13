from django.contrib import admin
from .models import Taxonomy, PostAuthor, Like, Bookmark, PostData, CustomUser

admin.site.register(Taxonomy)
admin.site.register(PostAuthor)
admin.site.register(Like)
admin.site.register(Bookmark)
admin.site.register(PostData)
admin.site.register(CustomUser)




# @admin.register(PostData)
# class PostDataAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'date', 'postType', 'commentCount', 'viewdCount')
#     search_fields = ('title', )
#     list_filter = ('postType',)


# @admin.register(PostData)
# class PostDataAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'date', 'postType', 'author', 'commentCount', 'viewdCount')
#     search_fields = ('title', 'author__firstName', 'author__lastName')
#     list_filter = ('postType', 'author', 'categories')

# @admin.register(PostData)
# class PostDataAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'date', 'postType', 'get_author_display', 'commentCount', 'viewdCount')
#     search_fields = ('title', 'author__firstName', 'author__lastName')
#     list_filter = ('postType', 'authorId__displayName', 'categories__name')

#     def get_author_display(self, obj):
#         return f"{obj.author.firstName} {obj.author.lastName}"
#     get_author_display.short_description = 'Author'
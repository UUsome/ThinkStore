from django.contrib import admin
from .models import CaseType, CaseTitle, CaseContent, CaseIdeaTitle, CaseIdeaContent


# # Register your models here.
@admin.register(CaseType)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(CaseTitle)
class CaseTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'caseType', 'title', 'user',)


@admin.register(CaseContent)
class CaseContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'Contents', 'parentId',)


@admin.register(CaseIdeaTitle)
class CaseIdeaTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'caseTitle', 'title',)


@admin.register(CaseIdeaContent)
class CaseIdeaContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'contents',)


# class SignedInfoAdmin(admin.ModelAdmin):
#     # 要列出的字段
#     list_display = ('id', 'user', 'status', 'date', 'signed_day', 'add_time',)
#     # 可以搜索的字段
#     search_fields = ('user', 'date',)
#     # 列出可以编辑的字段
#     list_editable = ('status', 'signed_day',)
#     # 根据某个字段排序
#     ordering = ('id',)
#     # 分页，每页显示多少条
#     list_per_page = 30

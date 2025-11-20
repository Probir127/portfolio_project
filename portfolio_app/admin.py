from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']
    search_fields = ['name', 'title']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['profile', 'email', 'phone', 'location']
    search_fields = ['email', 'phone']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'years', 'profile']
    list_filter = ['company', 'profile']
    search_fields = ['title', 'company']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'school', 'years', 'profile']
    list_filter = ['school', 'profile']
    search_fields = ['degree', 'school']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'profile']
    list_filter = ['profile']
    search_fields = ['name']

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['lang', 'level', 'profile']
    list_filter = ['level', 'profile']
    search_fields = ['lang']

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ['name', 'profile']
    list_filter = ['profile']
    search_fields = ['name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technologies', 'profile', 'live_link', 'github_link']
    list_filter = ['profile', 'technologies']
    search_fields = ['title', 'description', 'technologies']
    fieldsets = (
        ('Basic Information', {
            'fields': ('profile', 'title', 'description', 'technologies')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Links', {
            'fields': ('live_link', 'github_link')
        }),
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'get_category_display_name', 'profile']
    list_filter = ['category', 'profile']
    search_fields = ['name']
    ordering = ['category', 'name']
    
    def get_category_display_name(self, obj):
        return obj.get_category_display()
    get_category_display_name.short_description = 'Category Display'
    
    fieldsets = (
        ('Skill Information', {
            'fields': ('profile', 'name', 'category'),
            'description': 'Add your skills here. Categories: Language (Python, JS), Backend (FastAPI, Django), Frontend (HTML, CSS), Database (MySQL, SQLite), Tools (Git, Linux), Concepts (OOP, REST API)'
        }),
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    
    def has_add_permission(self, request):
        # Prevent manual addition of contact messages
        return False
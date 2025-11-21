from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Custom Admin Site Configuration
admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Management"
admin.site.index_title = "Manage Your Portfolio"


class ContactInline(admin.StackedInline):
    model = Contact
    can_delete = False
    verbose_name = "Contact Information"
    verbose_name_plural = "Contact Information"


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1
    fields = ['title', 'company', 'years', 'points']


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1


class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1


class LanguageInline(admin.TabularInline):
    model = Language
    extra = 1


class InterestInline(admin.TabularInline):
    model = Interest
    extra = 1


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 3
    fields = ['name', 'category']


class ProjectInline(admin.StackedInline):
    model = Project
    extra = 1
    fields = ['title', 'description', 'technologies', 'image', 'live_link', 'github_link']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'profile_image_preview']
    search_fields = ['name', 'title']
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'title', 'profile_pic'),
            'description': 'Your name and professional title'
        }),
        ('Professional Summary', {
            'fields': ('summary',),
            'description': 'Write a compelling summary about yourself'
        }),
    )
    inlines = [
        ContactInline,
        ExperienceInline,
        EducationInline,
        SkillInline,
        ProjectInline,
        CertificationInline,
        LanguageInline,
        InterestInline,
    ]
    
    def profile_image_preview(self, obj):
        if obj.profile_pic:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 50%; object-fit: cover;"/>',
                obj.profile_pic.url
            )
        return "No image"
    profile_image_preview.short_description = "Photo"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technologies', 'project_image_preview', 'has_live_link', 'has_github']
    list_filter = ['profile', 'technologies']
    search_fields = ['title', 'description', 'technologies']
    list_editable = []
    fieldsets = (
        ('Project Details', {
            'fields': ('profile', 'title', 'description', 'technologies')
        }),
        ('Media', {
            'fields': ('image',),
            'description': 'Upload a screenshot or preview image'
        }),
        ('Links', {
            'fields': ('live_link', 'github_link'),
            'description': 'Add links to live demo and source code'
        }),
    )
    
    def project_image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" height="50" style="object-fit: cover; border-radius: 4px;"/>',
                obj.image.url
            )
        return "No image"
    project_image_preview.short_description = "Preview"
    
    def has_live_link(self, obj):
        return bool(obj.live_link)
    has_live_link.boolean = True
    has_live_link.short_description = "Live"
    
    def has_github(self, obj):
        return bool(obj.github_link)
    has_github.boolean = True
    has_github.short_description = "GitHub"


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'get_category_display_name', 'profile']
    list_filter = ['category', 'profile']
    search_fields = ['name']
    ordering = ['category', 'name']
    list_per_page = 25
    
    def get_category_display_name(self, obj):
        return obj.get_category_display()
    get_category_display_name.short_description = 'Category Name'
    
    fieldsets = (
        ('Skill Information', {
            'fields': ('profile', 'name', 'category'),
            'description': '''
            Categories:
            • Language: Python, JavaScript, etc.
            • Backend: FastAPI, Django, Flask
            • Frontend: HTML, CSS, React
            • Database: MySQL, PostgreSQL, SQLite
            • Tools: Git, Docker, Linux
            • Concepts: OOP, REST API, DSA
            '''
        }),
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'years', 'profile']
    list_filter = ['company', 'profile']
    search_fields = ['title', 'company']
    fieldsets = (
        ('Job Details', {
            'fields': ('profile', 'title', 'company', 'years')
        }),
        ('Responsibilities', {
            'fields': ('points',),
            'description': 'Enter each point on a new line'
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'school', 'years', 'profile']
    list_filter = ['school', 'profile']
    search_fields = ['degree', 'school']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'short_message', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'message', 'created_at']
    date_hierarchy = 'created_at'
    
    def short_message(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    short_message.short_description = "Message Preview"
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False


# Unregister individual models that are managed via inlines
# (Keep them registered for direct access too)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['profile', 'email', 'phone', 'location']
    search_fields = ['email', 'phone']


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

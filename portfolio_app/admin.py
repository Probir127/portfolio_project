from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Custom Admin Site Configuration
admin.site.site_header = "Probir's Portfolio Admin"
admin.site.site_title = "Portfolio Management"
admin.site.index_title = "Manage Your Portfolio Content"


class ContactInline(admin.StackedInline):
    model = Contact
    can_delete = False
    verbose_name = "Contact Information"
    verbose_name_plural = "Contact Information"
    fields = ['phone', 'email', 'location', 'linkedin_url', 'github_url']


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1
    fields = ['title', 'company', 'years', 'is_current', 'points']


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1
    fields = ['degree', 'school', 'years', 'status']


class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1
    fields = ['name', 'issuer', 'year']


class LanguageInline(admin.TabularInline):
    model = Language
    extra = 1
    fields = ['lang', 'level']


class InterestInline(admin.TabularInline):
    model = Interest
    extra = 1
    fields = ['name', 'icon']


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 3
    fields = ['name', 'category']


class ProjectInline(admin.StackedInline):
    model = Project
    extra = 1
    fields = ['title', 'description', 'technologies', 'image', 'live_link', 'github_link', 'featured', 'order']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'profile_image_preview', 'has_contact']
    search_fields = ['name', 'title']
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'title', 'profile_pic'),
            'description': 'Your name and professional title'
        }),
        ('Professional Summary', {
            'fields': ('summary',),
            'description': 'Write a compelling summary about yourself (this appears in the About section)'
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
    
    def has_contact(self, obj):
        try:
            return bool(obj.contact)
        except:
            return False
    has_contact.boolean = True
    has_contact.short_description = "Contact Info"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technologies', 'featured', 'order', 'project_image_preview', 'has_live_link', 'has_github']
    list_filter = ['profile', 'featured']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['featured', 'order']
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
        ('Display Options', {
            'fields': ('featured', 'order'),
            'description': 'Control how this project appears on your portfolio'
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
    list_display = ['title', 'company', 'years', 'is_current', 'profile']
    list_filter = ['company', 'is_current', 'profile']
    search_fields = ['title', 'company']
    list_editable = ['is_current']
    fieldsets = (
        ('Job Details', {
            'fields': ('profile', 'title', 'company', 'years', 'is_current')
        }),
        ('Responsibilities', {
            'fields': ('points',),
            'description': 'Enter each point on a new line'
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'school', 'years', 'status', 'profile']
    list_filter = ['school', 'status', 'profile']
    search_fields = ['degree', 'school']
    list_editable = ['status']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'short_message', 'is_read', 'created_at']
    list_filter = ['created_at', 'is_read']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'message', 'created_at']
    date_hierarchy = 'created_at'
    list_editable = ['is_read']
    
    def short_message(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    short_message.short_description = "Message Preview"
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return True  # Allow marking as read


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['profile', 'email', 'phone', 'location', 'has_linkedin', 'has_github']
    search_fields = ['email', 'phone', 'location']
    
    def has_linkedin(self, obj):
        return bool(obj.linkedin_url)
    has_linkedin.boolean = True
    has_linkedin.short_description = "LinkedIn"
    
    def has_github(self, obj):
        return bool(obj.github_url)
    has_github.boolean = True
    has_github.short_description = "GitHub"


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuer', 'year', 'profile']
    list_filter = ['profile', 'year']
    search_fields = ['name', 'issuer']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['lang', 'level', 'profile']
    list_filter = ['level', 'profile']
    search_fields = ['lang']


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'profile']
    list_filter = ['profile']
    search_fields = ['name']
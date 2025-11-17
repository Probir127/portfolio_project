from django.db import models

# Model for managing your projects dynamically
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300)
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    live_link = models.URLField(max_length=200, null=True, blank=True)
    github_link = models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.title

# Model for managing your skills
class Skill(models.Model):
    name = models.CharField(max_length=100)
    
    # ➡️ UPDATED TO USE CHOICES FOR BETTER ADMIN/GROUPING
    CATEGORY_CHOICES = [
        ('Language', 'Programming Languages'),
        ('Backend', 'Backend Frameworks/Libraries'),
        ('Frontend', 'Frontend Development/UI'),
        ('Database', 'Databases & ORMs'),
        ('Tools', 'Tools, DevOps & OS'),
        ('Concepts', 'Core Concepts'),
    ]
    
    category = models.CharField(
        max_length=10, 
        choices=CATEGORY_CHOICES,
        default='Language',
        help_text="Select the category this skill belongs to."
    )
    
    class Meta:
        verbose_name_plural = "Skills"
        ordering = ['category', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
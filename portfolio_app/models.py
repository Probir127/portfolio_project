from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    def __str__(self):
        return f"Contact for {self.profile.name}"

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    years = models.CharField(max_length=50)
    points = models.TextField(help_text="Points separated by newlines")
    is_current = models.BooleanField(default=False, help_text="Check if this is your current position")

    class Meta:
        ordering = ['-is_current', '-id']

    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    years = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20,
        choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')],
        default='Completed'
    )

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.degree

class Certification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200, blank=True, help_text="Organization that issued the certification")
    year = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='languages')
    lang = models.CharField(max_length=50)
    level = models.CharField(max_length=50)

    class Meta:
        ordering = ['lang']

    def __str__(self):
        return f"{self.lang} ({self.level})"

class Interest(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='interests')
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True, help_text="Optional: emoji or icon")

    def __str__(self):
        return self.name

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300)
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    live_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False, help_text="Display as featured project")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")

    class Meta:
        ordering = ['-featured', 'order', '-id']

    def __str__(self):
        return self.title

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills', null=True, blank=True)
    name = models.CharField(max_length=100)
    CATEGORY_CHOICES = [
        ('Language', 'Programming Languages'),
        ('Backend', 'Backend Frameworks/Libraries'),
        ('Frontend', 'Frontend Development/UI'),
        ('Database', 'Databases & ORMs'),
        ('Tools', 'Tools, DevOps & OS'),
        ('Concepts', 'Core Concepts'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='Language')

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.created_at.strftime('%Y-%m-%d')}"
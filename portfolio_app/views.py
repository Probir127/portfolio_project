from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Project, Skill
from .forms import ContactForm

def home_view(request):
    """
    Main portfolio page view with all sections.
    """
    try:
        profile = Profile.objects.first()
    except Exception as e:
        profile = None
    
    if not profile:
        context = {
            'name': 'Your Name',
            'title': 'Add Your Profile in Admin Panel',
            'profile_pic': None,
            'contact': None,
            'summary': 'Please go to /admin/ to add your profile information.',
            'skills_data': {},
            'experience': [],
            'projects': [],
            'education': [],
            'certifications': [],
            'languages': [],
            'interests': [],
        }
        return render(request, 'portfolio_app/home.html', context)
    
    # Get contact information
    try:
        contact = profile.contact
    except:
        contact = None
    
    # Group skills by category
    skills_by_category = {}
    for skill in profile.skills.all():
        category_display = skill.get_category_display()
        if category_display not in skills_by_category:
            skills_by_category[category_display] = []
        skills_by_category[category_display].append(skill.name)
    
    # Order categories
    category_order = [
        'Programming Languages',
        'Backend Frameworks/Libraries',
        'Frontend Development/UI',
        'Databases & ORMs',
        'Tools, DevOps & OS',
        'Core Concepts',
    ]
    
    ordered_skills = {}
    for category in category_order:
        if category in skills_by_category:
            ordered_skills[category] = sorted(skills_by_category[category])
    
    for category, skills in sorted(skills_by_category.items()):
        if category not in ordered_skills:
            ordered_skills[category] = sorted(skills)
    
    # Build experience list with enhanced data
    experience_list = []
    for exp in profile.experiences.all():
        experience_list.append({
            'title': exp.title,
            'company': exp.company,
            'years': exp.years,
            'is_current': exp.is_current,
            'points': [point.strip() for point in exp.points.split('\n') if point.strip()],
        })
    
    # Get certifications with full details
    certifications = profile.certifications.all()
    
    # Handle project search/filter
    search_query = request.GET.get('q', '').strip()
    projects = profile.projects.all()
    if search_query:
        projects = projects.filter(technologies__icontains=search_query)
    
    # Handle profile picture
    profile_pic_url = None
    if profile.profile_pic:
        try:
            profile_pic_url = profile.profile_pic.url
        except:
            profile_pic_url = None
    
    # Build context
    context = {
        'profile': profile,
        'name': profile.name,
        'title': profile.title,
        'profile_pic': profile_pic_url,
        'contact': contact,
        'summary': profile.summary,
        'skills_data': ordered_skills,
        'experience': experience_list,
        'projects': projects,
        'education': profile.educations.all(),
        'certifications': certifications,
        'languages': profile.languages.all(),
        'interests': [interest.name for interest in profile.interests.all()],
    }
    
    return render(request, 'portfolio_app/home.html', context)


def contact_view(request):
    """
    Contact form page view.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Thank you! Your message has been sent successfully.')
            return redirect('home')
        else:
            messages.error(request, '❌ Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'portfolio_app/contact.html', {'form': form})
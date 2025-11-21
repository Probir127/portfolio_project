# ==================================
# SOLUTION: Use Static Image for Profile Picture
# ==================================

# STEP 1: Add your image to static folder
# ----------------------------------------
# Put your profile image here:
# portfolio_app/static/portfolio_app/img/profile.jpg
# (or profile.png, whatever format you have)

# STEP 2: Update views.py
# ----------------------------------------
from django.shortcuts import render, redirect
from django.contrib import messages
from django.templatetags.static import static
from .models import Profile, Project, Skill
from .forms import ContactForm

def home_view(request):
    profile = Profile.objects.first()
    
    if not profile:
        # Fallback static data
        context = {
            'name': 'Probir Saha Shohom',
            'title': 'Python Developer | Backend & AI Enthusiast',
            'profile_pic': static('portfolio_app/img/profile.jpg'),  # STATIC IMAGE PATH
            'contact': {
                'phone': '01711162048',
                'email': 'sohom5102@gmail.com',
                'location': 'Uttara, Dhaka',
                'linkedin_url': 'https://www.linkedin.com/in/probir-saha-shohom',
                'github_url': 'https://github.com/Probir127',
            },
            'summary': 'Passionate and detail-oriented Python Developer with a strong foundation in backend development, REST API design, and clean code practices. Currently completing a Diploma in Computer Science and gaining real-world experience through an internship at ACME.AI, where I developed an AI-powered HR Chatbot. Skilled in FastAPI, Django, Flask, and eager to grow into a full-stack or AI-focused engineering role.',
            'skills_data': {
                'Programming Languages': ['Python', 'JavaScript'],
                'Backend Frameworks/Libraries': ['FastAPI', 'Django', 'Flask'],
                'Frontend Development/UI': ['HTML', 'CSS', 'Responsive Web Design'],
                'Tools, DevOps & OS': ['Git', 'Linux (basic)'],
                'Databases & ORMs': ['SQLite', 'MySQL (basic)'],
                'Core Concepts': ['AI/ML', 'RAG', 'LangChain', 'NLP', 'OOP', 'REST API', 'DSA', 'Debugging', 'Problem Solving'],
            },
            'experience': [
                {
                    'title': 'Software Engineering Intern (Ongoing)',
                    'company': 'ACME.AI',
                    'years': '2025 — Present',
                    'points': [
                        'Developed an AI-powered HR Chatbot using Python and FastAPI to handle employee queries and automate HR responses.',
                        'Collaborated with mentors to debug, test, and improve system performance.',
                        'Gained hands-on experience with backend architecture, version control (Git), and deployment basics on Linux.',
                    ],
                },
            ],
            'projects': [],
            'education': [
                {'degree': 'Diploma in Computer Science (Ongoing)', 'school': 'Ahsanullah Institute of Technical & Vocational Education (AIVET)', 'years': '2022 — Present'},
                {'degree': 'Secondary School Certificate (SSC)', 'school': 'Momtaz Uddin Business Management College', 'years': '2021'},
            ],
            'certifications': ['Front-End Development Certification', 'Continuous Learning: Python for Beginners (self-taught), API Design with FastAPI'],
            'languages': [{'lang': 'Bangla', 'level': 'Native'}, {'lang': 'English', 'level': 'Proficient'}],
            'interests': ['Backend Development', 'AI/ML Applications', 'Problem-Solving Challenges', 'Open-Source Contributions'],
        }
    else:
        contact = getattr(profile, 'contact', None)
        
        # FIXED: Properly group skills by category display name
        grouped_skills = {}
        for skill in profile.skills.all():
            cat_display = skill.get_category_display()
            if cat_display not in grouped_skills:
                grouped_skills[cat_display] = []
            grouped_skills[cat_display].append(skill.name)
        
        # Sort the categories in a logical order
        category_order = [
            'Programming Languages',
            'Backend Frameworks/Libraries',
            'Frontend Development/UI',
            'Databases & ORMs',
            'Tools, DevOps & OS',
            'Core Concepts',
        ]
        
        # Create ordered dictionary
        ordered_skills = {}
        for cat in category_order:
            if cat in grouped_skills:
                ordered_skills[cat] = sorted(grouped_skills[cat])
        
        # Add any remaining categories not in the order
        for cat, skills in sorted(grouped_skills.items()):
            if cat not in ordered_skills:
                ordered_skills[cat] = sorted(skills)
        
        experience = [
            {
                'title': exp.title,
                'company': exp.company,
                'years': exp.years,
                'points': exp.points.splitlines() if exp.points else [],
            } for exp in profile.experiences.all()
        ]
        
        query = request.GET.get('q')
        projects = profile.projects.all().order_by('-id')
        if query:
            projects = projects.filter(technologies__icontains=query)
        
        # Use static image if no profile_pic uploaded, otherwise use uploaded image
        if profile.profile_pic:
            profile_pic_url = profile.profile_pic.url
        else:
            profile_pic_url = static('portfolio_app/img/profile.jpg')
        
        context = {
            'profile': profile,
            'name': profile.name,
            'title': profile.title,
            'profile_pic': profile_pic_url,  # WILL USE STATIC IMAGE
            'contact': contact,
            'summary': profile.summary,
            'skills_data': ordered_skills,
            'experience': experience,
            'projects': projects,
            'education': profile.educations.all(),
            'certifications': [c.name for c in profile.certifications.all()],
            'languages': profile.languages.all(),
            'interests': [i.name for i in profile.interests.all()],
        }
    
    return render(request, 'portfolio_app/home.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'portfolio_app/contact.html', {'form': form})

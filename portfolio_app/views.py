from django.shortcuts import render
from .models import Project, Skill 

def home_view(request):
    
    # --- DYNAMIC DATA FETCHING (Uncomment for full database integration) ---
    # all_projects = Project.objects.all().order_by('-id') 
    # all_skills = Skill.objects.all().order_by('category', 'name')
    # 
    # grouped_skills = {}
    # for skill in all_skills:
    #     if skill.category not in grouped_skills:
    #         grouped_skills[skill.category] = []
    #     grouped_skills[skill.category].append(skill.name)
    # ------------------------------------------------------------------------
    
    # --- STATIC DATA (Based on your detailed content) ---
    # Use static data as a placeholder for immediate visual confirmation
    # Ensure you uncomment the dynamic fetching above and populate the Admin for live data!
    
    context = {
        'name': 'Probir Saha Shohom',
        'title': 'Python Developer | Backend & AI Enthusiast',
        'contact': {
            'phone': '01711162048',
            'email': 'sohom5102@gmail.com',
            'location': 'Uttara, Dhaka',
            'linkedin_url': 'https://www.linkedin.com/in/probir-saha-shohom',
            'github_url': 'https://github.com/Probir127',
        },
        'summary': 'Passionate and detail-oriented Python Developer with a strong foundation in backend development, REST API design, and clean code practices. Currently completing a Diploma in Computer Science and gaining real-world experience through an internship at ACME.AI, where I developed an AI-powered HR Chatbot. Skilled in FastAPI, Django, Flask, and eager to grow into a full-stack or AI-focused engineering role.',
        
        # Static Skills Data - Structured for the template
        'skills_data': {
            'Programming Languages': ['Python', 'JavaScript'],
            'Backend Frameworks': ['FastAPI', 'Django', 'Flask'],
            'Web Development': ['HTML', 'CSS', 'Responsive Web Design'],
            'Tools & Platforms': ['Git', 'Linux (basic)'],
            'Databases': ['SQLite', 'MySQL (basic)'],
            # Updated AI/ML & Concepts with RAG, LangChain, and NLP
            'AI/ML & Concepts': ['AI/ML', 'RAG', 'LangChain', 'NLP', 'OOP', 'REST API', 'DSA', 'Debugging', 'Problem Solving'],
        },
        
        # Static Experience Data
        'experience': [
            {
                'title': 'Software Engineering Intern (Ongoing)',
                'company': 'ACME.AI',
                'years': '2025 – Present',
                'points': [
                    'Developed an AI-powered HR Chatbot using Python and FastAPI to handle employee queries and automate HR responses.',
                    'Collaborated with mentors to debug, test, and improve system performance.',
                    'Gained hands-on experience with backend architecture, version control (Git), and deployment basics on Linux.',
                ],
            },
        ],
        
        # Static Project Data (These should ideally be dynamic from DB for links)
        # Using a minimal structure since we can't reliably predict technologies/links
        'projects': [
            {'title': 'Attendance Management System', 'description': 'Built a desktop-based system to record and manage student attendance efficiently.', 'technologies': 'Python, Database'},
            {'title': 'Café Management System', 'description': 'Developed a small business management tool to handle orders, billing, and inventory tracking.', 'technologies': 'Python, Database'},
            {'title': 'E-Commerce Website', 'description': 'Worked on backend and product management features using Django and HTML, CSS Template', 'technologies': 'Django, HTML, CSS'},
            {'title': 'HR Chatbot (Internship Project)', 'description': 'Created an AI-integrated chatbot with backend logic for HR queries and employee management workflows.', 'technologies': 'FastAPI, AI/ML, Python'},
        ],
        
        # Static Education Data
        'education': [
            {'degree': 'Diploma in Computer Science (Ongoing)', 'school': 'Ahsanullah Institute of Technical & Vocational Education (AIVET)', 'years': '2022 – Present'},
            {'degree': 'Secondary School Certificate (SSC)', 'school': 'Momtaz Uddin Business Management College', 'years': '2021'},
        ],
        
        # Static Certifications/Languages/Interests
        'certifications': ['Front-End Development Certification', 'Continuous Learning: Python for Beginners (self-taught), API Design with FastAPI'],
        'languages': [{'lang': 'Bangla', 'level': 'Native'}, {'lang': 'English', 'level': 'Proficient'}],
        'interests': ['Backend Development', 'AI/ML Applications', 'Problem-Solving Challenges', 'Open-Source Contributions'],
    }
    
    return render(request, 'portfolio_app/home.html', context)
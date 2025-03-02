import random

def generate_linkedin_prospects(location, demographic, industry, industry_focus=None, target_role=None):
    """
    Generate mock LinkedIn prospect suggestions for testing.
    
    Parameters:
    - location: Target geographic location
    - demographic: Target demographic group
    - industry: Target industry
    - industry_focus: Specific focus within the industry (optional)
    - target_role: Specific role being targeted (optional)
    """
    # Mock data with realistic names
    first_names = [
        "Michael", "Sarah", "David", "Jennifer", "Robert",
        "Emma", "James", "Lisa", "William", "Rachel",
        "John", "Jessica", "Thomas", "Emily", "Daniel",
        "Michelle", "Christopher", "Amanda", "Matthew", "Ashley"
    ]
    last_names = [
        "Anderson", "Chen", "Patel", "Martinez", "Thompson",
        "Rodriguez", "Smith", "Johnson", "Wilson", "Brown",
        "Lee", "Garcia", "Miller", "Davis", "Lopez",
        "Harris", "Clark", "Lewis", "Young", "Walker"
    ]

    # Generate more industry-specific company names
    companies = generate_companies_for_industry(industry, industry_focus)

    # Generate job titles, potentially informed by target_role
    job_titles = generate_job_titles(industry, target_role)

    # Generate mock prospects
    mock_prospects = []
    for i in range(5):
        company = random.choice(companies)
        title = random.choice(job_titles)
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        name = f"{first_name} {last_name}"
        profile_url = f"https://linkedin.com/in/{first_name.lower()}-{last_name.lower()}"

        # Create more tailored email templates and follow-ups using all parameters
        email_template = generate_email_template(name, title, company, industry, industry_focus, target_role)
        follow_up_templates = generate_follow_up_templates(name, company, industry, industry_focus, target_role)

        prospect = {
            "name": name,
            "title": title,
            "company": company,
            "location": location,
            "profile_url": profile_url,
            "email_template": email_template,
            "follow_up_templates": follow_up_templates
        }
        mock_prospects.append(prospect)

    return mock_prospects

def generate_companies_for_industry(industry, industry_focus=None):
    """Generate industry-specific company names"""
    
    # Base companies that could work for any industry
    base_companies = [
        "Global Solutions", "Advanced Systems", 
        "Innovative Partners", "Strategic Ventures",
        "Premier Group", "Elite Services"
    ]
    
    # Industry-specific prefixes
    industry_prefixes = {
        "Technology & Software": ["Tech", "Software", "Digital", "Cyber", "Cloud", "Data", "AI"],
        "Finance & Banking": ["Financial", "Capital", "Invest", "Asset", "Wealth", "Bank"],
        "Healthcare & Pharmaceuticals": ["Health", "Care", "Medical", "Pharma", "Bio", "Life"],
        "Manufacturing & Industrial": ["Industrial", "Manufacturing", "Production", "Factory", "Assembly"],
        "Retail & E-commerce": ["Retail", "Shop", "Store", "Market", "Commerce", "Trade"],
        "Education & Training": ["Edu", "Learn", "Training", "Academy", "Institute", "School"],
        "Professional Services": ["Consult", "Advisory", "Service", "Solution", "Professional"],
        "Media & Entertainment": ["Media", "Entertainment", "Creative", "Studio", "Production"],
        "Energy & Utilities": ["Energy", "Power", "Utility", "Resource", "Grid"]
    }
    
    # Industry-specific suffixes
    industry_suffixes = {
        "Technology & Software": ["Systems", "Solutions", "Technologies", "Software", "Networks", "Platforms", "Labs"],
        "Finance & Banking": ["Group", "Partners", "Advisors", "Management", "Trust", "Securities"],
        "Healthcare & Pharmaceuticals": ["Healthcare", "Medical", "Therapeutics", "Sciences", "Pharmaceuticals"],
        "Manufacturing & Industrial": ["Manufacturing", "Industries", "Products", "Works", "Solutions"],
        "Retail & E-commerce": ["Retailers", "Stores", "Marketplace", "Outlets", "Emporium"],
        "Education & Training": ["Education", "Learning", "Academy", "Institute", "University"],
        "Professional Services": ["Consultants", "Partners", "Associates", "Group", "Advisors"],
        "Media & Entertainment": ["Studios", "Media", "Entertainment", "Productions", "Group"],
        "Energy & Utilities": ["Energy", "Power", "Resources", "Utilities", "Group"]
    }
    
    # Generate industry-specific companies
    specialized_companies = []
    
    # Get prefixes and suffixes for the industry, or use defaults if not found
    prefixes = industry_prefixes.get(industry, ["Global", "Advanced", "Innovative", "Strategic"])
    suffixes = industry_suffixes.get(industry, ["Group", "Inc", "Corporation", "Company"])
    
    # Generate 8 industry-specific company names
    for _ in range(8):
        prefix = random.choice(prefixes)
        suffix = random.choice(suffixes)
        
        # If we have industry_focus, try to incorporate it sometimes
        if industry_focus and random.random() > 0.5:
            focus_word = industry_focus.split()[0] if " " in industry_focus else industry_focus
            company_name = f"{prefix} {focus_word} {suffix}"
        else:
            company_name = f"{prefix} {suffix}"
        
        specialized_companies.append(company_name)
    
    # Combine base and specialized companies
    all_companies = base_companies + specialized_companies
    return all_companies

def generate_job_titles(industry, target_role=None):
    """Generate job titles appropriate for the industry and target role"""
    
    # Base titles that could work for any industry
    base_titles = ["CEO", "Founder", "Managing Director", "Business Owner", "Director of Operations"]
    
    # Industry-specific titles
    industry_titles = {
        "Technology & Software": [
            "CTO", "Software Engineer", "Product Manager", "IT Director", 
            "DevOps Manager", "Data Scientist", "VP of Engineering"
        ],
        "Finance & Banking": [
            "CFO", "Financial Advisor", "Investment Banker", "Risk Manager", 
            "Portfolio Manager", "Banking Executive", "Wealth Manager"
        ],
        "Healthcare & Pharmaceuticals": [
            "Medical Director", "Chief Medical Officer", "Research Director", 
            "Clinical Manager", "Healthcare Administrator", "Pharmaceutical Executive"
        ],
        "Manufacturing & Industrial": [
            "Plant Manager", "Operations Director", "Production Supervisor",
            "Quality Control Manager", "Supply Chain Director", "Process Engineer"
        ],
        "Retail & E-commerce": [
            "Retail Manager", "E-commerce Director", "Merchandising Manager",
            "Store Operations Director", "Digital Retail Strategist", "Buyer"
        ],
        "Education & Training": [
            "Principal", "Dean", "Educational Director", "Training Coordinator",
            "Curriculum Developer", "Academic Affairs Director"
        ],
        "Professional Services": [
            "Managing Partner", "Senior Consultant", "Practice Lead",
            "Principal Advisor", "Associate Director", "Client Services Manager"
        ],
        "Media & Entertainment": [
            "Creative Director", "Content Producer", "Media Manager",
            "Entertainment Executive", "Studio Head", "Production Manager"
        ],
        "Energy & Utilities": [
            "Energy Director", "Operations Manager", "Sustainability Manager",
            "Plant Supervisor", "Project Engineer", "Grid Operations Manager"
        ]
    }
    
    # Get titles for the industry, or use base titles if not found
    specialized_titles = industry_titles.get(industry, base_titles)
    
    # If target_role is provided, make sure to include it and variations of it
    if target_role:
        role_variations = [
            target_role,
            f"Senior {target_role}",
            f"Lead {target_role}",
            f"Head of {target_role}",
            f"{target_role} Manager"
        ]
        # Filter out variations that don't make sense
        role_variations = [r for r in role_variations if "Manager Manager" not in r]
        specialized_titles.extend(role_variations)
    
    # Combine base and specialized titles
    all_titles = base_titles + specialized_titles
    return all_titles

def generate_email_template(name, title, company, industry, industry_focus=None, target_role=None):
    """
    Generate a personalized cold outreach email template using all available parameters.
    """
    first_name = name.split()[0]
    
    # Create more specific subject line if we have industry focus
    if industry_focus:
        subject = f"Quick question about {company}'s {industry_focus} initiatives"
    else:
        subject = f"Quick question about {company}'s {industry} initiatives"
    
    # Industry-specific opening lines
    industry_openings = {
        "Technology & Software": [
            f"I noticed your role as {title} at {company} and your focus on {industry_focus or 'technology'} really caught my attention.",
            f"Your background in {target_role or 'technology leadership'} at {company} is impressive.",
            f"I've been following {company}'s innovations in {industry_focus or 'the tech space'} and wanted to connect."
        ],
        "Finance & Banking": [
            f"Your experience as {title} at {company} in the {industry_focus or 'financial'} sector stands out.",
            f"I've been researching leaders in {industry_focus or 'finance'} and your work at {company} is noteworthy.",
            f"Your background in {target_role or 'financial leadership'} is exactly what I was looking for."
        ],
        "Healthcare & Pharmaceuticals": [
            f"I've been following {company}'s advancements in {industry_focus or 'healthcare'} and was impressed by your work as {title}.",
            f"Your expertise in {target_role or 'healthcare management'} at {company} caught my attention.",
            f"I'm reaching out to leaders in {industry_focus or 'healthcare'} like yourself who are making an impact."
        ]
    }
    
    # Get industry-specific opening or use generic one if not found
    openings = industry_openings.get(industry, [
        f"I noticed your role as {title} at {company} and your experience in the {industry} sector really caught my attention.",
        f"Your background at {company} in {industry} is impressive.",
        f"I've been researching leaders in {industry} and your work stood out to me."
    ])
    
    # Use specific value proposition if we have industry focus and target role
    if industry_focus and target_role:
        value_prop = f"I'm reaching out because I've helped similar {industry_focus} companies improve their operations specifically for {target_role}s and drive growth."
    elif industry_focus:
        value_prop = f"I'm reaching out because I've helped similar companies in the {industry_focus} space streamline their operations and drive growth."
    elif target_role:
        value_prop = f"I'm reaching out because I've helped {target_role}s in {industry} companies streamline their operations and drive growth."
    else:
        value_prop = f"I'm reaching out because I've helped similar {industry} companies streamline their operations and drive growth."
    
    # Construct the email template
    template = f"""Subject: {subject}

Hi {first_name},

{random.choice(openings)}

{value_prop} I'd love to share some specific ideas I have for {company}.

Would you be open to a brief 15-minute chat this week to discuss how we might be able to help?

Best regards,
[Your name]"""

    return template

def generate_follow_up_templates(name, company, industry, industry_focus=None, target_role=None):
    """
    Generate follow-up email templates based on different response scenarios,
    incorporating industry, focus, and role information.
    """
    first_name = name.split()[0]
    
    # More specific subject lines based on response type
    positive_subject = "Excited to Connect – Next Steps"
    negative_subject = "Appreciate Your Time – Happy to Stay in Touch"
    no_response_subject = f"Following Up on {industry_focus or industry} Discussion"
    
    # Specific value proposition based on available parameters
    if industry_focus and target_role:
        value_prop = f"how we can support {company}'s {industry_focus} initiatives, particularly for {target_role}s"
    elif industry_focus:
        value_prop = f"how we can support {company}'s {industry_focus} initiatives"
    elif target_role:
        value_prop = f"how we can support {company}'s {target_role}s"
    else:
        value_prop = f"how we can support {company}"
    
    # Industry-specific resources to offer in negative response
    industry_resources = {
        "Technology & Software": f"our latest guide on optimizing {industry_focus or 'technology'} processes",
        "Finance & Banking": f"a market analysis on trends in {industry_focus or 'financial services'}",
        "Healthcare & Pharmaceuticals": f"a whitepaper on innovations in {industry_focus or 'healthcare'} management",
        "Manufacturing & Industrial": f"our case study on improving efficiency in {industry_focus or 'manufacturing'} operations",
        "Retail & E-commerce": f"our report on {industry_focus or 'retail'} customer engagement strategies",
        "Education & Training": f"our guide on {industry_focus or 'education'} technology integration",
        "Professional Services": f"a framework for optimizing {industry_focus or 'professional service'} delivery",
        "Media & Entertainment": f"our analysis of {industry_focus or 'media'} audience engagement trends",
        "Energy & Utilities": f"our whitepaper on {industry_focus or 'energy'} efficiency innovations"
    }
    
    # Get industry-specific resource or use generic one if not found
    resource = industry_resources.get(industry, f"some insights that might be valuable for {company}")
    
    # Create templates with the personalized information
    return {
        "positive": f"""Subject: {positive_subject}

Hi {first_name},

Thanks for your response! I'm glad to hear you're open to discussing {value_prop}.

Let's schedule a time that works best for you. Are you available [provide two or three time slots], or would you prefer to suggest a time? I'll send over a calendar invite once we confirm.

In the meantime, if there are any specific challenges or goals you'd like me to focus on during our call, feel free to share—I want to make the most of our time.

Looking forward to our conversation!

Best regards,
[Your Name]""",

        "negative": f"""Subject: {negative_subject}

Hi {first_name},

I appreciate you getting back to me. I completely understand that now might not be the right time.

If things change or if you'd like to revisit this conversation down the road, I'd be happy to connect when it makes sense for you. In the meantime, I'll stay in touch and share {resource} that might be valuable for {company}.

Wishing you continued success, and feel free to reach out anytime!

Best regards,
[Your Name]""",

        "no_response": f"""Subject: {no_response_subject}

Hi {first_name},

I hope you're doing well! I wanted to follow up on my previous email to see if you had a chance to review it. I understand things get busy, and I completely respect your time.

I'd still love the opportunity to connect and share some ideas on {value_prop}. Would you be open to a quick 15-minute chat this week? Let me know if there's a time that works for you.

Best regards,
[Your Name]"""
    }
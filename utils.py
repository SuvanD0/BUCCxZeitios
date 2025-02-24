import random

def generate_linkedin_prospects(location, demographic, industry):
    """
    Generate mock LinkedIn prospect suggestions for testing.
    """
    # Mock data with realistic names
    first_names = [
        "Michael", "Sarah", "David", "Jennifer", "Robert",
        "Emma", "James", "Lisa", "William", "Rachel"
    ]
    last_names = [
        "Anderson", "Chen", "Patel", "Martinez", "Thompson",
        "Rodriguez", "Smith", "Johnson", "Wilson", "Brown"
    ]

    companies = [
        "Tech Innovators Ltd", "Digital Solutions Inc", 
        "Global Systems Corp", "Future Enterprises",
        "Smart Business Solutions"
    ]

    job_titles = [
        "CEO", "Founder", "Managing Director",
        "Business Owner", "Director of Operations"
    ]

    # Generate mock prospects
    mock_prospects = []
    for i in range(5):
        company = random.choice(companies)
        title = random.choice(job_titles)
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        name = f"{first_name} {last_name}"
        profile_url = f"https://linkedin.com/in/{first_name.lower()}-{last_name.lower()}"

        prospect = {
            "name": name,
            "title": title,
            "company": company,
            "location": location,  # Use input location
            "profile_url": profile_url,
            "email_template": generate_email_template(name, title, company, industry)
        }
        mock_prospects.append(prospect)

    return mock_prospects

def generate_email_template(name, title, company, industry):
    """
    Generate a personalized cold outreach email template.
    """
    first_name = name.split()[0]

    template = f"""Subject: Quick question about {company}'s {industry} initiatives

Hi {first_name},

I noticed your role as {title} at {company} and your experience in the {industry} sector really caught my attention.

I'm reaching out because I've helped similar {industry} companies streamline their operations and drive growth. I'd love to share some specific ideas I have for {company}.

Would you be open to a brief 15-minute chat this week to discuss how we might be able to help?

Best regards,
[Your name]"""

    return template
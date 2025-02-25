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
            "location": location,
            "profile_url": profile_url,
            "email_template": generate_email_template(name, title, company, industry),
            "follow_up_templates": generate_follow_up_templates(name, company)
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

def generate_follow_up_templates(name, company):
    """
    Generate follow-up email templates based on different response scenarios.
    """
    first_name = name.split()[0]

    return {
        "positive": f"""Subject: Excited to Connect – Next Steps

Hi {first_name},

Thanks for your response! I'm glad to hear you're open to discussing how we can support {company}.

Let's schedule a time that works best for you. Are you available [provide two or three time slots], or would you prefer to suggest a time? I'll send over a calendar invite once we confirm.

In the meantime, if there are any specific challenges or goals you'd like me to focus on during our call, feel free to share—I want to make the most of our time.

Looking forward to our conversation!

Best regards,
[Your Name]""",

        "negative": f"""Subject: Appreciate Your Time – Happy to Stay in Touch

Hi {first_name},

I appreciate you getting back to me. I completely understand that now might not be the right time.

If things change or if you'd like to revisit this conversation down the road, I'd be happy to connect when it makes sense for you. In the meantime, I'll stay in touch and share any insights that might be valuable for {company}.

Wishing you continued success, and feel free to reach out anytime!

Best regards,
[Your Name]""",

        "no_response": f"""Subject: Following Up on My Previous Email

Hi {first_name},

I hope you're doing well! I wanted to follow up on my previous email to see if you had a chance to review it. I understand things get busy, and I completely respect your time.

I'd still love the opportunity to connect and share some ideas on how we can help {company} streamline operations and drive growth. Would you be open to a quick 15-minute chat this week? Let me know if there's a time that works for you.

Best regards,
[Your Name]"""
    }
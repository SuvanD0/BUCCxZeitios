import streamlit as st
import pandas as pd
from utils import generate_linkedin_prospects
from styles import apply_styles
import time

def main():
    # Apply custom styles
    apply_styles()

    # Initialize session state
    if 'prospects' not in st.session_state:
        st.session_state.prospects = None
    if 'form_submitted' not in st.session_state:
        st.session_state.form_submitted = False
    if 'show_industry_questions' not in st.session_state:
        st.session_state.show_industry_questions = False
    if 'industry_selected' not in st.session_state:
        st.session_state.industry_selected = None
    if 'industry_focus' not in st.session_state:
        st.session_state.industry_focus = ""
    if 'target_role' not in st.session_state:
        st.session_state.target_role = ""

    st.title("LinkedIn Prospect Finder")
    st.markdown("""
    Find potential LinkedIn prospects based on your target criteria and get customized outreach templates.
    """)

    # Define industry list
    industry_list = [
        "Technology & Software",
        "Finance & Banking",
        "Healthcare & Pharmaceuticals",
        "Manufacturing & Industrial",
        "Retail & E-commerce",
        "Education & Training",
        "Professional Services",
        "Media & Entertainment",
        "Energy & Utilities"
    ]
    
    # Industry-specific questions
    industry_questions = {
        "Technology & Software": {
            "focus_question": "What market segment are you targeting?",
            "focus_options": ["B2B", "B2C", "Enterprise", "SMB", "Startups"],
            "role_question": "What is your ideal target role?",
            "role_options": ["CTO/CIO", "Software Engineers", "Product Managers", "IT Directors", "DevOps"]
        },
        "Finance & Banking": {
            "focus_question": "What financial segment are you targeting?",
            "focus_options": ["Retail Banking", "Investment Banking", "Wealth Management", "Insurance", "Fintech"],
            "role_question": "What is your ideal target role?",
            "role_options": ["CFO", "Financial Advisors", "Risk Managers", "Investment Analysts", "Banking Executives"]
        },
        "Healthcare & Pharmaceuticals": {
            "focus_question": "What healthcare segment are you targeting?",
            "focus_options": ["Hospitals", "Clinics", "Research", "Pharmaceuticals", "Medical Devices"],
            "role_question": "What is your ideal target role?",
            "role_options": ["Physicians", "Hospital Administrators", "Research Directors", "Medical Staff", "Healthcare IT"]
        },
        "Manufacturing & Industrial": {
            "focus_question": "What manufacturing segment are you targeting?",
            "focus_options": ["Automotive", "Electronics", "Chemical", "Aerospace", "Consumer Goods"],
            "role_question": "What is your ideal target role?",
            "role_options": ["Plant Managers", "Operations Directors", "Supply Chain Managers", "Quality Control", "Engineers"]
        },
        "Retail & E-commerce": {
            "focus_question": "What retail segment are you targeting?",
            "focus_options": ["Brick & Mortar", "Online-only", "Omnichannel", "Luxury", "Mass Market"],
            "role_question": "What is your ideal target role?",
            "role_options": ["Merchandisers", "Digital Marketing Managers", "Store Managers", "E-commerce Directors", "Retail Buyers"]
        },
        "Education & Training": {
            "focus_question": "What education segment are you targeting?",
            "focus_options": ["K-12", "Higher Education", "Corporate Training", "Online Learning", "EdTech"],
            "role_question": "What is your ideal target role?",
            "role_options": ["School Administrators", "Faculty", "Educational Directors", "Training Managers", "EdTech Buyers"]
        },
        "Professional Services": {
            "focus_question": "What professional service segment are you targeting?",
            "focus_options": ["Consulting", "Legal", "Accounting", "HR", "Marketing Agencies"],
            "role_question": "What is your ideal target role?",
            "role_options": ["Partners", "Practice Leaders", "Associates", "Consultants", "Department Heads"]
        },
        "Media & Entertainment": {
            "focus_question": "What media segment are you targeting?",
            "focus_options": ["Film & TV", "Music", "Digital Media", "Publishing", "Gaming"],
            "role_question": "What is your ideal target role?",
            "role_options": ["Content Creators", "Producers", "Studio Executives", "Media Buyers", "Creative Directors"]
        },
        "Energy & Utilities": {
            "focus_question": "What energy segment are you targeting?",
            "focus_options": ["Oil & Gas", "Renewable Energy", "Utilities", "Power Generation", "Energy Services"],
            "role_question": "What is your ideal target role?",
            "role_options": ["Operations Managers", "Project Engineers", "Sustainability Directors", "Plant Supervisors", "Business Development"]
        }
    }

    # Input Form - Step 1
    if not st.session_state.show_industry_questions:
        with st.form("industry_form"):
            location = st.text_input(
                "Location",
                placeholder="e.g., San Francisco Bay Area, London, etc."
            )

            demographic = st.text_input(
                "Target Demographic",
                placeholder="e.g., Small Business Owners, C-level Executives, etc."
            )

            industry = st.selectbox(
                "Target Industry",
                options=industry_list,
                key="industry_dropdown"
            )

            submitted_step1 = st.form_submit_button("Next")

        if submitted_step1:
            if not all([location, demographic, industry]):
                st.error("Please fill in all fields to continue.")
            else:
                st.session_state.location = location
                st.session_state.demographic = demographic
                st.session_state.industry_selected = industry
                st.session_state.show_industry_questions = True
                # Use st.rerun() instead of st.experimental_rerun()
                st.rerun()

    # Input Form - Step 2 (Industry-specific questions)
    if st.session_state.show_industry_questions and not st.session_state.form_submitted:
        industry = st.session_state.industry_selected
        
        with st.form("industry_questions_form"):
            st.subheader(f"Tell us more about your {industry} prospects")
            
            # Display industry-specific questions
            if industry in industry_questions:
                focus_q = industry_questions[industry]["focus_question"]
                focus_options = industry_questions[industry]["focus_options"]
                
                industry_focus = st.selectbox(
                    focus_q,
                    options=focus_options,
                    key="industry_focus_select"
                )
                
                role_q = industry_questions[industry]["role_question"]
                role_options = industry_questions[industry]["role_options"]
                
                target_role = st.selectbox(
                    role_q,
                    options=role_options,
                    key="target_role_select"
                )
            
            submitted_step2 = st.form_submit_button("Find Prospects")
        
        if submitted_step2:
            st.session_state.industry_focus = industry_focus
            st.session_state.target_role = target_role
            
            with st.spinner("Searching for relevant prospects..."):
                time.sleep(1)
                # Pass additional parameters to the prospect generator
                st.session_state.prospects = generate_linkedin_prospects(
                    st.session_state.location, 
                    st.session_state.demographic, 
                    st.session_state.industry_selected,
                    st.session_state.industry_focus,
                    st.session_state.target_role
                )
                st.session_state.form_submitted = True
                # Use st.rerun() instead of st.experimental_rerun()
                st.rerun()
    
    # Display Results
    if st.session_state.form_submitted and st.session_state.prospects:
        prospects = st.session_state.prospects

        # Display the refined criteria
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.info(f"**Industry:** {st.session_state.industry_selected}")
            with col2:
                st.info(f"**Focus:** {st.session_state.industry_focus}")
            with col3:
                st.info(f"**Target Role:** {st.session_state.target_role}")

        # Progress indicator
        current_tab = st.radio(
            "Navigate Prospects",
            options=range(len(prospects)),
            format_func=lambda x: f"Prospect {x+1} of {len(prospects)}",
            horizontal=True,
            label_visibility="collapsed"
        )

        # Display current prospect card
        prospect = prospects[current_tab]

        # Card container
        with st.container():
            # Profile section
            st.markdown(f"""
                <div class="prospect-card">
                    <h3>{prospect['name']}</h3>
                    <p class="title">{prospect['title']} at {prospect['company']}</p>
                    <div class="prospect-details">
                        <p>{prospect['location']}</p>
                        <p><a href="{prospect['profile_url']}" target="_blank">View Profile ↗</a></p>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            # Email templates section
            tab1, tab2 = st.tabs(["Initial Outreach", "Follow-up Templates"])

            with tab1:
                email_col1, email_col2 = st.columns([4, 1])
                with email_col1:
                    st.text_area(
                        "Initial Email Template",
                        value=prospect['email_template'],
                        height=200,
                        key=f"email_{current_tab}"
                    )
                with email_col2:
                    st.button(
                        "Copy Template",
                        key=f"copy_initial_{current_tab}",
                        type="primary",
                        use_container_width=True
                    )

            with tab2:
                # Create columns for better layout
                select_col, _ = st.columns([2, 2])
                with select_col:
                    response_type = st.radio(
                        "Select response scenario:",
                        ["Positive Response", "Negative Response", "No Response"],
                        horizontal=True,
                        key=f"response_type_{current_tab}"
                    )

                template_key = {
                    "Positive Response": "positive",
                    "Negative Response": "negative",
                    "No Response": "no_response"
                }[response_type]

                # Follow-up template with copy button
                template_col1, template_col2 = st.columns([4, 1])
                with template_col1:
                    if 'follow_up_templates' in prospect and template_key in prospect['follow_up_templates']:
                        follow_up_value = prospect['follow_up_templates'][template_key]
                    else:
                        # Provide a default template if the key is missing
                        follow_up_value = f"[Default follow-up template for {template_key} scenario]"

                    st.text_area(
                        "Follow-up Template",
                        value=follow_up_value,
                        height=200,
                        key=f"followup_{current_tab}"
                    )
                with template_col2:
                    st.button(
                        "Copy Template",
                        key=f"copy_followup_{current_tab}",
                        type="primary",
                        use_container_width=True
                    )

            # Export and stats section
            with st.expander("Export & Statistics"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Prospects", len(prospects))
                    st.download_button(
                        label="Download as CSV",
                        data=pd.DataFrame(prospects).to_csv(index=False).encode('utf-8'),
                        file_name='linkedin_prospects.csv',
                        mime='text/csv',
                    )
                with col2:
                    st.metric("Industry", st.session_state.industry_selected)
                    st.metric("Focus", st.session_state.industry_focus)
                with col3:
                    st.metric("Location", st.session_state.location)
                    st.metric("Target Role", st.session_state.target_role)
            
            # Reset button to start a new search
            if st.button("Start New Search", type="secondary"):
                for key in st.session_state.keys():
                    del st.session_state[key]
                # Use st.rerun() instead of st.experimental_rerun()
                st.rerun()

if __name__ == "__main__":
    main()
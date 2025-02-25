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

    st.title("LinkedIn Prospect Finder")
    st.markdown("""
    Find potential LinkedIn prospects based on your target criteria and get customized outreach templates.
    """)

    # Input Form
    with st.form("prospect_form"):
        location = st.text_input(
            "Location",
            placeholder="e.g., San Francisco Bay Area, London, etc."
        )

        demographic = st.text_input(
            "Target Demographic",
            placeholder="e.g., Small Business Owners, C-level Executives, etc."
        )

        industry = st.text_input(
            "Target Industry",
            placeholder="e.g., Software Development, Healthcare, Finance, etc."
        )

        submitted = st.form_submit_button("Find Prospects")

    # Form Processing
    if submitted:
        if not all([location, demographic, industry]):
            st.error("Please fill in all fields to continue.")
        else:
            with st.spinner("Searching for relevant prospects..."):
                time.sleep(1)
                st.session_state.prospects = generate_linkedin_prospects(location, demographic, industry)
                st.session_state.form_submitted = True

    # Display Results
    if st.session_state.form_submitted and st.session_state.prospects:
        prospects = st.session_state.prospects

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
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Total Prospects", len(prospects))
                    st.download_button(
                        label="Download as CSV",
                        data=pd.DataFrame(prospects).to_csv(index=False).encode('utf-8'),
                        file_name='linkedin_prospects.csv',
                        mime='text/csv',
                    )
                with col2:
                    st.metric("Industry", industry)
                    st.metric("Location", location)

if __name__ == "__main__":
    main()
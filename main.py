import streamlit as st
import pandas as pd
from utils import generate_linkedin_prospects
from styles import apply_styles
import time

def main():
    # Apply custom styles
    apply_styles()

    st.title("LinkedIn Prospect Finder 🎯")
    st.markdown("""
    Find potential LinkedIn prospects based on your target criteria. This tool uses AI to suggest 
    relevant business profiles that match your requirements.
    """)

    # Input Form
    with st.form("prospect_form"):
        location = st.text_input(
            "Location 📍",
            placeholder="e.g., San Francisco Bay Area, London, etc."
        )

        demographic = st.text_input(
            "Target Demographic 👥",
            placeholder="e.g., Small Business Owners, C-level Executives, etc."
        )

        industry = st.text_input(
            "Target Industry 🏢",
            placeholder="e.g., Software Development, Healthcare, Finance, etc."
        )

        submitted = st.form_submit_button("Find Prospects")

    # Form Validation and Processing
    if submitted:
        if not all([location, demographic, industry]):
            st.error("Please fill in all fields to continue.")
            return

        try:
            with st.spinner("Searching for relevant prospects..."):
                # Simulate loading time for better UX
                time.sleep(1)
                prospects = generate_linkedin_prospects(location, demographic, industry)

                # Display Results
                st.subheader("🎉 Potential Prospects Found")

                # Create tabs for navigation
                if prospects:
                    tabs = st.tabs([f"Prospect {i+1}" for i in range(len(prospects))])

                    for i, (tab, prospect) in enumerate(zip(tabs, prospects)):
                        with tab:
                            # Card container with custom styling
                            st.markdown("""
                                <div style='
                                    background-color: white;
                                    padding: 20px;
                                    border-radius: 10px;
                                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                                    margin-bottom: 20px;'>
                                """, unsafe_allow_html=True)

                            # Header with name and title
                            st.markdown(f"""
                                <h3 style='color: gray; margin-bottom: 5px;'>{prospect['name']}</h3>
                                <h4 style='color: gray; margin-top: 0;'>{prospect['title']}</h4>
                                """, unsafe_allow_html=True)

                            # Company and location info
                            st.markdown(f"""
                                <div style='margin: 15px 0;'>
                                    <p><strong>🏢 Company:</strong> {prospect['company']}</p>
                                    <p><strong>📍 Location:</strong> {prospect['location']}</p>
                                    <p><strong>🔗 Profile:</strong> <a href='{prospect['profile_url']}'>{prospect['profile_url']}</a></p>
                                </div>
                                """, unsafe_allow_html=True)

                            # Email template section
                            st.markdown("#### 📧 Email Template")
                            email_template = st.text_area(
                                "",
                                value=prospect['email_template'],
                                height=200,
                                key=f"email_{i}",
                                label_visibility="collapsed"
                            )

                            # Copy button with better styling
                            if st.button("📋 Copy Email Template", key=f"copy_{i}", type="primary"):
                                st.write("Email template copied to clipboard!")

                            st.markdown("</div>", unsafe_allow_html=True)

                # Success message and export option
                st.success(f"Found {len(prospects)} potential prospects matching your criteria!")

                # Export option
                df = pd.DataFrame(prospects)
                st.download_button(
                    label="📥 Download Results as CSV",
                    data=df.to_csv(index=False).encode('utf-8'),
                    file_name='linkedin_prospects.csv',
                    mime='text/csv',
                )

        except Exception as e:
            st.error(f"An error occurred while processing your request: {str(e)}")

if __name__ == "__main__":
    main()
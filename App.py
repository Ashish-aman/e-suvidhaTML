import streamlit as st
import pandas as pd

# Simulated initial data
def load_data():
    data = {
        "Vendor": ["Vendor A", "Vendor B", "Vendor C"],
        "Risk Score": [0.75, 0.45, 0.9],
        "Risk Level": ["High", "Medium", "High"],
        "Last Updated": ["2024-08-01", "2024-08-15", "2024-08-10"]
    }
    df = pd.DataFrame(data)
    return df

# Feature Input Page
def feature_input():
    st.title("Tata Motors e-Suvidha: Vendor Risk Feature Input")

    # Dropdown options
    industry_options = ["Automotive", "Electronics", "Textiles", "Chemicals"]
    location_options = ["India", "USA", "Germany", "China"]
    credit_rating_options = ["AAA", "AA", "A", "BBB", "BB", "B"]
    compliance_certifications = ["ISO 9001", "ISO 27001", "GDPR Compliant", "None"]

    # User inputs
    vendor_name = st.text_input("Vendor Name")
    industry = st.selectbox("Industry", industry_options)
    location = st.selectbox("Geographical Location", location_options)
    credit_rating = st.selectbox("Credit Rating", credit_rating_options)
    compliance = st.multiselect("Compliance Certifications", compliance_certifications)
    years_in_business = st.slider("Years in Business", 1, 100)
    revenue = st.number_input("Annual Revenue (in million USD)", min_value=0.0)
    debt_equity_ratio = st.number_input("Debt-to-Equity Ratio", min_value=0.0, max_value=10.0)
    
    # Calculate button
    if st.button("Calculate Risk"):
        # Improved Risk Calculation
        risk_score = round((revenue / (years_in_business + 1) + debt_equity_ratio) / 100, 2)

        risk_level = "High" if risk_score > 0.7 else "Medium" if risk_score > 0.4 else "Low"

        # Display the calculated risk score and level
        st.write("### Risk Score and Level")
        st.write(f"**Risk Score for {vendor_name}:** {risk_score}")
        st.write(f"**Risk Level:** {risk_level}")

        # Add the new entry to the session state dataset
        new_entry = pd.DataFrame({
            "Vendor": [vendor_name],
            "Risk Score": [risk_score],
            "Risk Level": [risk_level],
            "Last Updated": [pd.Timestamp.now().strftime("%Y-%m-%d")]
        })

        # Update session state
        if 'df' not in st.session_state:
            st.session_state.df = load_data()

        st.session_state.df = pd.concat([st.session_state.df, new_entry], ignore_index=True)
    else:
        st.write("Enter the vendor details and click 'Calculate Risk' to assess the risk.")

# Display the Dashboard
def risk_overview():
    st.title("Tata Motors e-Suvidha: Vendor Credit Risk Overview")

    if 'df' not in st.session_state:
        st.session_state.df = load_data()

    df = st.session_state.df

    st.write("### Vendor Risk Scores")
    st.dataframe(df)

    st.write("### Risk Distribution")
    st.bar_chart(df['Risk Level'].value_counts())

    st.write("### Risk Score Trend")
    st.line_chart(df.set_index("Vendor")['Risk Score'])

# Simulate Document Analysis
def document_insights():
    st.title("Tata Motors e-Suvidha: Document Insights")

    st.write("### Upload Vendor Documents")
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

    if uploaded_files:
        st.write("### Key Risk Factors (Simulated)")
        st.write("Financial Instability, Market Risk, Contractual Obligations")
        
        st.write("### Document Summaries (Simulated)")
        for file in uploaded_files:
            st.write(f"**Summary for {file.name}:**")
            st.write("This is a simulated summary of the document contents...")
            
        st.write("### Citations (Simulated)")
        st.write("1. Annual Report 2023")
        st.write("2. Market Analysis Q2 2024")

# Expert Review Section
def expert_review():
    st.title("Tata Motors e-Suvidha: Expert Validation")
    
    st.write("### AI-Generated Assessment")
    st.text_area("Assessment Details", "Vendor A has a high risk due to financial instability and market exposure...")

    st.write("### Expert Commentary")
    expert_comment = st.text_area("Add your comments here:")
    
    if st.button("Submit Review"):
        st.write("Review submitted successfully!")
        st.write("Expert Comment:", expert_comment)

# Main application
def main():
    st.sidebar.title("Tata Motors e-Suvidha: Credit Risk Assessment")
    page = st.sidebar.selectbox("Choose a section", ["Risk Overview", "Document Insights", "Expert Validation", "Feature Input"])

    if page == "Risk Overview":
        risk_overview()
    elif page == "Document Insights":
        document_insights()
    elif page == "Expert Validation":
        expert_review()
    elif page == "Feature Input":
        feature_input()

if __name__ == "__main__":
    main()

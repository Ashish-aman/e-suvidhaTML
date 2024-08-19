import streamlit as st
import pandas as pd

# Simulated data
def load_data():
    data = {
        "Vendor": ["Vendor A", "Vendor B", "Vendor C"],
        "Risk Score": [0.75, 0.45, 0.9],
        "Risk Level": ["High", "Medium", "High"],
        "Last Updated": ["2024-08-01", "2024-08-15", "2024-08-10"]
    }
    df = pd.DataFrame(data)
    return df

# Display the Dashboard
def risk_overview(df):
    st.title("Tata Motors e-Suvidha: Vendor Credit Risk Overview")

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
    page = st.sidebar.selectbox("Choose a section", ["Risk Overview", "Document Insights", "Expert Validation"])

    df = load_data()

    if page == "Risk Overview":
        risk_overview(df)
    elif page == "Document Insights":
        document_insights()
    elif page == "Expert Validation":
        expert_review()

if __name__ == "__main__":
    main()

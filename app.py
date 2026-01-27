import streamlit as st
from crew import run_crew
from utils.file_utils import save_md
from utils.pdf_utils import md_to_pdf

st.set_page_config(page_title="AI Research Report Generator")
st.title("📄 AI Research & Report Generator")
st.write("Generate research reports using multi-agent AI")

topic = st.text_input("Enter research topic")

if st.button("Generate Report"):
    if not topic.strip():
        st.warning("Please enter a topic!")
    else:
        with st.spinner("Agents are working... 🤖"):
            report = run_crew(topic)

        st.success("Report generated successfully!")
        st.markdown(report)

        # Save markdown
        md_file = save_md(report)

        # Convert to PDF
        pdf_file = md_to_pdf(report)

        # Download buttons
        st.download_button("Download Markdown", data=open(md_file).read(), file_name="report.md")
        st.download_button("Download PDF", data=open("report.pdf", "rb").read(), file_name="report.pdf", mime="application/pdf")

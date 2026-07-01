import streamlit as st
import pandas as pd
from datetime import date
from fpdf import FPDF
import time
import re

st.set_page_config(page_title="AI Freelancer Assistant Pro - Day 4", layout="wide", page_icon="📄")

# PDF Class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'AI Freelancer Assistant Pro', 0, 1, 'C')
        self.ln(10)

# Session State = Database
if 'client_replies' not in st.session_state: st.session_state.client_replies = []
if 'invoices' not in st.session_state: st.session_state.invoices = []
if 'contracts' not in st.session_state: st.session_state.contracts = []
if 'ai_credits' not in st.session_state: st.session_state.ai_credits = 300

def generate_reply(msg, tone):
    time.sleep(1)
    templates = {
        "Professional": f"Dear Client,\n\nThank you for your message: '{msg}'. I have reviewed your requirements and I am confident I can deliver high-quality results. Let's schedule a call to discuss next steps.\n\nBest Regards,\nWarda",
        "Friendly": f"Hey! Thanks for reaching out about '{msg}'. That sounds like a fun project! I'm excited to work on this. Let's chat about the details?\n\nCheers,\nWarda",
        "Apologetic": f"Dear Client,\n\nI sincerely apologize for the delay regarding '{msg}'. I understand your concern and I am prioritizing this task now. You will have an update from me within 2 hours.\n\nRegards,\nWarda"
    }
    return templates.get(tone, templates["Professional"])

def create_pdf(content, title):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in content.split('\n'):
        pdf.multi_cell(0, 10, line)
    pdf.output(f"{title}.pdf")
    return f"{title}.pdf"

st.title("📄 AI Freelancer Assistant Pro - Day 4")
st.caption("Client Communication & Document Generator")

tab1, tab2, tab3, tab4 = st.tabs(["📊 Dashboard", "💬 Client Reply Generator", "🧾 Invoice Generator", "📑 Contract Generator"])

with tab1:
    st.subheader("Database Tables")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Replies Saved", len(st.session_state.client_replies))
    c2.metric("Invoices Made", len(st.session_state.invoices))
    c3.metric("Contracts Made", len(st.session_state.contracts))
    c4.metric("AI Credits", st.session_state.ai_credits)

with tab2:
    st.subheader("AI Client Reply Generator")
    client_msg = st.text_area("Client Message Input", "Hi, can you send me the project update?")
    tone = st.selectbox("Reply Tone Selection", ["Professional", "Friendly", "Apologetic"])

    if st.button("✨ Generate AI Reply", use_container_width=True):
        if st.session_state.ai_credits >= 5 and client_msg:
            reply = generate_reply(client_msg, tone)
            st.session_state.client_replies.append({"Msg": client_msg[:30], "Reply": reply, "Tone": tone})
            st.session_state.ai_credits -= 5
            
            st.success("Reply Generated!")
            st.text_area("AI Generated Reply", reply, height=150, key="reply_out")
            
            st.download_button("📋 Copy Response", reply, file_name="reply.txt") # Copy kaam
        else:
            st.error("Enter message + Check AI Credits")

    st.divider()
    st.subheader("Saved Replies Database")
    # ERROR FIX: Check lagaya hai
    if st.session_state.client_replies:
        st.dataframe(pd.DataFrame(st.session_state.client_replies), use_container_width=True)
    else:
        st.info("No replies saved yet.")

with tab3:
    st.subheader("Invoice Generator")
    c1, c2 = st.columns(2)
    client_name = c1.text_input("Client Details - Name", "ABC Company")
    client_email = c2.text_input("Client Email", "abc@email.com")
    
    project = st.text_input("Project Details", "Website Development")
    amount = st.number_input("Amount $", 50, 10000, 500)
    tax = st.slider("Tax %", 0, 25, 10)
    due_date = st.date_input("Due Date", date.today())

    if st.button("🧾 Generate Invoice PDF"):
        total = amount + (amount * tax / 100)
        inv_data = {"Client": client_name, "Project": project, "Amount": amount, "Total": total, "Due": str(due_date)}
        st.session_state.invoices.append(inv_data)

        content = f"""INVOICE\n\nTo: {client_name} - {client_email}\nProject: {project}\nAmount: ${amount}\nTax {tax}%: ${amount*tax/100}\nTotal Due: ${total}\nDue Date: {due_date}"""
        
        pdf_file = create_pdf(content, f"Invoice_{re.sub(r'[^A-Za-z0-9]+', '_', client_name)}")
        
        st.success("Invoice Generated!")
        st.download_button("📥 Download PDF", open(pdf_file, "rb"), file_name=pdf_file) # PDF Download

with tab4:
    st.subheader("Contract Generator")
    freelancer_name = st.text_input("Freelancer Details - Your Name", "Warda")
    client_name_c = st.text_input("Client Name", "XYZ Client")
    scope = st.text_area("Project Scope", "Develop a Streamlit app with 4 tabs.")
    timeline = st.text_input("Timeline", "14 days")
    payment = st.text_input("Payment Terms", "50% upfront, 50% on delivery")

    if st.button("📑 Generate Contract PDF"):
        contract_text = f"""CONTRACT AGREEMENT\n\nThis agreement is between {freelancer_name} and {client_name_c}.\n\nScope: {scope}\nTimeline: {timeline}\nPayment: {payment}\n\nTerms & Conditions: All work is original. Revisions included as per scope."""
        
        pdf_file = create_pdf(contract_text, f"Contract_{re.sub(r'[^A-Za-z0-9]+', '_', client_name_c)}")
        st.session_state.contracts.append({"Client": client_name_c, "Scope": scope[:30]})
        
        st.success("Contract Generated!")
        st.download_button("📥 Export PDF", open(pdf_file, "rb"), file_name=pdf_file)

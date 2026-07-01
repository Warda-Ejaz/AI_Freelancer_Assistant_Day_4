# AI_Freelancer_Assistant | Day 4

A professional Streamlit SaaS tool that helps freelancers manage client communication and generate business documents. Features include AI-powered replies, Invoice, and Contract generation with PDF export.

### ✨ Core Modules

#### 1. **Client Reply Generator** 💬
- **Inputs**: Client Message, Tone Selection - `Professional`, `Friendly`, `Apologetic`
- **AI Output**: Context-aware reply generated instantly
- **Features**: Copy Response to clipboard, Save to Database, Session history tracking

#### 2. **Invoice Generator** 🧾
- **Inputs**: Client Details, Project Details, Services, Amount, Tax %, Due Date
- **Logic**: Automatic tax calculation and total amount
- **Export**: One-click PDF Invoice download using `fpdf`

#### 3. **Contract Generator** 📑
- **Inputs**: Freelancer Details, Client Details, Scope, Timeline, Payment Terms, T&C
- **AI Output**: Professional contract text generated from inputs
- **Export**: One-click PDF Contract export

#### 4. **Business Dashboard & Database** 📊
- **Database Tables**: `Invoices`, `Contracts`, `Client Replies` using `st.session_state`
- **Analytics**: Live metrics for all generated documents
- **State Management**: Data persists during the entire session

### 🛠️ Tech Stack

| Category | Technology |
| --- | --- |
| **Framework** | Streamlit |
| **PDF Generation** | FPDF |
| **Data & Analytics** | Pandas, Plotly |
| **State Mgmt** | Streamlit Session State |

### 🚀 Local Setup & Run

1. **Clone & Navigate**
    ```bash
    git clone <https://github.com/Warda-Ejaz/AI_Freelancer_Assistant_Day_4>
    cd AI_FREELANCER_DAY_4
2. *Install Dependencies*
    pip install streamlit pandas plotly fpdf
> `fpdf` is required for PDF Invoice and Contract export.

3. *Launch the Application*
    streamlit run app.py
App will run at `http://localhost:8501`

### ✅ Day 4 Submission Checklist
- Working Client Reply Generator with Tone Selection
- Invoice Generator with PDF Download
- Contract Generator with Export PDF
- Database Integration for Replies, Invoices, Contracts
- Error Handling for empty session_state[x]

---
*Developed by:* Warda Ejaz
*Task:* Day 4 - Client Communication & Document Generator

import streamlit as st
import pandas as pd
import math
from io import BytesIO

st.set_page_config(
    page_title="Electrochemistry Virtual Laboratory",
    page_icon="⚗️",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stApp { background:#1e1e1e; color:#d8d8e2; }
[data-testid="stSidebar"] { background:#191a20; border-right:1px solid #292a32; }
[data-testid="stSidebar"] .block-container { padding-top:1.2rem; }
.block-container { max-width: 1050px; padding-top: 1.4rem; padding-bottom: 3rem; }
h1,h2,h3 { color:#d9d9e5 !important; }
h1 { font-weight:800 !important; line-height:1.2 !important; }
h2,h3 { font-weight:700 !important; }
p,li,label { color:#d0d0da; }
hr { border-color:#2a2b32; }
.stTextInput input,.stTextArea textarea,.stNumberInput input,
div[data-baseweb="select"] { background:#202127 !important; color:#eeeeF5 !important; }
div.stButton>button,div.stDownloadButton>button {
 background:#45464d;color:#f3f3f7;border:0;border-radius:7px;white-space:normal;height:auto;min-height:2.5rem;
}
div.stButton>button:hover,div.stDownloadButton>button:hover { background:#575963;color:white; }
div[data-testid="stMetric"] { background:#202127;border:1px solid #292a32;padding:12px;border-radius:8px; }
.lab-note { background:#1c2232;padding:14px 16px;border-radius:6px;color:#a9dcf5;margin:12px 0 20px; }
.good { background:#1b2a20;color:#92e6ae;padding:12px;border-radius:6px; }
.small-muted { color:#9696a4;font-size:.88rem; }
@media (max-width: 640px) {
  .block-container { padding-left:1rem; padding-right:1rem; padding-top:1rem; }
  h1 { font-size:1.8rem !important; }
  h2 { font-size:1.45rem !important; }
  h3 { font-size:1.2rem !important; }
  [data-testid="stMetric"] { padding:8px; }
  [data-testid="stMetricValue"] { font-size:1.25rem; }
}
</style>
""", unsafe_allow_html=True)

PAGES = [
    "🏠 Home",
    "📖 Theory",
    "🔋 Electrochemical Cell",
    "📊 Nernst Equation Report",
    "⚡ Conductivity Analysis",
    "📝 Assessment",
    "📄 Final Project Report",
]

if "page" not in st.session_state:
    st.session_state.page = PAGES[0]

with st.sidebar:
    st.markdown("## ⚗️ Virtual Lab")
    st.caption("Navigation")
    st.session_state.page = st.radio(
        "Go to", PAGES, index=PAGES.index(st.session_state.page),
        label_visibility="collapsed"
    )
    st.divider()
    st.markdown("### 🧑‍🎓 Student Information")
    student_name = st.text_input("Student Name", key="student_name")
    reg_no = st.text_input("Registration Number", key="reg_no")
    st.divider()
    st.markdown("### 🎓 Learning Objectives")
    st.caption("Students can learn:")
    for item in [
        "Oxidation and reduction",
        "Galvanic cells and electrodes",
        "Cell potential",
        "Nernst equation",
        "Electrolyte conductivity",
        "Electrochemical applications",
    ]:
        st.markdown(f"- {item}")

def footer():
    st.divider()
    st.markdown('<p class="small-muted">⚗️ Electrochemistry Virtual Laboratory | Python + Streamlit | Mobile-friendly layout</p>', unsafe_allow_html=True)

def nernst_potential(e0, n, q, temp):
    # E = E0 - RT/(nF) ln(Q)
    R, F = 8.314462618, 96485.33212
    return e0 - (R * temp / (n * F)) * math.log(q)

def example_cells():
    return {
        "Daniell Cell (Zn/Cu)": {"e0": 1.10, "n": 2, "anode": "Zinc (Zn)", "cathode": "Copper (Cu)", "reaction": "Zn(s) + Cu²⁺(aq) → Zn²⁺(aq) + Cu(s)"},
        "Magnesium/Copper Cell": {"e0": 2.71, "n": 2, "anode": "Magnesium (Mg)", "cathode": "Copper (Cu)", "reaction": "Mg(s) + Cu²⁺(aq) → Mg²⁺(aq) + Cu(s)"},
        "Iron/Copper Cell": {"e0": 0.78, "n": 2, "anode": "Iron (Fe)", "cathode": "Copper (Cu)", "reaction": "Fe(s) + Cu²⁺(aq) → Fe²⁺(aq) + Cu(s)"},
    }

if st.session_state.page == "🏠 Home":
    st.markdown("<h1 style='text-align:center'>⚗️ Electrochemistry<br>Virtual Laboratory</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;color:#a9d5ff !important'>SRM Institute of Science and Technology, Tiruchirappalli</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center'>Faculty of Engineering and Technology | Division of Chemistry</p>", unsafe_allow_html=True)
    st.divider()
    st.header("Welcome to the Virtual Laboratory")
    st.write("Explore how chemical reactions produce electrical energy, calculate cell potentials, and study the conductivity of electrolyte solutions.")
    st.subheader("⚗️ What can students do?")
    for item in [
        "Learn oxidation, reduction, anodes and cathodes",
        "Explore example electrochemical cells",
        "Calculate cell potential using the Nernst equation",
        "Change concentration and temperature to see their effect",
        "Compare electrolyte conductivity data",
        "Complete an assessment and create a project report",
    ]:
        st.markdown(f"✅ {item}")
    st.subheader("Example Electrochemical Cells")
    rows = []
    for name, cell in example_cells().items():
        rows.append({"Cell": name, "Standard Cell Potential (V)": cell["e0"], "Electrons transferred (n)": cell["n"], "Anode": cell["anode"], "Cathode": cell["cathode"]})
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
    st.markdown('<div class="lab-note">Tip: Enter your student details in the sidebar, then open the Electrochemical Cell or Nernst Equation page and change the values to explore the results.</div>', unsafe_allow_html=True)
    footer()

elif st.session_state.page == "📖 Theory":
    st.title("📚 Introduction to Electrochemistry")
    st.subheader("What is electrochemistry?")
    st.write("Electrochemistry studies the relationship between chemical reactions and electrical energy. It includes cells that produce electricity and processes that use electricity to drive chemical change.")
    st.subheader("Oxidation and reduction")
    st.markdown("- **Oxidation:** loss of electrons.\n- **Reduction:** gain of electrons.\n- **Anode:** oxidation occurs.\n- **Cathode:** reduction occurs.")
    st.subheader("Galvanic cell")
    st.write("A galvanic (voltaic) cell converts energy from a spontaneous redox reaction into electrical energy. Electrons travel through the external wire from anode to cathode.")
    st.subheader("Cell potential")
    st.latex(r"E^\\circ_{\\mathrm{cell}} = E^\\circ_{\\mathrm{cathode}} - E^\\circ_{\\mathrm{anode}}")
    st.write("For a spontaneous galvanic reaction under standard conditions, the cell potential is positive.")
    st.subheader("Nernst equation")
    st.latex(r"E = E^\\circ - \\frac{RT}{nF}\\ln Q")
    st.write("Here E is the cell potential, E° is the standard cell potential, R is the gas constant, T is temperature in kelvin, n is the number of electrons transferred, F is Faraday's constant, and Q is the reaction quotient.")
    st.subheader("Applications")
    st.markdown("- Batteries and fuel cells\n- Electroplating\n- Corrosion prevention\n- Sensors and industrial electrolysis")
    footer()

elif st.session_state.page == "🔋 Electrochemical Cell":
    st.title("🔋 Electrochemical Cell Simulator")
    st.markdown('<div class="lab-note">Choose an example cell and adjust ion concentrations. The Nernst equation estimates the cell voltage under the selected conditions.</div>', unsafe_allow_html=True)
    cells = example_cells()
    selected = st.selectbox("Choose a cell", list(cells.keys()))
    cell = cells[selected]
    c1, c2 = st.columns(2)
    with c1:
        zn_conc = st.number_input("Anode-ion concentration (mol/L)", min_value=0.001, max_value=10.0, value=1.0, step=0.1, format="%.3f")
    with c2:
        cu_conc = st.number_input("Cathode-ion concentration (mol/L)", min_value=0.001, max_value=10.0, value=1.0, step=0.1, format="%.3f")
    temp_c = st.slider("Temperature (°C)", min_value=0, max_value=100, value=25)
    # For the learning simulator, Q = anode ion concentration / cathode ion concentration.
    q = zn_conc / cu_conc
    voltage = nernst_potential(cell["e0"], cell["n"], q, temp_c + 273.15)
    st.success("Example cell selected. Results are estimates based on an ideal-solution model.")
    a, b, c = st.columns(3)
    a.metric("Standard potential", f"{cell['e0']:.2f} V")
    b.metric("Estimated cell potential", f"{voltage:.3f} V")
    c.metric("Electrons transferred", str(cell["n"]))
    st.subheader("Cell details")
    st.write(f"**Anode:** {cell['anode']} — oxidation")
    st.write(f"**Cathode:** {cell['cathode']} — reduction")
    st.write(f"**Overall reaction:** {cell['reaction']}")
    st.write(f"**Reaction quotient used in this simplified model:** Q = {q:.4g}")
    st.caption("For teaching purposes, the concentration ratio is simplified to match the example reaction stoichiometry. Real-cell calculations require the full reaction quotient and activities.")
    st.download_button("⬇️ Download cell results (CSV)", pd.DataFrame([{"Cell":selected,"Standard potential (V)":cell["e0"],"Anode ion concentration (mol/L)":zn_conc,"Cathode ion concentration (mol/L)":cu_conc,"Temperature (C)":temp_c,"Estimated cell potential (V)":voltage}]).to_csv(index=False).encode("utf-8"), "electrochemical_cell_results.csv", "text/csv")
    footer()

elif st.session_state.page == "📊 Nernst Equation Report":
    st.title("📊 Nernst Equation Calculator")
    st.markdown('<div class="lab-note">Calculate the cell potential from a standard potential, electron count, reaction quotient, and temperature.</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        e0 = st.number_input("Standard cell potential E° (V)", min_value=-3.0, max_value=3.0, value=1.10, step=0.05)
        n = st.selectbox("Electrons transferred (n)", [1, 2, 3, 4, 5, 6], index=1)
    with c2:
        q = st.number_input("Reaction quotient Q (must be positive)", min_value=0.0001, max_value=10000.0, value=1.0, step=0.1, format="%.4f")
        temp = st.number_input("Temperature (K)", min_value=200.0, max_value=500.0, value=298.15, step=1.0)
    e = nernst_potential(e0, n, q, temp)
    m1, m2 = st.columns(2)
    m1.metric("Calculated cell potential", f"{e:.4f} V")
    m2.metric("Standard potential", f"{e0:.2f} V")
    st.subheader("Equation used")
    st.latex(r"E = E^\\circ - \\frac{RT}{nF}\\ln Q")
    st.write("When Q = 1, ln(Q) = 0, so the calculated potential equals the standard potential.")
    results = pd.DataFrame([{"Standard potential (V)":e0,"Electrons transferred":n,"Reaction quotient Q":q,"Temperature (K)":temp,"Calculated potential (V)":e}])
    st.dataframe(results, use_container_width=True, hide_index=True)
    st.download_button("⬇️ Download Nernst report (CSV)", results.to_csv(index=False).encode("utf-8"), "nernst_equation_report.csv", "text/csv")
    footer()

elif st.session_state.page == "⚡ Conductivity Analysis":
    st.title("⚡ Electrolyte Conductivity Analysis")
    st.markdown('<div class="lab-note">Explore example conductivity readings and compare how strongly different solutions conduct electricity. Values below are illustrative learning data.</div>', unsafe_allow_html=True)
    df = pd.DataFrame([
        {"Electrolyte": "Hydrochloric acid (dilute)", "Conductivity (mS/cm)": 35.0, "Type": "Strong electrolyte"},
        {"Electrolyte": "Sodium chloride solution", "Conductivity (mS/cm)": 18.0, "Type": "Strong electrolyte"},
        {"Electrolyte": "Acetic acid (dilute)", "Conductivity (mS/cm)": 2.5, "Type": "Weak electrolyte"},
        {"Electrolyte": "Sugar solution", "Conductivity (mS/cm)": 0.05, "Type": "Non-electrolyte (approx.)"},
        {"Electrolyte": "Distilled water", "Conductivity (mS/cm)": 0.005, "Type": "Very low conductivity"},
    ])
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.subheader("Select a solution")
    name = st.selectbox("Electrolyte", df["Electrolyte"].tolist())
    row = df[df["Electrolyte"] == name].iloc[0]
    st.metric("Example conductivity", f"{row['Conductivity (mS/cm)']:.3g} mS/cm")
    st.info(f"Classification: **{row['Type']}**. Conductivity depends on the number and mobility of ions in solution, as well as concentration and temperature.")
    st.subheader("Conductivity comparison")
    st.bar_chart(df.set_index("Electrolyte")[["Conductivity (mS/cm)"]])
    st.download_button("⬇️ Download conductivity data (CSV)", df.to_csv(index=False).encode("utf-8"), "conductivity_analysis.csv", "text/csv")
    footer()

elif st.session_state.page == "📝 Assessment":
    st.title("📝 Electrochemistry Assessment")
    st.write("Choose one answer for each question, then submit to view your score.")
    questions = [
        ("Oxidation is the:", ["Gain of electrons", "Loss of electrons", "Gain of neutrons", "Loss of protons"], 1),
        ("Reduction takes place at the:", ["Anode", "Salt bridge", "Cathode", "External wire"], 2),
        ("In a galvanic cell, electrons flow through the external circuit from:", ["Cathode to anode", "Anode to cathode", "Salt bridge to anode", "Solution to salt bridge"], 1),
        ("If Q = 1 in the Nernst equation, then:", ["E = 0 always", "E = E°", "E is always negative", "Temperature is zero"], 1),
        ("Which is a common application of electrochemistry?", ["Electroplating", "Filtration only", "Sieving", "Distillation only"], 0),
    ]
    with st.form("quiz"):
        answers = []
        for i, (question, options, correct) in enumerate(questions):
            answers.append(st.radio(f"{i+1}. {question}", options, key=f"q{i}", index=None))
        submitted = st.form_submit_button("Submit Assessment")
    if submitted:
        score = sum(1 for answer, question in zip(answers, questions) if answer == question[1][question[2]])
        st.session_state.quiz_score = score
        if score >= 4:
            st.success(f"Assessment complete: {score}/{len(questions)}. Great work!")
        else:
            st.info(f"Assessment complete: {score}/{len(questions)}. Review the Theory page and try again.")
        review = pd.DataFrame({"Question":[q[0] for q in questions],"Your answer":[a or "Not answered" for a in answers],"Correct answer":[q[1][q[2]] for q in questions]})
        with st.expander("Review answers"):
            st.dataframe(review, use_container_width=True, hide_index=True)
    footer()

elif st.session_state.page == "📄 Final Project Report":
    st.title("📄 Final Student Electrochemistry Report")
    st.write("Create a personalized project summary using your student details and cell calculation.")
    name = st.text_input("Student Name for Report", value=student_name, key="report_name")
    reg = st.text_input("Registration Number for Report", value=reg_no, key="report_reg")
    title = st.text_input("Project Title", "Study of Cell Potential Using the Nernst Equation")
    e0 = st.number_input("Standard cell potential E° (V)", min_value=-3.0, max_value=3.0, value=1.10, step=0.05, key="final_e0")
    n = st.selectbox("Electrons transferred (n)", [1,2,3,4,5,6], index=1, key="final_n")
    q = st.number_input("Reaction quotient Q", min_value=0.0001, max_value=10000.0, value=1.0, format="%.4f", key="final_q")
    temp = st.number_input("Temperature (K)", min_value=200.0, max_value=500.0, value=298.15, step=1.0, key="final_temp")
    e = nernst_potential(e0,n,q,temp)
    st.markdown('<div class="good">✅ Inputs are ready for the report.</div>', unsafe_allow_html=True)
    st.write(f"**Calculated cell potential:** {e:.4f} V")
    if st.button("📄 Generate Personalized Final Project Report"):
        report = f"""ELECTROCHEMISTRY VIRTUAL LABORATORY
FINAL STUDENT PROJECT REPORT

Student Name: {name or 'Not provided'}
Registration Number: {reg or 'Not provided'}
Project Title: {title}

OBJECTIVE
To investigate how standard cell potential, reaction quotient, electron transfer, and temperature affect electrochemical cell potential.

INPUT DATA
Standard cell potential: {e0:.3f} V
Electrons transferred: {n}
Reaction quotient: {q}
Temperature: {temp:.2f} K

EQUATION
E = E° - (RT/nF) ln(Q)

RESULT
Calculated cell potential: {e:.4f} V

CONCLUSION
Cell potential can change with reaction conditions. The Nernst equation relates the standard potential to the reaction quotient and temperature. This report is intended for educational use.

Generated by Electrochemistry Virtual Laboratory.
"""
        st.text_area("Generated report", report, height=300)
        st.download_button("⬇️ Download Final Report (TXT)", report.encode("utf-8"), "electrochemistry_final_report.txt", "text/plain")
    footer()

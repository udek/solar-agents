import streamlit as st

st.set_page_config(page_title="Solar Hub", page_icon="☀️", layout="wide")

st.title("☀️ Solar Agent Hub")
st.markdown("Your 3 solar engineering tools in one place")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("🔧 PV Multi-Agent")
    st.markdown("AI-powered PV system design & simulation")
    st.markdown("**What it does:**")
    st.markdown("- System sizing & panel selection")
    st.markdown("- Real weather data simulation")
    st.markdown("- Battery storage & savings")
    st.markdown("- PDF report generation")
    if st.button("Launch PV Multi-Agent", type="primary"):
        st.markdown("Open [localhost:8501](http://localhost:8501) or run:")
        st.code('cd "C:\\Users\\Martins Udek\\solar-agents\\pv-multi-agent"\n.venv\\Scripts\\streamlit run gui.py')

with col2:
    st.header("🤖 EnergyAI MCP")
    st.markdown("Solar intelligence inside opencode")
    st.markdown("**What it does:**")
    st.markdown("- Solar production estimates")
    st.markdown("- Incentive & rebate lookups")
    st.markdown("- Energy scoring")
    st.markdown("- Installer routing")
    st.markdown("**Use in opencode by asking:**")
    st.code('"How much will 10kW produce in Lagos?"')
    st.code('"What solar incentives exist?"')
    st.code('"Rate this property\'s solar potential"')

with col3:
    st.header("📐 SolarEdge Designer")
    st.markdown("Professional 3D solar design & proposals")
    st.markdown("**What it does:**")
    st.markdown("- Satellite rooftop detection")
    st.markdown("- Auto panel placement & stringing")
    st.markdown("- Shading analysis")
    st.markdown("- Client-ready PDF proposals")
    if st.button("Open SolarEdge Designer"):
        st.markdown("Go to [solaredge.com/designer](https://solaredge.com/us/products/software-tools/designer)")

st.divider()

st.header("🚀 Quick Start")
st.markdown("1. **Ask me** for solar estimates (EnergyAI works now)")
st.markdown("2. **Launch PV Multi-Agent** for detailed system design")
st.markdown("3. **Use SolarEdge Designer** for professional client proposals")

st.info("Tip: Use PV Multi-Agent for engineering, SolarEdge Designer for the pretty client-facing proposals, and EnergyAI for quick answers.")

if st.checkbox("Show tech details"):
    import subprocess, sys
    st.write("Python:", sys.version)
    try:
        import pvlib; st.write("pvlib:", pvlib.__version__)
    except: st.write("pvlib: not installed")
    try:
        import streamlit; st.write("streamlit:", streamlit.__version__)
    except: st.write("streamlit: not installed")

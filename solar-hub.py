import streamlit as st

st.set_page_config(page_title="Solar Hub", page_icon="☀️", layout="wide")

st.title("☀️ Solar Agent Hub")
st.markdown("Your 3 solar engineering tools in one place")

col1, col2 = st.columns(2)

with col1:
    col1a, col1b = st.columns(2)
    with col1a:
        st.header("🔧 PV Multi-Agent")
        st.markdown("AI-powered PV system design & simulation")
        st.markdown("**What it does:**")
        st.markdown("- System sizing & panel selection")
        st.markdown("- Real weather data simulation")
        st.markdown("- Battery storage & savings")
        st.markdown("- PDF report generation")
        if st.button("Launch PV Multi-Agent", type="primary"):
            st.markdown("Open [localhost:8502](http://localhost:8502)")
    with col1b:
        st.header("🏗️ OpenSolar")
        st.markdown("Free all-in-one solar platform")
        st.markdown("**What it does:**")
        st.markdown("- 3D roof modeling & auto design")
        st.markdown("- Shading analysis (raytracing)")
        st.markdown("- Single Line Diagrams")
        st.markdown("- CRM, proposals, payments")
        if st.button("Open OpenSolar"):
            st.markdown("Go to [app.opensolar.com](https://app.opensolar.com)")

    st.divider()

    st.header("🚀 Quick Start")
    st.markdown("1. **OpenSolar** → 3D design, shading, SLDs, proposals")
    st.markdown("2. **PV Multi-Agent** → engineering sims, battery sizing, PDF reports")
    st.markdown("3. **Ask me** → quick estimates & solar answers (EnergyAI)")

with col2:
    col2a, col2b = st.columns(2)
    with col2a:
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
    with col2b:
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

    st.info("💡 Tip: OpenSolar + PV Multi-Agent + SolarEdge cover design, engineering, and proposals. EnergyAI gives quick answers.")

if st.checkbox("Show tech details"):
    import subprocess, sys
    st.write("Python:", sys.version)
    try:
        import pvlib; st.write("pvlib:", pvlib.__version__)
    except: st.write("pvlib: not installed")
    try:
        import streamlit; st.write("streamlit:", streamlit.__version__)
    except: st.write("streamlit: not installed")

@echo off
set STREAMLIT_EMAIL=
cd /d "C:\Users\Martins Udek\solar-agents\pv-multi-agent"
start "" http://localhost:8502
.venv\Scripts\streamlit run gui.py --server.port 8502

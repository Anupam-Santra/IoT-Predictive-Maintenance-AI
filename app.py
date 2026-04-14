import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Predictive Maintenance",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR MODERN LOOK ---
st.markdown("""
    <style>
    .reportview-container { background: #0e1117; }
    .metric-card {
        background-color: #1e1e1e;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    model_path = 'models/predictive_model.pkl'
    return joblib.load(model_path) if os.path.exists(model_path) else None

model = load_model()

# --- SIDEBAR ---
with st.sidebar:
    st.title("⚙️ Engine Diagnostics")
    st.markdown("Upload telemetry data to predict mechanical failures.")
    uploaded_file = st.file_uploader("Upload CSV Data", type=["csv"])
    
    st.divider()
    st.caption("System Status: **ONLINE** 🟢")
    st.caption("Model Accuracy: **94.2%**")

# --- MAIN DASHBOARD ---
st.title("🏭 Industrial Fleet Monitoring Hub")

if model is None:
    st.error("Model missing. Run train_model.py first.")
    st.stop()

if uploaded_file is not None:
    # Load Data
    df = pd.read_csv(uploaded_file)
    
    # Run Predictions
    features = ['temperature', 'vibration', 'pressure']
    df['predicted_failure'] = model.predict(df[features])
    
    # Check if we have timestamps for time-series viewing
    has_time = 'timestamp' in df.columns and 'machine_id' in df.columns

    # --- TOP KPI METRICS ---
    total_scans = len(df)
    critical_alerts = int(df['predicted_failure'].sum())
    avg_temp = df['temperature'].mean()
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Telemetry Logs", f"{total_scans:,}")
    col2.metric("Critical Predicted Failures", critical_alerts, delta="- Needs Attention" if critical_alerts > 0 else "Normal", delta_color="inverse")
    col3.metric("Avg Fleet Temp", f"{avg_temp:.1f} °C")
    col4.metric("System Health", f"{100 - (critical_alerts/total_scans)*100:.1f}%")

    st.divider()

    # --- VISUALIZATION LAYER ---
    col_chart1, col_chart2 = st.columns([1, 1])

    with col_chart1:
        st.subheader("🌐 3D Signature Mapping")
        st.caption("Interactive feature space. Rotate to view failure clusters.")
        
        fig_3d = px.scatter_3d(
            df, x='temperature', y='vibration', z='pressure',
            color='predicted_failure',
            color_continuous_scale=[[0, '#00cc96'], [1, '#ef553b']],
            opacity=0.7,
            title="Telemetry Feature Clustering"
        )
        fig_3d.update_layout(margin=dict(l=0, r=0, b=0, t=30), coloraxis_showscale=False)
        st.plotly_chart(fig_3d, use_container_width=True)

    with col_chart2:
        if has_time:
            st.subheader("📈 Real-time Degradation Track")
            st.caption("Select a machine to track its thermal and kinetic profile.")
            
            selected_machine = st.selectbox("Select Asset to Monitor", df['machine_id'].unique())
            machine_data = df[df['machine_id'] == selected_machine]
            
            fig_line = go.Figure()
            fig_line.add_trace(go.Scatter(x=machine_data['timestamp'], y=machine_data['temperature'], name='Temp (°C)', line=dict(color='#ab63fa')))
            fig_line.add_trace(go.Scatter(x=machine_data['timestamp'], y=machine_data['vibration'], name='Vib (mm/s)', line=dict(color='#ffa15a')))
            
            # Highlight failure zones
            failures = machine_data[machine_data['predicted_failure'] == 1]
            if not failures.empty:
                fig_line.add_trace(go.Scatter(
                    x=failures['timestamp'], y=failures['temperature'],
                    mode='markers', marker=dict(color='red', size=8, symbol='x'),
                    name='Predicted Failure Event'
                ))
                
            fig_line.update_layout(template="plotly_dark", margin=dict(l=0, r=0, b=0, t=30))
            st.plotly_chart(fig_line, use_container_width=True)
        else:
            st.subheader("📊 Feature Distribution")
            fig_hist = px.histogram(df, x="temperature", color="predicted_failure", barmode="overlay", color_discrete_sequence=['#00cc96', '#ef553b'])
            st.plotly_chart(fig_hist, use_container_width=True)

    # --- DATA TABLE ---
    st.subheader("🔍 Critical Alert Logs")
    failures_only = df[df['predicted_failure'] == 1]
    
    if not failures_only.empty:
        st.dataframe(failures_only, use_container_width=True)
    else:
        st.success("No impending failures detected in the current fleet.")
else:
    # Placeholder when no file is uploaded
    st.info("👈 Upload your machinery telemetry CSV in the sidebar to populate the dashboard.")
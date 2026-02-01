import streamlit as st
import pandas as pd
import numpy as np

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Tim Omotoyinbo | Systems Thinker and Data Scientist",
    layout="wide",
)

# ----------------------------
# Personal profile constants
# ----------------------------
PROFILE = {
    "name": "Tim Omotoyinbo",
    "brand_name": "Timoo",
    "headline": "Systems Thinker | Data Scientist | Metallurgy Researcher | Finance Lead",
    "tagline": "I build decision systems that turn complexity into clarity, then into outcomes.",
    "institution": "University of Johannesburg",
    "lab_focus": "LPBF aluminum alloys, process–microstructure–property mapping, ML-based prediction",
    "role": "Finance Lead, FourthCanvas",
    "location": "Johannesburg, South Africa",
    "email": "hello@timomotoyinbo.com",
    "website": "https://timomotoyinbo.com",
    "linkedin": "https://www.linkedin.com/in/timomotoyinbo/",
    "github": "https://github.com/timomotoyinbo",
}

# Local image path (place the file in your project folder)
PROFILE_IMAGE_URL = "https://github.com/timomotoyinbo/css_streamlit_2026/blob/bd7b86c49371331bb692ee606fe2c2326d3029dd/headshot.jpg"
st.image(PROFILE_IMAGE_URL, caption="Timoo", use_container_width=True)

# ----------------------------
# Sidebar navigation
# ----------------------------
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to:", ["Profile", "Publications", "Data Explorer", "Contact"])
st.sidebar.markdown("---")
st.sidebar.caption("Built as a clarity system: signal, structure, decisions.")

# ----------------------------
# Dummy datasets (tailored)
# ----------------------------
materials_data = pd.DataFrame(
    {
        "Alloy": ["AlSi10Mg", "AlSi10Mg", "AlSi7Mg", "AlSi7Mg", "AlSi10Mg", "AlSi7Mg"],
        "Scan Speed (mm/s)": [800, 1000, 900, 1100, 1200, 950],
        "Laser Power (W)": [350, 350, 330, 330, 350, 330],
        "Hatch Spacing (mm)": [0.11, 0.11, 0.12, 0.12, 0.11, 0.12],
        "Layer Thickness (mm)": [0.03, 0.03, 0.03, 0.03, 0.03, 0.03],
        "Relative Density (%)": [99.2, 98.9, 99.0, 98.6, 98.4, 99.1],
        "Hardness (HV)": [125, 118, 115, 110, 112, 117],
    }
)

finance_data = pd.DataFrame(
    {
        "Month": pd.date_range("2025-01-01", periods=6, freq="MS"),
        "Revenue (ZAR)": [180000, 240000, 220000, 310000, 295000, 360000],
        "Cost (ZAR)": [90000, 120000, 110000, 160000, 155000, 175000],
        "Cash In (ZAR)": [170000, 230000, 200000, 290000, 285000, 345000],
        "Cash Out (ZAR)": [95000, 115000, 125000, 150000, 165000, 185000],
    }
)
finance_data["Gross Margin (ZAR)"] = finance_data["Revenue (ZAR)"] - finance_data["Cost (ZAR)"]
finance_data["Net Cashflow (ZAR)"] = finance_data["Cash In (ZAR)"] - finance_data["Cash Out (ZAR)"]

ml_data = pd.DataFrame(
    {
        "Model": ["XGBoost", "Random Forest", "SVR", "MLP", "Gaussian Process"],
        "Target": ["Hardness (HV)", "Hardness (HV)", "Density (%)", "Hardness (HV)", "Hardness (HV)"],
        "MAE": [3.8, 4.5, 0.25, 4.2, 3.6],
        "RMSE": [5.1, 6.0, 0.33, 5.6, 4.9],
        "R2": [0.91, 0.88, 0.93, 0.89, 0.92],
    }
)

# ----------------------------
# Pages
# ----------------------------
if menu == "Profile":
    st.title(f"{PROFILE['brand_name']} | {PROFILE['headline']}")
    st.write(PROFILE["tagline"])

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        try:
            st.image(PROFILE_IMAGE_PATH, use_container_width=True)
            st.markdown(
                f"<div style='text-align:center; font-weight:600; margin-top:6px;'>{PROFILE['name']}</div>",
                unsafe_allow_html=True,
            )
        except Exception:
            st.warning("Profile image not found. Add your photo at: assets/headshot.jpg")

        st.markdown("### At a glance")
        st.write(f"**Institution:** {PROFILE['institution']}")
        st.write(f"**Location:** {PROFILE['location']}")
        st.write(f"**Research focus:** {PROFILE['lab_focus']}")
        st.write(f"**Industry role:** {PROFILE['role']}")

    with col2:
        st.markdown("## What I do")
        st.write(
            "I design systems that reduce noise, expose signal, and support decisions. "
            "My work spans data science, materials engineering research, and finance operations."
        )

        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("Finance systems", "Cashflow, FP&A", "Decision clarity")
        with m2:
            st.metric("Data science", "ML, forecasting", "Predict and explain")
        with m3:
            st.metric("Metallurgy", "LPBF Al alloys", "Process to property")

        st.markdown("---")

        tabs = st.tabs(["Core domains", "What I build", "Tooling", "Current focus"])

        with tabs[0]:
            st.markdown("### Core domains")
            st.markdown(
                "- **Systems thinking:** map constraints, feedback loops, bottlenecks, incentives\n"
                "- **Data science:** pipelines, modeling, evaluation, deployment-ready outputs\n"
                "- **Materials science:** process–microstructure–property relationships in LPBF"
            )

        with tabs[1]:
            st.markdown("### What I build")
            st.markdown(
                "- **Decision dashboards (BI):** KPI trees and reporting that drive action\n"
                "- **Forecasting and ML models:** predict outcomes and explain drivers\n"
                "- **Materials analytics:** link process parameters to microstructure and properties\n"
                "- **Automation and data pipelines:** clean inputs, trusted metrics, repeatability"
            )

        with tabs[2]:
            st.markdown("### Tooling")
            tool_cols = st.columns(3)
            tools = [
                ("Python and ML", "Modeling, automation, forecasting"),
                ("SQL and Data Modeling", "Metric integrity, transformations"),
                ("BI and Dashboards", "Decision-ready reporting"),
                ("Excel and Financial Modeling", "Scenarios, budgets, sensitivity"),
                ("Materials Informatics", "Feature extraction, property prediction"),
                ("Characterization Data", "SEM, EBSD, XRD signals into insight"),
            ]
            for i, (title, desc) in enumerate(tools):
                with tool_cols[i % 3]:
                    st.markdown(f"**{title}**")
                    st.caption(desc)

        with tabs[3]:
            st.markdown("### Current focus")
            st.markdown(
                "- Building reproducible datasets for LPBF experiments\n"
                "- Training and validating ML models for hardness and density prediction\n"
                "- Designing dashboards that align metrics to decisions\n"
                "- Strengthening data science fundamentals through ALX"
            )

    st.markdown("---")
    st.markdown("## Quick pitch")
    st.info(
        "If your team is sitting on data but not getting decisions, I help you build the structure "
        "that turns information into action."
    )

elif menu == "Publications":
    st.title("Publications")
    st.caption("Upload a CSV to manage publications, filter by keywords, and view trends.")

    st.sidebar.header("Upload and filter")
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

    st.markdown("### Suggested CSV columns")
    st.code("Title, Authors, Year, Venue, Keywords, Link", language="text")

    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications, use_container_width=True)

        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(
                    lambda row: keyword.lower() in row.astype(str).str.lower().values,
                    axis=1
                )
            ]
            st.write(f"Filtered results for: {keyword}")
            st.dataframe(filtered, use_container_width=True)
        else:
            st.write("Showing all publications")

        if "Year" in publications.columns:
            st.subheader("Publication trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.warning("No 'Year' column found, so trends cannot be plotted.")
    else:
        st.info("Upload your publications CSV to populate this page.")

elif menu == "Data Explorer":
    st.title("Data Explorer")
    st.caption("Explore materials, finance, and model performance datasets with filters.")

    st.sidebar.header("Dataset selection")
    data_option = st.sidebar.selectbox(
        "Choose a dataset",
        ["LPBF Process and Properties", "Finance KPIs", "Model Experiments"],
    )

    if data_option == "LPBF Process and Properties":
        st.subheader("LPBF Process and Properties")
        st.dataframe(materials_data, use_container_width=True)

        alloy_filter = st.multiselect(
            "Filter by alloy",
            sorted(materials_data["Alloy"].unique()),
            default=sorted(materials_data["Alloy"].unique()),
        )
        speed_range = st.slider(
            "Scan speed range (mm/s)",
            int(materials_data["Scan Speed (mm/s)"].min()),
            int(materials_data["Scan Speed (mm/s)"].max()),
            (
                int(materials_data["Scan Speed (mm/s)"].min()),
                int(materials_data["Scan Speed (mm/s)"].max()),
            ),
        )
        hardness_range = st.slider(
            "Hardness range (HV)",
            int(materials_data["Hardness (HV)"].min()),
            int(materials_data["Hardness (HV)"].max()),
            (int(materials_data["Hardness (HV)"].min()), int(materials_data["Hardness (HV)"].max())),
        )

        filtered = materials_data[
            (materials_data["Alloy"].isin(alloy_filter))
            & (materials_data["Scan Speed (mm/s)"].between(speed_range[0], speed_range[1]))
            & (materials_data["Hardness (HV)"].between(hardness_range[0], hardness_range[1]))
        ]
        st.write("Filtered results")
        st.dataframe(filtered, use_container_width=True)

    elif data_option == "Finance KPIs":
        st.subheader("Finance KPIs")
        st.dataframe(finance_data, use_container_width=True)

        revenue_range = st.slider(
            "Revenue range (ZAR)",
            int(finance_data["Revenue (ZAR)"].min()),
            int(finance_data["Revenue (ZAR)"].max()),
            (int(finance_data["Revenue (ZAR)"].min()), int(finance_data["Revenue (ZAR)"].max())),
        )

        filtered = finance_data[finance_data["Revenue (ZAR)"].between(revenue_range[0], revenue_range[1])]
        st.write("Filtered results")
        st.dataframe(filtered, use_container_width=True)

        st.subheader("Quick view charts")
        st.line_chart(filtered.set_index("Month")[["Revenue (ZAR)", "Cost (ZAR)", "Net Cashflow (ZAR)"]])

    elif data_option == "Model Experiments":
        st.subheader("Model Experiments")
        st.dataframe(ml_data, use_container_width=True)

        target_filter = st.multiselect(
            "Target",
            sorted(ml_data["Target"].unique()),
            default=sorted(ml_data["Target"].unique()),
        )
        r2_min = st.slider("Minimum R2", 0.0, 1.0, 0.85)

        filtered = ml_data[(ml_data["Target"].isin(target_filter)) & (ml_data["R2"] >= r2_min)]
        st.write("Filtered results")
        st.dataframe(filtered, use_container_width=True)

        st.subheader("Model comparison")
        st.bar_chart(filtered.set_index("Model")[["MAE", "RMSE", "R2"]])

elif menu == "Contact":
    st.title("Contact")
    st.write("If you want to collaborate, discuss a project, or review research ideas, reach out.")

    st.markdown("### Direct")
    st.write(f"**Email:** {PROFILE['email']}")
    st.write(f"**Website:** {PROFILE['website']}")
    st.write(f"**LinkedIn:** {PROFILE['linkedin']}")
    st.write(f"**GitHub:** {PROFILE['github']}")


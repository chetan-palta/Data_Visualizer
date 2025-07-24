# web_app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from datetime import datetime
from fpdf import FPDF
from io import BytesIO
import base64

# --- SETUP ---
st.set_page_config("📊 Data Visualizer Pro", layout="wide")
sns.set_style("whitegrid")
os.makedirs("charts", exist_ok=True)
os.makedirs("reports", exist_ok=True)

st.title("📊 Data Visualizer Pro")

# --- FILE UPLOAD ---
uploaded_file = st.file_uploader("📂 Upload CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip().str.title()
    st.success("✅ File loaded!")

    # --- CLEANING ---
    if df.isnull().any().any():
        st.warning("⚠️ Missing values found. Dropping rows...")
        df.dropna(inplace=True)

    # --- COLUMN TYPES ---
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    categorical_cols = df.select_dtypes(exclude='number').columns.tolist()

    # --- FILTERS ---
    with st.sidebar:
        st.header("📌 Filters")
        if 'Region' in df.columns:
            region = st.selectbox("Filter by Region", ['All'] + sorted(df['Region'].unique()))
            if region != 'All':
                df = df[df['Region'] == region]
        if 'Month' in df.columns:
            month = st.selectbox("Filter by Month", ['All'] + sorted(df['Month'].unique()))
            if month != 'All':
                df = df[df['Month'] == month]
        st.divider()
        theme = st.radio("🎨 Theme", ['whitegrid', 'darkgrid', 'ticks', 'poster'])
        sns.set_style(theme)

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # --- INSIGHTS ---
    st.subheader("📈 Insights")
    insight_text = ""
    if 'Sales' in df.columns:
        if 'Month' in df.columns:
            peak_month = df.groupby('Month')['Sales'].sum().idxmax()
            insight_text += f"💡 Peak Sales Month: **{peak_month}**\n"
        if 'Region' in df.columns:
            top_region = df.groupby('Region')['Sales'].sum().idxmax()
            insight_text += f"💡 Top Sales Region: **{top_region}**\n"
    if 'Expenses' in df.columns and 'Region' in df.columns:
        top_exp = df.groupby('Region')['Expenses'].sum().idxmax()
        insight_text += f"💡 Highest Expenses Region: **{top_exp}**\n"
    st.markdown(insight_text)

    # --- DOWNLOAD DATA ---
    st.download_button("⬇️ Download Filtered CSV", df.to_csv(index=False), "filtered_data.csv")
    excel_buffer = BytesIO()
    df.to_excel(excel_buffer, index=False, engine='xlsxwriter')
    st.download_button("⬇️ Download Filtered Excel", excel_buffer.getvalue(), "filtered_data.xlsx")

    # --- CHART SECTION ---
    st.subheader("📊 Plot Charts")
    col1, col2 = st.columns(2)

    with col1:
        x1 = st.selectbox("Chart 1: X-axis", df.columns, key='x1')
        y1 = st.selectbox("Chart 1: Y-axis", df.columns, key='y1')
        chart1 = st.selectbox("Chart 1 Type", ['line', 'bar', 'scatter', 'box', 'hist', 'pie'], key='c1')

    with col2:
        x2 = st.selectbox("Chart 2: X-axis", df.columns, key='x2')
        y2 = st.selectbox("Chart 2: Y-axis", df.columns, key='y2')
        chart2 = st.selectbox("Chart 2 Type", ['line', 'bar', 'scatter', 'box', 'hist', 'pie'], key='c2')

    if st.button("📊 Compare Charts"):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        def plot(ax, x, y, kind):
            if kind == 'line':
                sns.lineplot(data=df, x=x, y=y, ax=ax)
            elif kind == 'bar':
                sns.barplot(data=df, x=x, y=y, ax=ax)
            elif kind == 'scatter':
                sns.scatterplot(data=df, x=x, y=y, ax=ax)
            elif kind == 'box':
                sns.boxplot(data=df, x=x, y=y, ax=ax)
            elif kind == 'hist':
                sns.histplot(data=df, x=y, bins=20, kde=True, ax=ax)
            elif kind == 'pie':
                pie_data = df.groupby(x)[y].sum()
                pie_data.plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
                ax.set_ylabel("")

            ax.set_title(f"{kind.capitalize()} of {y} vs {x}")
            ax.tick_params(axis='x', rotation=45)

        plot(ax1, x1, y1, chart1)
        plot(ax2, x2, y2, chart2)

        plt.tight_layout()
        st.pyplot(fig)
        chart_path = f"charts/compare_{x1}_{y1}_vs_{x2}_{y2}.png".replace(" ", "_")
        fig.savefig(chart_path)
        st.success(f"✅ Chart saved: {chart_path}")

    # --- FORECASTING ---
    st.subheader("📈 Forecast")
    if numeric_cols:
        fc_col = st.selectbox("Column to forecast", numeric_cols)
        steps = st.slider("Periods to forecast", 1, 12, 3)
        try:
            from statsmodels.tsa.holtwinters import ExponentialSmoothing

            df_fc = df.copy()
            df_fc['Index'] = range(len(df_fc))
            model = ExponentialSmoothing(df_fc[fc_col], trend='add', seasonal=None)
            fit = model.fit()
            future = fit.forecast(steps)

            st.line_chart(pd.concat([df_fc[fc_col], future]))
            st.success("✅ Forecast completed.")
        except:
            st.error("⚠️ Forecast failed. Make sure data is numeric and time-ordered.")

    # --- EXPORT PDF REPORT ---
    st.subheader("📄 Export PDF Report")

    def generate_pdf(text):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)
        report_path = f"reports/Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        pdf.output(report_path)
        return report_path

    if st.button("📤 Generate Report PDF"):
        pdf_text = f"Data Insights Report\n\n{insight_text}\n\nGenerated on: {datetime.now()}"
        path = generate_pdf(pdf_text)
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            href = f'<a href="data:application/octet-stream;base64,{b64}" download="{os.path.basename(path)}">📥 Download Report</a>'
            st.markdown(href, unsafe_allow_html=True)
            st.success("📄 Report generated!")

else:
    st.info("📌 Please upload a CSV file to get started.")

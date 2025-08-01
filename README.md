````markdown
# 📊 Data Visualizer

A powerful, fully offline Python project for exploring CSV data across 3 modes:
- ✅ **CLI script** (`main.py`)
- ✅ **Streamlit web app** (`web_app.py`)
- ✅ **Jupyter dashboard** (`dashboard.ipynb`)

---

## 🚀 Features Overview

### 🖥️ CLI Tool (`main.py`)
- Select plot theme (`darkgrid`, `whitegrid`, etc.)
- Browse and load any CSV from `/`
- Filter data by **Region** or **Month**
- Auto-detect numeric & categorical columns
- Plot line, bar, scatter, histogram, box charts
- Compare charts side-by-side
- Save charts to `/charts`
- Get insights (peak month, top region, etc.)

### 🌐 Streamlit Web App (`web_app.py`)
- Upload and preview CSV in-browser
- Auto-clean missing rows
- Filter by Region/Month (via sidebar)
- Compare charts interactively
- Download data as CSV or Excel
- Forecast trends (e.g., Sales) using time series
- Export PDF reports
- Theme customization

### 📓 Jupyter Dashboard (`dashboard.ipynb`)
- Interactive widgets for CSV, columns, and charts
- Real-time previews
- Filters via dropdowns
- Save charts with one click

---

## 📂 Project Structure

```text
Data_Visualizer/
├── main.py              # CLI version
├── web_app.py           # Streamlit web app
├── dashboard.ipynb      # Interactive Jupyter notebook
├── charts/              # Saved plot images
├── reports/             # Generated PDF reports
├── sample.csv
├── sample2.csv
├── README.md
└── LICENSE
````

---

## ▶️ How to Use

### 🔧 CLI Tool

```bash
python main.py
```

Follow on-screen prompts to choose theme, file, filters, columns, and chart types.

---

### 🌐 Streamlit Web App

```bash
streamlit run web_app.py
```

Use the sidebar to:

* Filter and visualize data
* Forecast trends
* Download filtered CSV/Excel
* Export visual report as PDF

---

### 📓 Jupyter Dashboard

```bash
jupyter notebook dashboard.ipynb
```

Use dropdowns and buttons to explore CSVs and save charts.

---

## 📦 Requirements

Install dependencies:

```bash
pip install pandas matplotlib seaborn streamlit fpdf statsmodels xlsxwriter openpyxl ipywidgets
```

---

## ✅ Feature Matrix

| Feature                    | CLI | Web App | Notebook |
| -------------------------- | :-: | :-----: | :------: |
| Theme selector             |  ✅  |    ✅    |     ❌    |
| CSV filtering              |  ✅  |    ✅    |     ✅    |
| Auto column detection      |  ✅  |    ✅    |     ✅    |
| Side-by-side chart compare |  ✅  |    ✅    |     ❌    |
| CSV/Excel download         |  ❌  |    ✅    |     ❌    |
| Forecasting                |  ❌  |    ✅    |     ❌    |
| PDF export                 |  ❌  |    ✅    |     ❌    |
| Interactive UI             |  ❌  |    ✅    |     ✅    |

---

## 🛠️ Planned Features

* 📂 Drag-and-drop CSV upload in Jupyter
* 📊 Compare multiple datasets simultaneously
* 📄 Visual charts embedded in PDF reports
* 🖥️ Convert into desktop app (PyInstaller or Electron)

---

## 👨‍💻 About the Author

**Chetan Palta** – Ludhiana, Punjab, India
GitHub: [@chetan-palta](https://github.com/chetan-palta)
LinkedIn: [@chetan-palta](https://linkedin.com/in/chetan-palta-b1281329b)

---

## 📄 License

Licensed under the [MIT License](./LICENSE)

```

---



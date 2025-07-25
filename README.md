```markdown
# 📊 Data Visualizer

A full-feature Python project for exploring CSV data interactively—using:
- ✅ **CLI script** (`main.py`)
- ✅ **Streamlit web app** (`web_app.py`)
- ✅ **Jupyter dashboard** (`dashboard.ipynb`)

Works entirely **offline**, no deployment required.

---

## 🚀 Features Overview

### 🖥️ CLI Tool (`main.py`)
- Choose plot theme (`darkgrid`, `whitegrid`, etc.)
- Browse and load any CSV file from folder
- Filter data by **Region** or **Month**
- Detect numeric/categorical columns automatically
- Generate charts: line, bar, scatter, histogram, box
- Compare two charts side-by-side
- Save plots to `/charts`
- Show data insights: peak sales month, top region, expenses hotspot

### 🌐 Streamlit Web App (`web_app.py`)
- Upload and preview CSV in browser
- Clean data and drop missing rows automatically
- Interactive filters via sidebar (Region, Month)
- Plot chart types and compare two side-by-side
- Download filtered data as CSV or Excel
- Forecast future values (e.g., Sales) using time-series model
- Export a PDF report with insights
- Choose from multiple plot themes

### 📓 Jupyter Dashboard (`dashboard.ipynb`)
- Fully interactive widget-based interface
- Dropdowns for selecting CSV, X/Y columns, chart type
- Real-time plot previews
- Region/Month filters as dropdowns
- Button to save charts to `/charts`

---

## 📂 Project Structure

```

Data\_Visualizer/
├── main.py              # CLI version
├── web\_app.py           # Streamlit web app
├── dashboard.ipynb      # Interactive Jupyter notebook
├── charts/              # Saved plot images
├── reports/             # Generated PDF reports
├── sample.csv
├── sample2.csv
├── README.md

````

---

## ▶️ How to Use This Tool

### CLI Tool

```bash
python main.py
````

Follow prompts to select theme, file, filters, columns, and chart options.

---

### Streamlit Web App

```bash
streamlit run web_app.py
```

Use the sidebar to filter data, generate charts, download data, forecast trends, and generate PDF reports.

---

### Jupyter Dashboard

```bash
jupyter notebook dashboard.ipynb
```

Interact with UI controls inline to explore your data and save charts with a button click.

---

## 📦 Requirements

Install all necessary Python packages:

```bash
pip install pandas matplotlib seaborn streamlit fpdf statsmodels xlsxwriter openpyxl ipywidgets
```

---

## 📝 Summary of Features Added

| Feature                    | Available As         |
| -------------------------- | -------------------- |
| Theme selector             | CLI + Streamlit      |
| CSV filtering              | All modes            |
| Automatic column detection | CLI + Web + Notebook |
| Side-by-side chart compare | CLI + Streamlit      |
| CSV/Excel download         | Streamlit only       |
| Sales/Expense forecasting  | Streamlit only       |
| PDF report export          | Streamlit only       |
| Jupyter interactive UI     | Dashboard notebook   |

---

## 🛠 Future Enhancements

* Add drag-and-drop file upload in notebook
* Support multi-dataset analysis
* Include visual report in PDF with embedded charts
* Package as desktop app via PyInstaller or Electron

---

## 🧑‍💻 About the Author

**Chetan Palta** (Ludhiana, Punjab, India)
GitHub: [chetan‑palta](https://github.com/chetan-palta) |
LinkedIn: [chetan‑palta](https://linkedin.com/in/chetan-palta-b1281329b)

---

## 📄 License

This project is open-source under the **MIT License**.

```

---


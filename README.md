# Job Market Skills Analysis

A beginner-friendly data analysis dashboard built with Python, Pandas, NumPy, Matplotlib, and Streamlit.

## Features
- View and filter a sample job-skills dataset
- Calculate total and average openings with NumPy
- Identify the skill with the most sample openings
- Visualize openings using a bar chart
- Visualize opening distribution using a pie chart
- Compare illustrative average salary estimates
- Download filtered data as CSV

## Important note
The included dataset is fictional/illustrative for educational demonstration. It is not live or verified job-market data. Replace `job_market_data.csv` with a properly sourced dataset for real analysis.

## Requirements
- Python 3.9 or newer recommended
- Internet access for the first-time package installation

## Run on Windows
1. Extract the ZIP file.
2. Open the extracted folder.
3. Click the folder address bar in File Explorer, type `cmd`, and press Enter.
4. Run:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Start the app:

   ```bash
   python -m streamlit run app.py
   ```

6. The dashboard should open in your browser. If it does not, copy the local URL shown in Command Prompt into your browser.

## Project structure
- `app.py` — dashboard and analysis code
- `job_market_data.csv` — sample dataset
- `requirements.txt` — Python dependencies
- `README.md` — setup instructions

## Libraries used
- Pandas: reads and filters tabular data
- NumPy: numerical summaries
- Matplotlib: charts
- Streamlit: interactive web dashboard

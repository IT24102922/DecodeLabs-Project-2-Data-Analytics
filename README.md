# E-Commerce Data Auditing & Automated Insights Pipeline (Project 2)

An automated data-driven pipeline developed for the DecodeLabs Data Analytics Internship (Milestone 2). This project covers end-to-end data auditing, descriptive statistics, mathematical anomaly detection, and corporate-standard visual analytics using Python.

## 🚀 Key Deliverables Included
* `clean_data.py`: Automated Python script for data quality auditing and pre-processing.
* `visualize_data.py`: Advanced diagnostic script handling high-fidelity visual representations.
* `Cleaned_Data_Analytics.csv`: Final processed dataset maintaining 100% operational integrity.

---

## 🛠️ Technical Competencies Used
* **Languages & Core Libraries:** Python, Pandas, NumPy
* **Data Visualization:** Seaborn, Matplotlib
* **Environment:** VS Code, Git/GitHub
* **Statistical Methods:** Interquartile Range (IQR), Z-Score Evaluation, Correlation Matrices

---

## 📊 Analytical Insights & Business Value
1. **Data Integrity Standard:** Checked the dataset and confirmed **0 missing values** and **0 duplicates**, securing high-fidelity baselines.
2. **Distribution & Portfolio Performance:** Outlier-cleared data presents a Mean Order Value of `$1,364.55` and Median of `$1,080.70`. A horizontal bar chart revealed that **Desks** and **Laptops** are the core drivers, contributing over 50% of the top-line revenue.
3. **Advanced Anomaly Detection:** Calculated Z-Scores to logically isolate 14 high-value orders, verifying them as valid corporate bulk orders/VIP commercial signals rather than systemic noise.
4. **Data Visualization (Pie Chart Avoidance):** Ditched legacy pie charts for multi-dimensional horizontal bar plots to display marketing channel contributions, identifying Instagram as the primary conversion leader.
5. **Operational Risk Management:** Multi-variable correlation heatmaps and stacked bar plots flagged distinct logistical anomalies in the Electronics segment (Monitors and Phones) due to irregular cancellation and return rates.

---

## 💻 How to Run the Pipeline
1. Ensure Python 3.x, Pandas, NumPy, Matplotlib, and Seaborn are installed.
2. Execute the data auditor first:
   ```bash
   python clean_data.py

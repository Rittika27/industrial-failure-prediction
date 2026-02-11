# 🏭 Industrial Failure Prediction System

Live Demo: https://huggingface.co/spaces/RIT27/industrial-failure-prediction  
GitHub Repo: https://github.com/Rittika27/industrial-failure-prediction

---

## 📌 Project Summary

Predictive maintenance is critical in modern manufacturing to reduce unplanned downtime and maintenance cost.  
This project uses **machine learning** to identify machine failures and diagnose **specific failure types** using real industrial sensor data.

---

## 🚀 Features

✅ Predicts whether a machine will fail  
✅ Identifies specific failure types:
- TWF — Tool Wear Failure  
- HDF — Heat Dissipation Failure  
- PWF — Power Failure  
- OSF — Overstrain Failure  
- RNF — Random Failure

✅ Merged and trained on **multiple industrial datasets**  
✅ Evaluated with:
- Confusion Matrix  
- ROC Curve  
- Multi-label classification metrics

✅ **Interactive web demo** deployed on Hugging Face using Gradio  
✔ You can input real sensor values and get real-time predictions.

---

## 📊 Model Performance

| Failure Type | Precision | Recall | F1-Score |
|--------------|-----------|--------|----------|
| TWF          | 1.00      | 1.00   | 1.00     |
| HDF          | 1.00      | 1.00   | 1.00     |
| PWF          | 1.00      | 1.00   | 1.00     |
| OSF          | 1.00      | 1.00   | 1.00     |
| RNF          | 1.00      | 1.00   | 1.00     |

The model demonstrates strong generalization even when trained and tested on separate industrial datasets.

---

## 🧠 Tech Stack

- Python  
- Scikit-learn  
- Pandas / NumPy  
- Gradio (Deployment)  
- Hugging Face Spaces

---

## 🛠 Project Structure

industrial-failure-prediction/
├── app.py # Gradio application
├── requirements.txt # Dependencies
├── predictive_maintenance_model.pkl # Trained ML model
├── README.md # Project summary (this file)


---

## 🧰 How It Works

1. Collect and merge real industrial sensor data  
2. Preprocess features (temperatures, rpm, torque, tool wear)  
3. Train multi-output ML model for failure types  
4. Deploy an interactive Gradio UI to Hugging Face  
5. Predict failures and provide actionable results

---

## 💡 Why This Matters

This system can be used in:
✅ Smart factories  
✅ Industry 4.0 analytics  
✅ Manufacturing maintenance dashboards  
✅ Preventive action and cost reduction strategies

---

## 📍 Try It Live

👉 **Hugging Face Space:**  
https://huggingface.co/spaces/RIT27/industrial-failure-prediction

---

## 📄 About the Author

**Rittika27**  
AI & Data Science enthusiast building industrial ML solutions. 

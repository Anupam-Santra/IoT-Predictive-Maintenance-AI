# 🏭 AI-Powered Predictive Maintenance System for IoT Devices

![GitHub repo size](https://img.shields.io/github/repo-size/Anupam-Santra/IoT-Predictive-Maintenance-AI)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit_Learn-orange)

## 📌 Overview
This project simulates an industrial IoT environment where sensor telemetry data (temperature, vibration, pressure) is actively monitored by an Artificial Intelligence engine. The system's Machine Learning backend classifies equipment health and predicts mechanical failures *before* they occur.

## ⚙️ Industry Relevance 
In environments like manufacturing facilities, aviation, and power plants, unexpected asset failure translates to severe profit loss and safety hazards. Predictive maintenance solves this by interpreting machine signatures, allowing preemptive part replacement while avoiding over-maintenance costs. 

## 🛠️ Technology Stack
- **Language:** Python
- **Data Manipulation:** NumPy, Pandas
- **Machine Learning:** Scikit-Learn (Random Forest)
- **Data Visualization:** Matplotlib, Seaborn

## 🚀 How to Run Locally 
1. Clone the repository: `git clone https://github.com/Anupam-Santra/IoT-Predictive-Maintenance-AI.git`
2. Install requirements: `pip install -r requirements.txt`
3. Generate synthetic IoT data: `python src/data_generator.py`
4. Train the AI model: `python src/train_model.py`
5. Test failure predictions and generate visualization dashboards: `python src/predict.py`

## 📊 Sample Output 
*(Upload your images/failure_scatter.png to GitHub and link it here!)*
![Scatter Plot](./images/failure_scatter.png)

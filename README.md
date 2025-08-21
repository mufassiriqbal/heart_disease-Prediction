# 🩺 Heart Disease Prediction using Machine Learning

## 📜 Description  
A machine learning project for predicting heart disease using patient health data.  
Models like **KNN, SVM, Decision Tree, and Random Forest** are trained and compared.  
Includes **data visualization, evaluation metrics, and saved `.pkl` models** for deployment.  
👉 Frontend (Streamlit/Flask app) will be uploaded soon!  

---

## ⚙️ Models Implemented
- K-Nearest Neighbors (KNN)  
- Support Vector Machine (SVM)  
- Decision Tree Classifier  
- Random Forest Classifier  

---

## 📊 Dataset  
The dataset used is the **UCI Heart Disease dataset** (or Kaggle equivalent).  
**Features**: Age, Sex, Chest pain type, Resting BP, Cholesterol, Max HR, etc.  
**Target**:  
- `0` → No Heart Disease  
- `1` → Heart Disease Present  

---

## 🚀 Steps in the Project
1. Data Cleaning & Preprocessing  
2. Feature Visualization (scatter plots, PCA, pairplots)  
3. Model Training with KNN, SVM, Decision Tree, Random Forest  
4. Model Evaluation: Accuracy, Precision, Recall, F1-Score, Confusion Matrix  
5. Model Saving with **Pickle (`.pkl` files)**  

---

## 📈 Results
- **KNN (k=1)** achieved the highest accuracy (~97–99%).  
- Other models performed well but slightly lower depending on tuning.  
- Trade-off: small `k` in KNN captures detail (may overfit), larger `k` generalizes better.  

---

## 🛠️ Tech Stack
- Python 🐍  
- Scikit-learn  
- Pandas, NumPy  
- Matplotlib, Seaborn  

---

## ▶️ How to Use  

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction

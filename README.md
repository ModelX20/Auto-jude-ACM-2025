# AutoJudge 🧠  
### Automated Programming Problem Difficulty Predictor

AutoJudge is a Machine Learning–based web application that predicts the **difficulty level** of programming problems (**Easy / Medium / Hard**) and assigns a **numerical difficulty score (1–10)** based on the textual description of the problem.

The system uses **Natural Language Processing (NLP)** and **supervised learning models** to analyze programming problem statements and estimate their complexity.

---

## 🚀 Features
- Difficulty classification: **Easy / Medium / Hard**
- Numerical difficulty scoring (1–10)
- Text-based analysis using **TF-IDF**
- Interactive **Streamlit** web interface
- End-to-end ML workflow:
  - Data preprocessing
  - Feature extraction
  - Model training
  - Web-based inference

---

## 📊 Dataset Used

The dataset consists of programming problems stored in **JSONL format**.  
Each data entry includes:
- Problem description
- Input specification
- Output specification
- Difficulty class label (Easy / Medium / Hard)
- Numerical difficulty score

**Dataset location:**

---

## 🧠 Approach and Models Used

1. **Data Preprocessing**
   - Combined problem description, input description, and output description into a single text field.
   - Removed missing values and performed basic text cleaning.

2. **Feature Extraction**
   - Used **TF-IDF Vectorization** to convert textual data into numerical feature vectors.

3. **Model Experimentation**
   The following models were evaluated:
   - Support Vector Classifier (SVC)
   - Gradient Boosting
   - Random Forest

   Although SVC and Gradient Boosting models were tested with different hyperparameters, they did not outperform Random Forest on the given dataset.

4. **Final Models Selected**
   - **Classification:** Random Forest Classifier (Easy / Medium / Hard)
   - **Regression:** Random Forest Regressor (Difficulty score)

   Random Forest was selected due to its **more stable and consistent performance** on this dataset.

---

## 📈 Evaluation Metrics

- **Classification Accuracy:** ~54–57%
- **Regression Metrics:**
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)

The accuracy is limited due to subjectivity in difficulty labels and dataset ambiguity, which is common in text-based difficulty prediction tasks.

---

## 🖥️ Web Interface Explanation

The web interface is built using **Streamlit** and allows users to:
- Enter:
  - Problem description
  - Input description
  - Output description
- Predict:
  - Difficulty level (Easy / Medium / Hard)
  - Numerical difficulty score
- Clear inputs using a **Clear All** button

The application runs **locally** and does not require online hosting.

---

## ⚠️ Important Note About Model Files

The file **`difficulty_regressor.pkl`** is **not included** in this repository.

**Reason:**  
GitHub does not allow uploading files larger than **25 MB**, and the regression model exceeds this limit.

The project has been **fully tested locally**, and instructions are provided below to run the project successfully.

---

##  How to Run the Project (Evaluator Instructions)

### STEP 1 : Download the repository

git clone <YOUR_GITHUB_REPO_LINK>
cd AutoJudge

### STEP 2: Install Dependencies
pip install -r requirements.txt

### STEP 3 :Add the Regression Model
Place the file difficulty_regressor.pkl in the same folder as app.py.
link for difficulty_regressor.pkl - https://drive.google.com/file/d/1kg9D1u_b25sYiAoubV6OBUOZQF6ydJlJ/view?usp=sharing

### STEP 4 : Run the command in terminal
streamlit run app.py



# AutoJudge   
### Automated Programming Problem Difficulty Predictor

AutoJudge is a Machine Learning–based web application that predicts the **difficulty level** of programming problems (**Easy / Medium / Hard**) and assigns a **numerical difficulty score** based on the problem description.

---

##  Features
- Predicts problem difficulty: **Easy, Medium, Hard**
- Generates a difficulty score (1–10)
- NLP-based analysis using **TF-IDF**
- Clean and interactive **Streamlit** web interface
- End-to-end ML workflow (training → prediction → UI)

##  Model Experimentation

Tried using multiple machine learning models during development, including:

- Support Vector Classifier (SVC)
- Gradient Boosting
- Random Forest

Tried to implement SVC and Gradient Boosting models with different hyperparameters, but they failed to outperform the Random Forest model on the given dataset.
Based on empirical evaluation and validation accuracy, I selected **Random Forest** for both classification and regression tasks, as it provided more stable and consistent results.




##  Project Structure
##  Important Note About Model Files

The file **`difficulty_regressor.pkl`** is **not included** in this repository.

🔹 Reason:  
GitHub does not allow uploading files larger than **25 MB**, and the regression model exceeds this limit.

🔹 The application has been **fully tested locally** with this model.

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



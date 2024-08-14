
# **Sentiment Analysis with MLOps**

This repository contains a complete end-to-end machine learning pipeline designed for sentiment analysis. Leveraging tools like MLflow, DagsHub, DVC, Flask, and Cookiecutter, this project showcases the journey from experimentation to model deployment in a reproducible and scalable manner.

## **Table of Contents**

1. [Project Overview](#project-overview)
2. [Directory Structure](#directory-structure)
3. [Installation](#installation)
4. [Experimentation & Model Building](#experimentation--model-building)
5. [DVC Pipeline Development](#dvc-pipeline-development)
6. [Model Registry & Deployment](#model-registry--deployment)
7. [Project Organization & Version Control](#project-organization--version-control)
8. [Future Work](#future-work)
9. [Contributing](#contributing)
10. [License](#license)

## **Project Overview**

This project focuses on building a sentiment analysis model using various machine learning techniques. The pipeline integrates multiple tools and frameworks to ensure that models are high-performing, reproducible, and ready for deployment.

### **Key Features:**

- **Experiment Tracking:** Managed using MLflow, which tracks experiments, models, and metrics.
- **Version Control:** Handled by Git and DVC, ensuring that both code and data are versioned.
- **Model Deployment:** The best model is deployed using Flask for real-time sentiment analysis.
- **Collaboration:** Enabled through DagsHub, allowing for team-based experiments.


## **Installation**

To get started with this project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Install DVC and MLflow
pip install dvc[all] mlflow
```

## **Experimentation & Model Building**

### **1️⃣ Baseline Model**

Start by running the baseline model using Logistic Regression with Bag of Words as the feature extraction technique.

### **2️⃣ Model Exploration**

Explore different combinations of models such as Random Forest, Naive Bayes, Gradient Boosting, XGBoost, LSTM, and feature extraction techniques (Bag of Words, TF-IDF).

### **3️⃣ Hyperparameter Tuning**

Fine-tune hyperparameters across different models to achieve the best performance.

All these experiments are tracked and logged in MLflow for easy comparison and analysis.

## **DVC Pipeline Development**

The DVC pipeline manages the entire workflow, from data ingestion to model registration. Here's a quick rundown of how to run the pipeline:

```bash
# Initialize DVC and add the pipeline stages
dvc init
dvc repro
```

Refer to the `dvc.yaml` file for the exact structure and sequence of pipeline stages.

## **Model Registry & Deployment**

### **1️⃣ Model Registry**

The best-performing model is registered in the MLflow model registry. This allows tracking of different model versions and makes deployment straightforward.

### **2️⃣ Deployment with Flask**

Use the `app.py` script to deploy the model as a Flask web application for real-time sentiment analysis predictions:

```bash
python app.py
```

Access the app by navigating to `http://localhost:5000` in your browser.

## **Project Organization & Version Control**

### **Cookiecutter for Project Structure**

The project layout is created using Cookiecutter to ensure consistent and organized structure across the project.

### **Git & DVC for Version Control**

- **Git:** Manages source code and notebook versioning.
- **DVC:** Manages data versioning and tracks changes to datasets.

All source files are stored in GitHub, while datasets are versioned in a local TEMP folder.

## **Future Work**

- **Integrating CI/CD:** Set up continuous integration and deployment pipelines.
- **Advanced Feature Engineering:** Experiment with more sophisticated techniques like Word2Vec and GloVe.
- **Model Interpretability:** Incorporate tools like SHAP and LIME to make model predictions interpretable.

## **Contributing**

Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request.

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

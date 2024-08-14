from flask import Flask, render_template,request
import mlflow
from preprocessing_utility import normalize_text
import dagshub
import pickle


mlflow.set_tracking_uri("https://dagshub.com/sudeepjoelbayyee/MLOps-Mini-Project.mlflow")
dagshub.init(repo_owner='sudeepjoelbayyee', repo_name='MLOps-Mini-Project', mlflow=True)

app = Flask(__name__)

# load model from model registry
def get_latest_model_version(model_name):
    client = mlflow.MlflowClient()
    latest_version = client.get_latest_versions(model_name, stages=["Production"])
    if not latest_version:
        latest_version = client.get_latest_versions(model_name, stages=["None"])
    return latest_version[0].version if latest_version else None

model_name = "my_model"
model_version = get_latest_model_version(model_name)

model_uri = f'models:/{model_name}/{model_version}'
model = mlflow.pyfunc.load_model(model_uri)

vectorizer = pickle.load(open('models/vectorizer.pkl','rb'))

@app.route("/")
def home():
    return render_template("index.html",result=None)

@app.route("/predict", methods=['POST'])
def predict():
    text = request.form['text']

    # clean
    text = normalize_text(text)

    # BOW
    features = vectorizer.transform([text])

    # prediction
    result = model.predict(features)

    return render_template("index.html",result=result[0])

    return text

app.run(debug=True)


import dagshub
import mlflow

mlflow.set_tracking_uri("https://dagshub.com/sudeepjoelbayyee/MLOps-Mini-Project.mlflow")
dagshub.init(repo_owner='sudeepjoelbayyee', repo_name='MLOps-Mini-Project', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
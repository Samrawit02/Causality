import mlflow
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from file_helper import FileHelper
import pickle


Config.MODELS_PATH.mkdir(parents=True, exist_ok=True)
Config.METRICS_FILE_PATH.mkdir(parents=True, exist_ok=True)


class TrainModel():
  def __init__(self, X_train, X_test, y_train, y_test, model_name="LR"):

        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.model_name = model_name

        self.clf = LogisticRegression()
        # self.logger = App_Logger("models.log").get_app_logger()

  
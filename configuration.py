from configparser import ConfigParser
import os


class Configuration:

    def __init__(self):
        project_config = ConfigParser()
        project_config.read('/home/sachin/Desktop/sentiment-analysis-cp/inference/app/config.ini')
        self.DATA_PATH = project_config.get('IO', "dataset_path")
        self.TEST_PATH = project_config.get('IO', "test_path")
        self.MODEL_PATH = project_config.get('IO', "model_path")
        self.LOAD_MODEL_PATH = project_config.get('IO', "load_model_path")
        self.PREDICTION_PATH = project_config.get('IO', "prediction_path")


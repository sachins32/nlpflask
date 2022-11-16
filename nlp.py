import ktrain
import configuration as c

config = c.Configuration()

class nlp_prediction():

    def model_predict(self, data):
        filePath = config.LOAD_MODEL_PATH
        predictor = ktrain.load_predictor(
            filePath, batch_size=32, custom_objects=None)
        df = data[4]
        results = predictor.predict(df)
        return results

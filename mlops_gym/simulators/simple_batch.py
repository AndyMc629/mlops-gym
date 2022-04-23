import mlops_gym

BATCH_SIZE = 10




class SimpleBatchSimulator(mlops_gym.Simulator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def model_predict(self):
        self.model.predict()
        #pass


def create_wine_classifier_model():
    from sklearn.datasets import load_wine
    import sklearn.metrics
    import autosklearn.classification
    from sklearn.model_selection import train_test_split
    from joblib import dump,load

    try:
        automl = load('wine_classifier.pkl')
    except:
        automl = autosklearn.classification.AutoSklearnClassifier(
            time_left_for_this_task=30,#60,
            per_run_time_limit=2#30
        )

        # Grab the data
        wine_data = load_wine()
        feature_names = wine_data.feature_names
        X, y = wine_data.data, wine_data.target

        # Make a 70/30 reference/test split
        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.70,
                                                        random_state=42)

        automl.fit(X_train, y_train, dataset_name='wine')

        print(automl.show_models())
        print(automl.sprint_statistics())
        predictions = automl.predict(X_test)
        sklearn.metrics.accuracy_score(y_test, predictions)
        dump(automl, 'wine_classifier.pkl')

    return automl


if __name__ == "__main__":
    model = create_wine_classifier_model()
    simple_batch_simulator = SimpleBatchSimulator(model=model)
    simple_batch_simulator.create_sim_batch_dataframe()
    print(simple_batch_simulator.simulated_data_frame)
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score


class LogisticRegressionModel:
    @staticmethod
    def create_save_pickle(testcsv, regression_model, y_test):

        # Dump the trained decision tree classifier with Pickle
        decision_tree_pkl_filename = '../Model/logistic_regression.pkl'

        # Write and save file in pkl format
        decision_tree_model_pkl = open(decision_tree_pkl_filename, 'wb')
        pickle.dump(regression_model, decision_tree_model_pkl)

        # Close the pickle instance
        decision_tree_model_pkl.close()

        # Loading the saved decision tree model pickle
        decision_tree_model_pkl = open(decision_tree_pkl_filename, 'rb')
        pickelmodel = pickle.load(decision_tree_model_pkl)

        df = pd.read_csv(testcsv)
        X_test = df.loc[:, ['Age', 'EstimatedSalary']]

        y_pred = pickelmodel.predict(X_test)

        test_accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy is :", test_accuracy)

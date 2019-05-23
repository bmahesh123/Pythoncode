import pickle
import pandas as pd
from sklearn.metrics import accuracy_score


class RandomForestModel:
    @staticmethod
    def create_save_pickle(test_csv_path, regression_model, y_test):

        # Dump the trained decision tree classifier with Pickle
        decision_tree_pkl_filename = '../Model/Random_Classifier_Model.pkl'

        # Write and save file in pkl format
        decision_tree_model_pkl = open(decision_tree_pkl_filename, 'wb')
        pickle.dump(regression_model, decision_tree_model_pkl)

        # Close the pickle instance
        decision_tree_model_pkl.close()

        # Loading the saved decision tree model pickle
        decision_tree_model_pkl = open(decision_tree_pkl_filename, 'rb')
        pickelmodel = pickle.load(decision_tree_model_pkl)

        df = pd.read_csv(test_csv_path)
        X_test = df.loc[:, ['Age', 'EstimatedSalary']]

        # Prediction using test data
        y_pred = pickelmodel.predict(X_test)

        # Calculating Accuracy
        test_accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy of Test set is :", test_accuracy)



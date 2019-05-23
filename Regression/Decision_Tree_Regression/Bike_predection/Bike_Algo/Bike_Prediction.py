# Importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np
import matplotlib.pyplot as plt


class Bikepred:
    try:
        @staticmethod
        def bike_pred():
            # Importing dataset and splitting dataset into 2 different csv files
            dataSet = pd.read_csv('../Dataset/bike_sharing.csv')

            df_training = dataSet.sample(frac=0.8)
            df_test = pd.concat([dataSet, df_training]).drop_duplicates(keep=False)

            df_training.to_csv('../Dataset/training_data.csv', header=True, index=None)
            df_test.to_csv('../Dataset/test_data.csv', header=True, index=None)

            dataSet = pd.read_csv('../Dataset/training_data.csv')

            x1_index = dataSet.columns.get_loc("temp")
            y_index = dataSet.columns.get_loc("cnt")

            x = dataSet.iloc[:, [x1_index]]
            y = dataSet.iloc[:, y_index:(y_index + 1)]

            # Checking for null values
            if y['cnt'].isnull().sum() > 0:
                print("Taking care of null values of cnt column")
                y = y.fillna(y.mean())

            if x['temp'].isnull().sum() > 0:
                print("Taking care of null values of temp column")
                x = x.fillna(x.mean())

            # Feature Scaling
            scx = StandardScaler()
            x = scx.fit_transform(x)

            # Splitting data into training and test set
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

            # Fitting training data into model
            dc_regression = DecisionTreeRegressor()
            dc_regression.fit(x_train, y_train)

            # Using model to predict test data
            y_pred = dc_regression.predict(x_test)

            # Calculating accuracy
            accuracy = r2_score(y_test, y_pred)
            print("Accuracy from model is : ", accuracy)

            # Dumping model into pickle

            if accuracy > 0.8:
                file_name = '../Model/DecisionTreeRegression_bike.pkl'
                pkl_file = open('../Model/DecisionTreeRegression_bike.pkl', 'wb')
                pkl_model = pickle.dump(dc_regression, pkl_file)

                # Load model from pickle and use same to predict test values
                pkl_file = open('../Model/DecisionTreeRegression_bike.pkl', 'rb')
                pkl_model = pickle.load(pkl_file)

                dataset_testdata = pd.read_csv('../Dataset/test_data.csv')
                x_testdata = dataset_testdata.iloc[:, [x1_index]]
                y_testdata = dataset_testdata.iloc[:, y_index:(y_index + 1)]

                y_pred = pkl_model.predict(x_testdata)
                accuracy_pkl = r2_score(y_testdata, y_pred)
                print("Accuracy by pickle model ", accuracy_pkl)

            # Visualising the Decision Tree Regression Training data set
            x_grid = np.arange(min(x_train), max(x_train), 0.01)
            x_grid = x_grid.reshape((len(x_grid), 1))

            plt.scatter(x_train, y_train, color='yellow')
            plt.plot(x_grid, dc_regression.predict(x_grid), color='blue')
            plt.title('Decision Tree Regression Train Set')
            plt.xlabel('Position')
            plt.ylabel('Salary')
            plt.show()

            # Visualising the Decision Tree Regression Test set
            X_grid_test = np.arange(min(x_test), max(x_test), 0.003)
            X_grid_test = X_grid_test.reshape((len(X_grid_test), 1))

            plt.scatter(x_test, y_test, color='red')
            plt.plot(X_grid_test, dc_regression.predict(X_grid_test), color='blue')
            plt.title('Decision Tree Regression Test Set')
            plt.xlabel('Position')
            plt.ylabel('Salary')
            plt.show()

    except FileNotFoundError:
        print("File Not Found Error")


Bikepred.bike_pred()






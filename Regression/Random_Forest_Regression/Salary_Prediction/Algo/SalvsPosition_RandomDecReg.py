# Random Forest Regression
# Importing libraries

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np
import matplotlib.pyplot as plt


class SalVsPositionRF:
    try:
        @staticmethod
        def SalVsPosition_RF():
            # Importing dataset

            """
             :Data Preprocessing start:
            """

            dataSet = pd.read_csv('../Dataset/Position_Salaries.csv')
            length_old = len(dataSet.columns)

            # Handling categorical data

            positions = pd.get_dummies(dataSet['Position'])
            dataSet = dataSet.drop('Position', axis=1)
            dataSet = pd.concat([dataSet, positions], axis=1)

            # Splitting dataset into 2 different csv files
            df_training = dataSet.sample(frac=0.8)
            df_test = pd.concat([dataSet, df_training]).drop_duplicates(keep=False)

            df_training.to_csv('../Dataset/training_data.csv', header=True, index=None)
            df_test.to_csv('../Dataset/test_data.csv', header=True, index=None)

            dataSet = pd.read_csv('../Dataset/training_data.csv')

            length_new = len(dataSet.columns)
            y_index = dataSet.columns.get_loc("Salary")

            y = dataSet.iloc[:, y_index:(y_index + 1)]
            x = dataSet.iloc[:, (length_old - 1):length_new]

            # Checking for null values
            if y['Salary'].isnull().sum() > 0:
                print("Taking care of null values of Salary column")
                y = y.fillna(y.mean())

            # Feature scaling
            scx = StandardScaler()
            x = scx.fit_transform(x)

            # Splitting data into training and test set
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

            """
            :Data Preprocessing start:
            
            """

            # Fitting training data into model
            rd_regression = RandomForestRegressor(n_estimators=10, random_state=0)
            rd_regression.fit(x_train, y_train.values.ravel())

            # Using model to predict test data
            y_pred = rd_regression.predict(x_test)

            # Calculating accuracy
            accuracy = r2_score(y_test, y_pred)
            print("Accuracy from model is : ", accuracy)

            # Dumping model into pickle
            if accuracy > 0.8:
                file_name = '../Model/RandomForestRegression.pkl'
                pkl_file = open(file_name, 'wb')
                model = pickle.dump(rd_regression, pkl_file)

                # Loading pickle model to predict data from test_data.csv file
                pkl_file = open(file_name, 'rb')
                model_pkl = pickle.load(pkl_file)

                dataSet_testdata = pd.read_csv('../Dataset/test_data.csv')

                x_testdata = dataSet_testdata.iloc[:, (length_old - 1):length_new]
                y_testdata = dataSet_testdata.iloc[:, y_index:(y_index + 1)]

                y_pred_pkl = model_pkl.predict(x_testdata)

                # Calculating accuracy from pickle model
                accuracy_pk = r2_score(y_testdata, y_pred_pkl)
                print("Accuracy by pickle model ", accuracy_pk)

                # Plotting the Decision Tree Regression Training data set
                x_grid = np.arange(min(x_train), max(x_train), 0.01)
                x_grid = x_grid.reshape((len(x_grid), 1))

                plt.scatter(x_train, y_train, color='yellow')
                plt.plot(x_grid, rd_regression.predict(x_grid), color='blue')
                plt.title('Random Forest Regression Train Set')
                plt.xlabel('Position')
                plt.ylabel('Salary')
                plt.show()

                # Plotting the Decision Tree Regression Test set
                x_grid_test = np.arange(min(x_test), max(x_test), 0.003)
                x_grid_test = x_grid_test.reshape((len(x_grid_test), 1))

                plt.scatter(x_test, y_test, color='red')
                plt.plot(x_grid_test, rd_regression.predict(x_grid_test), color='blue')
                plt.title('Random Forest Regression Test Set')
                plt.xlabel('Position')
                plt.ylabel('Salary')
                plt.show()

    except FileNotFoundError:
        print("FileNotFoundError")


SalVsPositionRF.SalVsPosition_RF()

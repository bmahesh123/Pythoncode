# Importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np
from matplotlib import pyplot as plt


class SalaryPred:

    try:
        def Salary_Pred():

            # data preprocessing Start

            # Importing dataset
            csv_dataSet = pd.read_csv('../Dataset/Position_Salaries.csv')
            df_training = csv_dataSet.sample(frac=0.8)
            df_test = pd.concat([csv_dataSet, df_training]).drop_duplicates(keep=False)

            # Spliting Dataset into two set Train and Test set and stored into Dirc

            df_training.to_csv('../Dataset/training_data.csv', header=True, index=None)
            df_test.to_csv('../Dataset/test_data.csv', header=True, index=None)

            csv_dataSet = pd.read_csv('../Dataset/training_data.csv')
            x_index = csv_dataSet.columns.get_loc("Level")
            y_index = csv_dataSet.columns.get_loc("Salary")

            x = csv_dataSet.iloc[:, x_index:(x_index + 1)]
            y = csv_dataSet.iloc[:, y_index:(y_index + 1)]

            # Checking for null values
            if y['Salary'].isnull().sum() > 0:
                print("Taking care of null values of Salary column")
                y = y.fillna(y.mean())

            if x['Level'].isnull().sum() > 0:
                print("Taking care of null values of Level column")
                x = x.fillna(x.mean())

            # Feature scaling
            scx = StandardScaler()
            x = scx.fit_transform(x)

            # Splitting data into training and test set
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

            # data preprocessing end

            # Fitting training data
            dc_regression = DecisionTreeRegressor()
            dc_regression.fit(x_train, y_train)

            # Using model to predict test data
            y_pred = dc_regression.predict(x_test)

            # Calculating accuracy
            accuracy = r2_score(y_test, y_pred)
            print("Accuracy from model is : ", accuracy)

            # Dumping model into pickle
            if accuracy > 0.9:
                file_name = '../Model/DecisionTreeRegression.pkl'
                pkl_file = open(file_name, 'wb')
                model = pickle.dump(dc_regression, pkl_file)

                # Loading pickle model to predict data from test_data.csv file
                pkl_file = open(file_name, 'rb')
                model_pkl = pickle.load(pkl_file)

                dataSet_testdata = pd.read_csv('../Dataset/test_data.csv')

                x_testdata = dataSet_testdata.iloc[:, x_index:(x_index + 1)]
                y_testdata = dataSet_testdata.iloc[:, y_index:(y_index + 1)]

                y_pred_pkl = model_pkl.predict(x_testdata)

                # Calculating accuracy from pickle model
                accuracy_pk = r2_score(y_testdata, y_pred_pkl)
                print("Accuracy by pickle model ", accuracy_pk)

            # Visualising the Decision Tree Regression Training data set
            x_grid = np.arange(min(x_train), max(x_train), 0.01)
            x_grid = x_grid.reshape((len(x_grid), 1))

            plt.scatter(x_train, y_train, color='red')
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


SalaryPred.Salary_Pred()



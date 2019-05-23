# Importing libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import pickle
import numpy as np
import matplotlib.pyplot as plt


class BikesRandomForestReg:
    try:
        @staticmethod
        def Bikes_RandomForestReg():

            """
            :Data Preprocessing start:
            """
            # Importing dataset

            csv_dataSet = pd.read_csv('../Dataset/bike_sharing.csv')
            df_training = csv_dataSet.sample(frac=0.8)
            df_test = pd.concat([csv_dataSet, df_training]).drop_duplicates(keep=False)

            # Spilt dataset into Train and Test dataset
            df_training.to_csv('../Dataset/training_data.csv', header=True, index=None)
            df_test.to_csv('../Dataset/test_data.csv', header=True, index=None)

            csv_dataSet = pd.read_csv('../Dataset/training_data.csv')
            x1_index = csv_dataSet.columns.get_loc("temp")
            x2_index = csv_dataSet.columns.get_loc("atemp")
            x3_index = csv_dataSet.columns.get_loc("hum")
            x4_index = csv_dataSet.columns.get_loc("windspeed")
            y_index = csv_dataSet.columns.get_loc("cnt")

            x = csv_dataSet.iloc[:, [x1_index, x2_index, x3_index, x4_index]]
            y = csv_dataSet.iloc[:, y_index:(y_index + 1)]

            # Checking for null values
            if y['cnt'].isnull().sum() > 0:
                print("Taking care of null values of cnt column")
                y = y.fillna(y.mean())

            for c in x.columns:
                if x[c].isnull().sum() > 0:
                    print("Taking care of null values of temp column")
                    x[c] = x[c].fillna(x.mean())

            # Feature scaling
            sc_x = StandardScaler()
            x = sc_x.fit_transform(x)

            # Splitting dataset into training and test dataset
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

            """ 
            :Data Preprocessing End: 
            """

            # Fitting model
            rd_regression = RandomForestRegressor(n_estimators=10)
            rd_regression.fit(x_train, y_train.values.ravel())

            # Predicting values of test data
            y_pred = rd_regression.predict(x_test)

            # Calculating accuracy of trained model
            accuracy = r2_score(y_test, y_pred)
            print("Accuracy of model ", accuracy)

            # Saving model into pickle file
            if accuracy > 0.8:
                file_name = '../Model/randomForestRegression.pkl'
                pkl_file = open(file_name, 'wb')
                model = pickle.dump(rd_regression, pkl_file)
                pkl_file.close()

                # Load pickle model to predict data
                pkl_file = open(file_name, 'rb')
                model = pickle.load(pkl_file)

                # Read data, Predict y values and calculate accuracy
                test_dataSet = pd.read_csv('../Dataset/test_data.csv')
                x_testdata = test_dataSet.iloc[:, [x1_index, x2_index, x3_index, x4_index]]
                y_testdata = test_dataSet.iloc[:, y_index:(y_index + 1)]

                y_pred = model.predict(x_testdata)
                accuracy_pkl = r2_score(y_testdata, y_pred)

                print("Accuracy by pickle model ", accuracy_pkl)

                # Plotting the Decision Tree Regression Training data set
                x_grid = np.logical_or(min(x_train), max(x_train))
                x_grid = x_grid.reshape((len(x_grid), 1))

                plt.scatter(x_train, y_train, color='yellow')
                plt.plot(x_grid, rd_regression.predict(x_grid), color='blue')
                plt.title('Random Forest Regression Train Set')
                plt.xlabel('Temp X-Axis')
                plt.ylabel('Bike Shared')
                plt.show()

                # # Plotting the Decision Tree Regression Test set
                x_grid_test = np.logical_or(min(x_test), max(x_test), 0.003)
                x_grid_test = x_grid_test.reshape((len(x_grid_test), 1))

                plt.scatter(x_test, y_test, color='red')
                plt.plot(x_grid_test, rd_regression.predict(x_grid_test), color='blue')
                plt.title('Random Forest Regression Test Set')
                plt.xlabel('Temp X-Axis')
                plt.ylabel('Bike Shared')
                plt.show()

    except FileNotFoundError:
        print("FileNotFoundError")


BikesRandomForestReg.Bikes_RandomForestReg()



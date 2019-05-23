# Support Vector Regression
# Importing the libraries
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.svm import SVR
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

class SalVsPosition_SupportVectorRegression:
    try:
        @staticmethod
        def SalVsPosition_Support_Vector_Reg():
            # Importing the dataset
            dataset = pd.read_csv('../Dataset/Position_Salaries.csv')
            X = dataset.iloc[:, :1].values
            y = dataset.iloc[:, 2].values

            # Encoding categorical data using label encoding

            label_encoder = LabelEncoder()
            X[:, 0] = label_encoder.fit_transform(X[:, 0])

            # Feature Scaling
            from sklearn.preprocessing import StandardScaler
            sc_X = StandardScaler()
            sc_y = StandardScaler()
            X = sc_X.fit_transform(X)
            # y = y.reshape(-1, 1)
            y = np.array(y).reshape((len(y), 1))
            y = sc_y.fit_transform(y)

            # Splitting the dataset into the Training set and Test set
            from sklearn.model_selection import train_test_split
            x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

            # RBF model
            svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
            svr_rbf.fit(x_train, y_train)
            y_pred = svr_rbf.predict(x_test)
            print("Accuracy for rbf: ", r2_score(y_test, y_pred))

            # Linear model
            svr_lin = SVR(kernel='linear', C=1e3)
            svr_lin.fit(x_train, y_train)
            y_pred = svr_lin.predict(x_test)
            print("Accuracy for linear: ", r2_score(y_test, y_pred))

            # Polynomial model
            svr_poly = SVR(kernel='poly', C=1e3, degree=2)
            svr_poly.fit(x_train, y_train)
            y_pred = svr_poly.predict(x_test)
            print("Accuracy for poly: ", r2_score(y_test, y_pred))

            # Visualising the SVR results (for higher resolution and smoother curve) for Train data set
            x_grid = np.arange(min(x_train), max(x_train), 0.01)
            x_grid = x_grid.reshape((len(x_grid), 1))
            plt.scatter(x_train, y_train, color='black')
            plt.plot(x_grid, svr_rbf.predict(x_grid), color='red', label='Radial Basis')
            plt.plot(x_grid, svr_lin.predict(x_grid), color='blue', linestyle='-', label='Linear Model')
            plt.plot(x_grid, svr_poly.predict(x_grid), color='green', linestyle='--', label='Poly')
            plt.title('Position vs Salary (SVR)')
            plt.xlabel('Position level')
            plt.ylabel('Salary')
            plt.show()

            # Visualising the SVR results (for higher resolution and smoother curve) for Test data set
            x_grid = np.arange(min(x_test), max(x_test), 0.01)
            x_grid = x_grid.reshape((len(x_grid), 1))
            plt.scatter(x_test, y_test, color='red')
            plt.plot(x_grid, svr_rbf.predict(x_grid), color='red')
            plt.plot(x_grid, svr_lin.predict(x_grid), color='blue')
            plt.plot(x_grid, svr_poly.predict(x_grid), color='green')
            plt.title('Position vs Salary (SVR)')
            plt.xlabel('Position level')
            plt.ylabel('Salary')
            plt.show()

    except FileNotFoundError:
        print("FileNotFoundError")


SalVsPosition_SupportVectorRegression.SalVsPosition_Support_Vector_Reg()



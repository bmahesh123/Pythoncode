# Simple Linear Regression
# Data Preprocessing Start

# importing library
import pandas as pd
import matplotlib.pyplot as plt


class Salary_Predection_Lin_Regression:
    @staticmethod
    def salary_prediction():

        # Importing dataset
        csv_dataset = pd.read_csv('Salary_Data.csv')
        print(csv_dataset.head())

        x_data = csv_dataset.iloc[:, :-1].values
        y_data = csv_dataset.iloc[:, 1].values

        # Spliting Dataset into Training set and Test set
        from sklearn.model_selection import train_test_split
        x_train_data, x_test, y_train_data, y_test = train_test_split(x_data, y_data, test_size=1/3, random_state = 0)

        # Data Preprocessing End

       # Fitting Simple Linear Regression model to the Training set
        from sklearn.linear_model import LinearRegression
        lin_obj = LinearRegression()
        lin_obj.fit(x_train_data, y_train_data)

        # Predicting the Test_set results
        predication = lin_obj.predict(x_test)
        print("Predicated Data: ")
        print(predication)


        plt.scatter(x_train_data, y_train_data, color='purple')
        plt.plot(x_train_data, lin_obj.predict(x_train_data), color='red')
        plt.title('Salary & Experience (Training set)')
        plt.xlabel('Experience in Year')
        plt.ylabel('Salary Range')
        plt.show()

        # Plotting Test set results
        plt.scatter(x_test, y_test, color='red')
        plt.plot(x_train_data, lin_obj.predict(x_train_data), color='blue')
        plt.title('Salary & Experience (Predicated set / Test set)')
        plt.xlabel('Experience in Year')
        plt.ylabel('Salary Range')
        plt.show()


Salary_Predection_Lin_Regression.salary_prediction()





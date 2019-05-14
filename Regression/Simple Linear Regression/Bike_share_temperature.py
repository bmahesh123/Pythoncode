# Simple Linear Regression
# Data Preprocessing Start

# import Library

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Bike_share_temp_Lin_Regression:

    def bike_share_temp(self):

        # Importing dataset
        bike_dataset = pd.read_csv('bike_sharing.csv')
        datafram = pd.DataFrame(bike_dataset)

        x_data = (datafram[['temp']])
        y_data = (datafram[['cnt']])

        # Spliting Dataset into Training set and Test set
        from sklearn.model_selection import train_test_split
        x_train_data, x_test, y_train_data, y_test = train_test_split(x_data, y_data, test_size=1/3, random_state=0)

        # Data Preprocessing End

        # Fitting Simple Linear Regression model to the Training set
        from sklearn.linear_model import LinearRegression
        lin_obj1 = LinearRegression()
        lin_obj1.fit(x_train_data, y_train_data)

        # Predicting the Test_set results
        predication1 = lin_obj1.predict(x_test)
        print("Prediction Data:")
        print(predication1)

        # Plotting Training set results
        plt.scatter(x_train_data, y_train_data, color = 'yellow')
        plt.plot(x_train_data, lin_obj1.predict(x_train_data), color = 'red')
        plt.title('Bikes Shared Based On The Temp(Training set)')
        plt.xlabel('Temperature of the day- x Axis')
        plt.ylabel('Number of Bikes Shared- Y Axis')
        plt.show()

        # Plotting Test set results
        plt.scatter(x_test, y_test, color='red')
        plt.plot(x_train_data, lin_obj1.predict(x_train_data), color='blue')
        plt.title('Bikes Shared Based On The Temp(Predicated set/Test set)')
        plt.xlabel('Temperature of the day- x Axis')
        plt.ylabel('Number of Bikes Shared- Y Axis')
        plt.show()


obj = Bike_share_temp_Lin_Regression()
obj.bike_share_temp()




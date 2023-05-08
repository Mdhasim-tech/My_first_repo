'''import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error

linnerud=datasets.load_linnerud()
linnerud_x=linnerud.data[:,np.newaxis,2]



linnerud_x_train=linnerud_x[:-10]
linnerud_x_test=linnerud_x[-10:]
print(len(linnerud_x_test))

linnerud_y_train=linnerud.target[:-10]
linnerud_y_test=linnerud.target[-10:]
print(len(linnerud_y_test))

model=linear_model.LinearRegression()
model.fit(linnerud_x_train,linnerud_y_train)

linnerud_y_predicted=model.predict(linnerud_x_test)
print(linnerud_y_predicted)
plt.scatter(linnerud_x_test,linnerud_y_test)
plt.plot(linnerud_x_test,linnerud_y_predicted)
plt.show()'''

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error

diabetes=datasets.load_diabetes()

'''print(diabetes)
print(diabetes.keys())
print(diabetes.DESCR)'''
diabetes_x=diabetes.data[:,np.newaxis,2]

diabetes_x_train=diabetes_x[:-30]
diabetes_x_test=diabetes_x[-30:]

diabetes_y_train=diabetes.target[:-30]
print(diabetes_y_train)
diabetes_y_test=diabetes.target[-30:]
print(diabetes_y_test)

model=linear_model.LinearRegression()
model.fit(diabetes_x_train,diabetes_y_train)

#training is done,model is ready,now testing the model

diabetes_y_predicted= model.predict(diabetes_x_test)
print(diabetes_y_predicted)
print("Mean squared error is:", mean_squared_error(diabetes_y_test,diabetes_y_predicted))
print("weights:",model.coef_)
print("intercept:",model.intercept_)

plt.scatter(diabetes_x_test,diabetes_y_test)
plt.plot(diabetes_x_test,diabetes_y_predicted)
plt.show()
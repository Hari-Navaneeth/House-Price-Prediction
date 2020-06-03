#Importing Required Library
import tensorflow as tf
import numpy as np
from tensorflow import keras

#Creation of Model begins here
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

#Getting Required Inputs
number=int(input("Enter Number of Sample Houses : "))
while(number<5):
    number=int(input("Enter atleast 5 Sample Houses : "))
no_of_rooms=[]
house_price=[]
print("==============================================================================")
for i in range(1,number+1):
    print("Enter House",i,":")
    no_of_rooms.append(float(input(" Number of Rooms : ")))
    house_price.append(float(input(" House Price     : ")))
    print("==============================================================================")

#Model Training
print("Wait for Few Seconds to Train a Model......")
Rooms_in_House = np.array(no_of_rooms, dtype=float)
Price_of_House = np.array(house_price, dtype=float)
model.fit(Rooms_in_House, Price_of_House, epochs=1000)
print("==============================================================================")

#Prediction takes place here
predict_input=float(input("Enter number rooms required in your house : "))
print(*model.predict([predict_input]))
print("==============================================================================")

#Done Happy Coding

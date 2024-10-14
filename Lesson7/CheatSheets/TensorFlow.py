# ============================
# TensorFlow Cheat Sheet
# Advanced machine learning and deep learning.
# ============================

import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
import numpy as np

# ============================
# TensorFlow Basics
# ============================

# Creating a Tensor
tensor = tf.constant([[1, 2], [3, 4]])
print(tensor)

# Creating Tensors from NumPy arrays
numpy_array = np.array([[1, 2], [3, 4]])
tensor_from_numpy = tf.convert_to_tensor(numpy_array)
print(tensor_from_numpy)

# Tensor Operations
x = tf.constant([5, 6, 7])
y = tf.constant([1, 2, 3])

add = tf.add(x, y)  # Addition
subtract = tf.subtract(x, y)  # Subtraction
multiply = tf.multiply(x, y)  # Element-wise multiplication

print(add, subtract, multiply)

# ============================
# GPU/CPU Device Management
# ============================

# Check for GPU availability
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

# Explicitly specify device
with tf.device('/CPU:0'):
    tensor_cpu = tf.random.uniform([2, 2])

with tf.device('/GPU:0'):
    tensor_gpu = tf.random.uniform([2, 2])

print(tensor_cpu)
print(tensor_gpu)

# ============================
# Building a Neural Network (Sequential API)
# ============================

# Define a Sequential model
model = models.Sequential()

# Add layers
model.add(layers.Dense(64, activation='relu', input_shape=(32,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# ============================
# Building a Neural Network (Functional API)
# ============================

# Input layer
inputs = tf.keras.Input(shape=(32,))
x = layers.Dense(64, activation='relu')(inputs)
x = layers.Dense(64, activation='relu')(x)
outputs = layers.Dense(10, activation='softmax')(x)

# Define the model
functional_model = models.Model(inputs=inputs, outputs=outputs)

# Compile the model
functional_model.compile(optimizer='adam',
                         loss='sparse_categorical_crossentropy',
                         metrics=['accuracy'])

# ============================
# Training and Evaluation
# ============================

# Generate random data
X_train = np.random.random((1000, 32))
y_train = np.random.randint(10, size=(1000,))

# Train the model
history = model.fit(X_train, y_train, epochs=10, batch_size=32)

# Evaluate the model on test data
X_test = np.random.random((200, 32))
y_test = np.random.randint(10, size=(200,))
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss}, Test Accuracy: {accuracy}")

# ============================
# Making Predictions
# ============================

# Making predictions on new data
predictions = model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)
print(predicted_classes)

# ============================
# Callbacks (Early Stopping, Model Checkpointing)
# ============================

from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Early stopping to prevent overfitting
early_stopping = EarlyStopping(monitor='val_loss', patience=3)

# Save the best model during training
checkpoint = ModelCheckpoint('best_model.h5', save_best_only=True, monitor='val_loss')

# Re-train the model with callbacks
history = model.fit(X_train, y_train, epochs=10, batch_size=32,
                    validation_split=0.2, callbacks=[early_stopping, checkpoint])

# ============================
# Custom Loss Functions
# ============================

# Define a custom loss function
def custom_loss(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))

# Compile model with custom loss
model.compile(optimizer='adam', loss=custom_loss)

# Train the model with the custom loss
model.fit(X_train, y_train, epochs=10, batch_size=32)

# ============================
# Save and Load Models
# ============================

# Save the entire model
model.save('my_model.h5')

# Load the saved model
loaded_model = models.load_model('my_model.h5')

# ============================
# Preprocessing Data (Using tf.data API)
# ============================

# Creating a Dataset from NumPy arrays
dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))

# Shuffle and batch the dataset
dataset = dataset.shuffle(buffer_size=1024).batch(32)

# Iterating through the dataset
for batch in dataset:
    print(batch)

# ============================
# Data Augmentation (Image Data)
# ============================

from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Create an ImageDataGenerator for augmenting images
datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Fit the generator on a dataset
datagen.fit(X_train.reshape(-1, 32, 32, 1))  # Assuming X_train is image data

# Use the generator to augment data during training
model.fit(datagen.flow(X_train, y_train, batch_size=32), epochs=10)

# ============================
# TensorBoard for Visualization
# ============================

from tensorflow.keras.callbacks import TensorBoard

# Set up TensorBoard callback
tensorboard = TensorBoard(log_dir='./logs')

# Train the model with TensorBoard
history = model.fit(X_train, y_train, epochs=10, batch_size=32, callbacks=[tensorboard])

# To view TensorBoard, run the following in the terminal:
# tensorboard --logdir=./logs

# ============================
# End of Cheat Sheet
# ============================
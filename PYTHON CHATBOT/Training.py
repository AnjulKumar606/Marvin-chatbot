# Import necessary libraries
import random
import json
import pickle
import numpy as np
import tensorflow as tf

# Import NLTK and initialize the WordNet lemmatizer
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Load the intents JSON file
intents = json.loads(open('student.json').read())

# Initialize lists for words, classes, and documents
words = []
classes = []
documents = []
ignoreLetters = ['?', '!', '.', ',']

# Iterate through intents and patterns to collect words and build documents
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize words from the pattern
        wordList = nltk.word_tokenize(pattern)
        # Extend words list with tokenized words
        words.extend(wordList)
        # Append document as a tuple of words and intent tag
        documents.append((wordList, intent['tag']))
        # Add intent tag to classes if not already present
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize and clean words, then sort and remove duplicates
words = [lemmatizer.lemmatize(word) for word in words if word not in ignoreLetters]
words = sorted(set(words))

# Sort classes alphabetically
classes = sorted(set(classes))

# Save words and classes to pickle files for later use
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Initialize training data and create bag of words and output rows
training = []
outputEmpty = [0] * len(classes)

# Loop through documents to create training data
for document in documents:
    bag = []
    wordPatterns = document[0]
    wordPatterns = [lemmatizer.lemmatize(word.lower()) for word in wordPatterns]
    for word in words:
        bag.append(1) if word in wordPatterns else bag.append(0)
    
    # Create an output row with 0s, and set the correct class to 1
    outputRow = list(outputEmpty)
    outputRow[classes.index(document[1])] = 1
    
    # Append bag of words and output row to training data
    training.append(bag + outputRow)

# Shuffle the training data and convert it to a numpy array
random.shuffle(training)
training = np.array(training)

# Split training data into input (X) and output (Y)
trainX = training[:, :len(words)]
trainY = training[:, len(words):]

# Create a sequential neural network model
# Create a Sequential model
model = tf.keras.Sequential()

# Add a Dense (fully connected) layer with 128 units/neurons
# Input shape is determined by the number of features in trainX (the length of each input vector)
# Activation function 'relu' (Rectified Linear Unit) is used for non-linearity
model.add(tf.keras.layers.Dense(128, input_shape=(len(trainX[0]),), activation='relu'))

# Add a Dropout layer with a dropout rate of 0.5
# Dropout helps prevent overfitting by randomly deactivating 50% of the neurons during training
model.add(tf.keras.layers.Dropout(0.5))

# Add another Dense layer with 64 units/neurons
# Activation function 'relu' is used again for non-linearity
model.add(tf.keras.layers.Dense(64, activation='relu'))

# Add another Dropout layer with a dropout rate of 0.5
model.add(tf.keras.layers.Dropout(0.5))

# Add the output layer with units equal to the number of classes in trainY
# Activation function 'softmax' is used for multi-class classification
model.add(tf.keras.layers.Dense(len(trainY[0]), activation='softmax'))


# Define the stochastic gradient descent optimizer
sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)

# Compile the model with categorical cross-entropy loss and accuracy metric
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train the model with the training data
model.fit(trainX, trainY, epochs=200, batch_size=5, verbose=1)

# Save the trained model to a file
model.save('chatbot_model.h5')

# Print a message indicating that the process is done
print('Done')

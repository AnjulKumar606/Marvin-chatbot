# Import necessary libraries
import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

# Initialize the WordNet lemmatizer for word normalization
lemmatizer = WordNetLemmatizer()

# Load the intents from a JSON file
intents = json.loads(open('student.json').read())

# Load preprocessed data: words, classes, and the trained chatbot model
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')

# Define a function to clean up a sentence
def clean_up_sentence(sentence):
    # Tokenize the sentence into individual words
    sentence_words = nltk.word_tokenize(sentence)
    
    # Lemmatize each word to its base form for better understanding
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    
    return sentence_words

# Define a function to create a bag of words from a sentence
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    
    # Initialize an empty array for the bag of words
    bag = [0] * len(words)
    
    # Mark the presence of words in the bag
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    
    return np.array(bag)

# Define a function to predict the intent of a sentence
def predict_class(sentence):
    # Convert the sentence into a bag of words
    bow = bag_of_words(sentence)
    
    # Use the trained model to make predictions
    res = model.predict(np.array([bow]))[0]
    
    # Set a threshold for prediction confidence
    ERROR_THRESHOLD = 0.25
    
    # Filter out predictions below the threshold
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    
    # Sort predictions by confidence, highest first
    results.sort(key=lambda x: x[1], reverse=True)
    
    # Create a list of predicted intents with probabilities
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    
    return return_list

# Define a function to get a response based on the predicted intent
def get_response(intents_list, intent_json):
    # Get the predicted intent tag
    tag = intents_list[0]['intent']
    
    # Find the corresponding response options in the intents JSON
    list_of_intents = intent_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            # Randomly select a response from the available options
            result = random.choice(i['responses'])
            break
    
    return result

# Main entry point
print("The ChatBot is running!")

# Main interaction loop
while True:
    # Get user input
    message = input("")
    
    # Predict the intent of the user's message
    ints = predict_class(message)
    
    # Get a response based on the predicted intent
    res = get_response(ints, intents)
    
    # Print the chatbot's response
    print(res)

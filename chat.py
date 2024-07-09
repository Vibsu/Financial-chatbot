import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json
import pickle

# Load the model
model = tf.keras.models.load_model('chatbot_model.h5')

# Load the tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Load the intents dataset
with open('intents.json') as file:
    data = json.load(file)

# Create tag mappings
tag_to_index = {}
index_to_tag = {}
for i, intent in enumerate(data['intents']):
    tag = intent['tag']
    tag_to_index[tag] = i
    index_to_tag[i] = tag

# Function to get response
def get_response(text):
    # Tokenize and pad the input
    input_sequence = tokenizer.texts_to_sequences([text])
    input_padded = pad_sequences(input_sequence, maxlen=model.input_shape[1])

    # Make a prediction
    prediction = model.predict(input_padded)[0]

    # Get the predicted tag
    predicted_tag_index = tf.argmax(prediction).numpy()
    predicted_tag = index_to_tag[predicted_tag_index]
    print(predicted_tag)

    # Get the response for the predicted tag
   # response = [intent['responses'][0] for intent in data['intents'] if intent['tag'] == predicted_tag][0]
    response = data['intents'][tag_to_index[predicted_tag]]['responses']

    print(response)
    import random
    random_sentence = random.choice(response)
    print(random_sentence)
    return random_sentence,predicted_tag


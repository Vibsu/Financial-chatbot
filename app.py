# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd
import csv
import requests 
import config
import pickle
import io
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from chat import get_response
import os

from flask import Flask, render_template, request, redirect, url_for,Markup
import sounddevice as sd
import numpy as np
import librosa
from flask import Flask, render_template, request, redirect, url_for
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write, read
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import speech_recognition as sr




import joblib
import numpy as np;
import pandas as pd;
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
gmail_list=[]
password_list=[]
gmail_list1=[]
password_list1=[]
import numpy as np;
import pandas as pd;
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
import random



import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np;
import pandas as pd;
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle


# ------------------------------------ FLASK APP -------------------------------------------------
import random
import string

# Generate three random alphabets
random_alphabets = ''.join(random.choices(string.ascii_uppercase, k=3))

# Generate three random integers
random_integers = ''.join(random.choices(string.digits, k=3))

# Combine alphabets and integers
random_combination = random_alphabets + random_integers

print(random_combination)



app = Flask(__name__)

# render home page
def convert_to_international_number(salary):
    # Remove the last word from the salary string ("lakh")
    salary = salary[:-5]
    # Convert the remaining string to an integer and multiply by 100,000
    return int(salary) * 100000
# Function to initialize or load chat history
def load_chat_history():
    chat_history = []
    file_path = 'chat_history.csv'

    if os.path.exists(file_path):
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                chat_history.append({'random_combination':[0],'user_message': row[1], 'bot_response': row[2]})

    return chat_history

def load_chat_history2(target_combination):
    chat_history = []
    file_path = 'chat_history.csv'

    if os.path.exists(file_path):
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                # Assuming the 'random_combination' field is in the second column (index 1)
                if len(row) > 1 and row[0] == target_combination:
                    chat_history.append({'random_combination': [0], 'user_message': row[1], 'bot_response': row[2]})

    return chat_history

# Function to save a new message to the chat history
def save_to_chat_history(random_combination,user_message, bot_response):
    file_path = 'chat_history.csv'

    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([random_combination,user_message, bot_response])
#@ app.route('/')
#def home():
#    title = 'Coalbot'
#    return render_template('index4.html', title=title)

# render crop recommendation form page
@app.route('/')
def home():
    return render_template('index5.html') 

@app.route('/logedin',methods=['POST'])
def logedin():
    
    int_features3 = [str(x) for x in request.form.values()]
    print(int_features3)
    logu=int_features3[0]
    passw=int_features3[1]
   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root","","ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(gmail_list)
    

    cursor1= db.cursor()
    cursor1.execute("SELECT password FROM user_register")
    result2=cursor1.fetchall()
              #print(result1)
              #print(gmail1)
    for row2 in result2:
                      print(row2)
                      print(row2[0])
                      password_list.append(str(row2[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(password_list)
    print(gmail_list.index(logu))
    print(password_list.index(passw))
    
    if gmail_list.index(logu)==password_list.index(passw):
        return render_template('chatbot.html')
    else:
        return jsonify({'result':'use proper  gmail and password'})
                  
                                               



                          
                     # print(value1[0:])
    
    
    
    

              
              # int_features3[0]==12345 and int_features3[1]==12345:
               #                      return render_template('index.html')
        
@app.route('/register',methods=['POST'])
def register():
    

    int_features2 = [str(x) for x in request.form.values()]
    #print(int_features2)
    #print(int_features2[0])
    #print(int_features2[1])
    r1=int_features2[0]
    print(r1)
    
    r2=int_features2[1]
    print(r2)
    logu1=int_features2[0]
    passw1=int_features2[1]
        
    

    

   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root",'',"ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list1.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(gmail_list1)
    if logu1 in gmail_list1:
                      return jsonify({'result':'this gmail is already in use '})  
    else:

                  #return jsonify({'result':'this  gmail is not registered'})
              

# Prepare SQL query to INSERT a record into the database.
                  sql = "INSERT INTO user_register(user,password) VALUES (%s,%s)"
                  val = (r1, r2)
   
                  try:
   # Execute the SQL command
                                       cursor.execute(sql,val)
   # Commit your changes in the database
                                       db.commit()
                  except:
   # Rollback in case there is any error
                                       db.rollback()

# disconnect from server
                  db.close()
                 # return jsonify({'result':'succesfully registered'})
                  return render_template('login44.html')

                      



@app.route('/chatboat', methods=['GET', 'POST'])
def chatboat():
   
    return render_template('login44.html')


@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    # You can replace the next line with a call to an AI model for generating responses
    bot_response ,predicted_tag=get_response(user_message)

    if predicted_tag=="stock_market_investment":
              pr_text=user_message
              import re

              user_message = pr_text

              # Define a regular expression pattern to match the salary value
              pattern = r'\b\d+\s*lakh\b'

              # Use findall to extract all matches of the pattern from the string
              salary_matches = re.findall(pattern, user_message)

              # If there are matches, print them
              if salary_matches:
                  print("Salary:", salary_matches[0])
                  # Input salary in the Indian numbering system
                  salary = salary_matches[0]

                  # Convert to international numbering system
                  converted_salary = convert_to_international_number(salary)
              else:
                  print("No salary mentioned in the message.")

              random_float = random.uniform(0.10, 0.20)

              bot_response="You can invest "+str(converted_salary*random_float) +" to your stock market and also please check with few other parameters before you invest."


    elif predicted_tag=="home_loan_amount":
              pr_text=user_message
              import re

              user_message = pr_text

              # Define a regular expression pattern to match the salary value
              pattern = r'\b\d+\s*lakh\b'

              # Use findall to extract all matches of the pattern from the string
              salary_matches = re.findall(pattern, user_message)

              # If there are matches, print them
              if salary_matches:
                  print("Salary:", salary_matches[0])
                  # Input salary in the Indian numbering system
                  salary = salary_matches[0]

                  # Convert to international numbering system
                  converted_salary = convert_to_international_number(salary)
              else:
                  print("No salary mentioned in the message.")

              random_integer = random.randint(1,6)

              bot_response="You can have home loan of "+str(converted_salary*random_integer) +"  also please check other features before getting loans."

    elif predicted_tag=="car_loan_amount":
              pr_text=user_message
              import re

              user_message = pr_text

              # Define a regular expression pattern to match the salary value
              pattern = r'\b\d+\s*lakh\b'

              # Use findall to extract all matches of the pattern from the string
              salary_matches = re.findall(pattern, user_message)

              # If there are matches, print them
              if salary_matches:
                  print("Salary:", salary_matches[0])
                  # Input salary in the Indian numbering system
                  salary = salary_matches[0]

                  # Convert to international numbering system
                  converted_salary = convert_to_international_number(salary)
              else:
                  print("No salary mentioned in the message.")

              random_integer = random.randint(2,3)

              bot_response="You can have car  loan of "+str(converted_salary*random_integer) +"  also please check other features before getting loans."

    elif predicted_tag=="mobile_phone_affordability":
              pr_text=user_message
              import re

              user_message = pr_text

              # Define a regular expression pattern to match the salary value
              pattern = r'\b\d+\s*lakh\b'

              # Use findall to extract all matches of the pattern from the string
              salary_matches = re.findall(pattern, user_message)

              # If there are matches, print them
              if salary_matches:
                  print("Salary:", salary_matches[0])
                  # Input salary in the Indian numbering system
                  salary = salary_matches[0]

                  # Convert to international numbering system
                  converted_salary = convert_to_international_number(salary)
              else:
                  print("No salary mentioned in the message.")

              random_float = random.uniform(0.05, 0.15)

              bot_response="You can buy a Mobile phone worth nearly  "+str(converted_salary*random_float) +"  also please check the other futures ."

    elif predicted_tag=="general_expenditure":
              pr_text=user_message
              import re

              user_message = pr_text

              # Define a regular expression pattern to match the salary value
              pattern = r'\b\d+\s*lakh\b'

              # Use findall to extract all matches of the pattern from the string
              salary_matches = re.findall(pattern, user_message)

              # If there are matches, print them
              if salary_matches:
                  print("Salary:", salary_matches[0])
                  # Input salary in the Indian numbering system
                  salary = salary_matches[0]

                  # Convert to international numbering system
                  converted_salary = convert_to_international_number(salary)
              else:
                  print("No salary mentioned in the message.")

              random_float1 = random.uniform(0.10, 0.15)
              random_float2 = random.uniform(0.15, 0.20)
              random_float3 = random.uniform(0.20, 0.25)
              random_float4 = random.uniform(0.10, 0.12)
              random_float5 = random.uniform(0.10, 0.25)
              random_float6 = random.uniform(0.02, 0.05)
              #random_float5 = random.uniform(0.02, 0.05)


              bot_response="You can Devide it  like "+".for education you can have "+str(int(converted_salary*random_float1) )+". for health you can have "+str(int(converted_salary*random_float2))+".for housing you can use "+str(int(converted_salary*random_float3))+".for Savings/Investment you can use "+str(int(converted_salary*random_float4))+".for daily living expenses you can have "+str(int(converted_salary*random_float5))+".for Entertainment/Leisure you can have "+str(int(converted_salary*random_float6))




    else:
      bot_response=bot_response
      #print("a")
    #save_to_chat_history(random_combination,user_message, bot_response)

    #chat_history = load_chat_history2(random_combination)

  #  print("the random generated result is ",chat_history)





    # Extract 'bot_response' value
    #bot_response_value = chat_history[0]['bot_response']

    
    from gtts import gTTS
    from pydub import AudioSegment
    import pygame
    import os

    text = str(bot_response)
    language = 'en'

    try:
        # Create gTTS object
        tts = gTTS(text=text, lang=language, slow=False)

        # Save the converted audio in a file
        tts.save("output.mp3")
        print("Audio file saved successfully.")
    except Exception as e:
        print(f"Error: {e}")

    # Play the saved audio file using pygame
    try:
        # Initialize pygame mixer
        pygame.mixer.init()

        # Load the audio file
        pygame.mixer.music.load("output.mp3")

        # Play the audio file
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Adjust the tick value as needed

        # Close the mixer
        pygame.mixer.quit()

    except Exception as e:
        print(f"Error playing audio: {e}")
    

    from translate import Translator

    def translate_text(text, target_language):
        translator= Translator(to_lang=target_language)
        translation = translator.translate(text)
        return translation
   
    text_to_translate =bot_response
    # Translate to Kannada
    english_translation=text_to_translate
    kannada_translation = translate_text(text_to_translate, "kn")
    print(f"Kannada: {kannada_translation}")

    # Translate to Hindi
    hindi_translation = translate_text(text_to_translate, "hi")
    print(f"Hindi: {hindi_translation}")

    # Translate to Tamil
    tamil_translation = translate_text(text_to_translate, "ta")
    print(f"Tamil: {tamil_translation}")

    # Translate to Malayalam
    malayalam_translation = translate_text(text_to_translate, "ml")
    print(f"Malayalam: {malayalam_translation}")


    marathi_translation = translate_text(text_to_translate, "mr")
    print(f"marathi: {marathi_translation}")

    # Print the result
    #print("this is the text response for present question",loaded_data_yield)
    #return render_template('index.html', user_message=user_message, bot_response=bot_response)
    save_to_chat_history(random_combination,user_message, bot_response=text_to_translate)

    chat_history = load_chat_history2(random_combination)

    #bot_response_value = chat_history[0]['bot_response']

    return render_template('chatbot.html', user_message=user_message, bot_response=text_to_translate, chat_history=chat_history,kannada_translation=kannada_translation,hindi_translation=hindi_translation,tamil_translation=tamil_translation,malayalam_translation=malayalam_translation,english_translation=english_translation,marathi_translation=marathi_translation)



# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template,request
from pymongo import MongoClient
import sklearn
import pickle
import pandas as pd
import os

# import os
# import tensorflow as tf
# import numpy as np
# from tensorflow import keras
# from skimage import io
# from tensorflow.keras.preprocessing import image


# # Flask utils
# from flask import Flask, redirect, url_for, request, render_template
# from werkzeug.utils import secure_filename
# from gevent.pywsgi import WSGIServer

app=Flask("Hara Jeewan")

model = pickle.load(open("RFmodel.pkl", "rb"))
# model =tf.keras.models.load_model('PlantDNet.h5',compile=False)

# def model_predict(img_path, model):
#     img = image.load_img(img_path, grayscale=False, target_size=(64, 64))
#     show_img = image.load_img(img_path, grayscale=False, target_size=(64, 64))
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis=0)
#     x = np.array(x, 'float32')
#     x /= 255
#     preds = model.predict(x)
#     return preds


@app.route("/")
def front():
    return render_template("home.html")

@app.route("/cropinfo")
def cropinfo():
    return render_template("cropquery.html")

@app.route("/govt")
def govt():
    return render_template("govt.html")
    
@app.route("/tech")
def tech():
    return render_template("farmingtech.html")

@app.route("/crop_recom")
def crop_recom():
    return render_template("crop_recom.html")    

@app.route("/irrigation")
def irrigation():
    return render_template("modern_irrigation.html")   

# @app.route('/predict', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         # Get the file from post request
#         f = request.files['file']

#         # Save the file to ./uploads
#         basepath = os.path.dirname(__file__)
#         file_path = os.path.join(
#             basepath, 'uploads', secure_filename(f.filename))
#         f.save(file_path)

#         # Make prediction
#         preds = model_predict(file_path, model)
#         print(preds[0])

#         # x = x.reshape([64, 64]);
#         disease_class = ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy', 'Potato___Early_blight',
#                          'Potato___Late_blight', 'Potato___healthy', 'Tomato_Bacterial_spot', 'Tomato_Early_blight',
#                          'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot',
#                          'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot',
#                          'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus', 'Tomato_healthy']
#         a = preds[0]
#         ind=np.argmax(a)
#         print('Prediction:', disease_class[ind])
#         result=disease_class[ind]
#         return result
#     return None

@app.route("/login")
def login():
    return render_template("login.html")  

@app.route("/PM")
def PM():
    return render_template("PM.html")  
@app.route("/PM2")
def PM2():
    return render_template("PM2.html") 
@app.route("/PM3")
def PM3():
    return render_template("PM3.html")
@app.route("/PM4")
def PM4():
    return render_template("PM4.html")
@app.route("/organic")
def organic():
    return render_template("organic.html")  
@app.route("/tech1")
def tech1():
    return render_template("tech1.html")
@app.route("/tech2")
def tech2():
    return render_template("tech2.html")
@app.route("/tech3")
def tech3():
    return render_template("tech3.html")
@app.route("/tech4")
def tech4():
    return render_template("tech4.html") 
@app.route("/MIT1")
def MIT1():
    return render_template("MIT1.html")
@app.route("/MIT2")
def MIT2():
    return render_template("MIT2.html")  
@app.route("/MIT3")
def MIT3():
    return render_template("MIT3.html")  
@app.route("/MIT4")
def MIT4():
    return render_template("MIT4.html")                  
  
@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        
        # Nitrogen
        nitrogen = float(request.form["nitrogen"])
        
        # Phosphorus
        phosphorus = float(request.form["phosphorus"])
        
        # Potassium
        potassium = float(request.form["potassium"])
        
        # Temperature
        temperature = float(request.form["temperature"])
        
        # Humidity Level
        humidity = float(request.form["humidity"])
        
        # PH level
        phLevel = float(request.form["ph-level"])
        
        # Rainfall
        rainfall = float(request.form["rainfall"])
        
        # Making predictions from the values:
        predictions = model.predict([[nitrogen, phosphorus, potassium, temperature, humidity, phLevel, rainfall]])
        
        output = predictions[0]
        finalOutput = output.capitalize()
        
        if (output == "rice" or output == "blackgram" or output == "pomegranate" or output == "papaya"
            or output == "cotton" or output == "orange" or output == "coffee" or output == "chickpea"
            or output == "mothbeans" or output == "pigeonpeas" or output == "jute" or output == "mungbeans"
            or output == "lentil" or output == "maize" or output == "apple"):
            cropStatement = finalOutput + " should be harvested. It's a Kharif crop, so it must be sown at the beginning of the rainy season e.g between April and May."
                            

        elif (output == "muskmelon" or output == "kidneybeans" or output == "coconut" or output == "grapes" or output == "banana"):
            cropStatement = finalOutput + " should be harvested. It's a Rabi crop, so it must be sown at the end of monsoon and beginning of winter season e.g between September and October."
            
        elif (output == "watermelon"):
            cropStatement = finalOutput + " should be harvested. It's a Zaid Crop, so it must be sown between the Kharif and rabi season i.e between March and June."
        
        elif (output == "mango"):
            cropStatement = finalOutput + " should be harvested. It's a cash crop and also perennial. So you can grow it anytime."
        
              
                
    return render_template('CropRecom.html', prediction_text=cropStatement)


@app.route("/cropinfo",methods=["POST", "GET"])
def forms():
    s=request.form.get("crop")  
    s=str(s)
    print(s)
    print(type(s))
    client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&directConnection=true&ssl=false')
    filter={
    'CROPS': s
}
    result = client['crop']['crop'].find(
    filter=filter
     )
    print(type(result))
    rslt=list(result)
    print(type(rslt))
    cropname = rslt[0]["CROPS"]
    about = rslt[0]["GENERAL INFO"]
    croptype = rslt[0]["TYPE OF CROPS"]
    bio_name = rslt[0]["BIOLOGICAL NAMES"]
    seeds = rslt[0]["SEED"]
    soil = rslt[0]["TYPE OF SOIL USED"]
    major_g_states = rslt[0]["MAJOR GROWING STATES"]
    climate = rslt[0]["CLIMATE(degree)"]
    #irrigation = rslt[0]["SEED"]
    grow_months= rslt[0]["GROWING MONTHS"]
    yield_d = rslt[0]["YIELD (DAYS)"]
    pesticide = rslt[0]["PESTICIDE TYPE"]
    chemical = rslt[0]["CHEMICAL USED"]
    diseases = rslt[0]["Diseases"]
    symptoms = rslt[0]["Symptoms"]
    print(cropname)
    #return (cropname)
    return render_template("printcropinfo.html", cropname=cropname,about=about,croptype=croptype, bio_name=bio_name,seeds=seeds,soil=soil, 
    major_g_states=major_g_states,climate=climate,grow_months=grow_months,yield_d=yield_d,  pesticide=pesticide,
     chemical=chemical, diseases=diseases,symptoms=symptoms)


app.run(port=5000,debug=True,host='localhost')    


from flask import Flask, render_template,request
from pymongo import MongoClient


app=Flask("Hara Jeewan")

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

@app.route("/irrigation")
def irrigation():
    return render_template("modern_f.html")   

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
  

@app.route("/cropinfo",methods=["POST", "GET"])
def forms():
    s=request.form.get("crop")  
    s=str(s)
    print(s)
    print(type(s))
    client = MongoClient('mongodb://127.0.0.1:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
    filter={
    'CROPS': s
}
    result = client['admin']['crops'].find(
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

@app.route("/data")
def data():
    return "data123"

app.run(port=5000,debug=True,host='0.0.0.0')    

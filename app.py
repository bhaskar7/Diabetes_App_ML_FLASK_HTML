from flask import Flask, render_template, request
from keras.models import load_model

model  = load_model("dia_flask_model.h5")
app = Flask("self")

@app.route("/")
def home():
    return render_template("frontpage.html")

@app.route("/result", methods=["GET"])
def result():
   # if request.method == "POST":
        pragnencies = request.args.get("pragnencies")
        glucose = request.args.get("glucose")
        bp = request.args.get("bp")
        st = request.args.get("st")
        insulin = request.args.get("insulin")
        bmi = request.args.get("bmi")
        dpf = request.args.get("dpf")
        age = request.args.get("age")
        result1 = request.form

        x1 = pragnencies
        x2 = glucose
        x3 = bp
        x4 = st
        x5 = insulin
        x6 = bmi
        x7 = dpf
        x8 = age
        result = model.predict([[ int(x1), int(x2), int(x3), int(x4), int(x5), float(x6), float(x7), int(x8)  ]])
        if round(result[0][0]) == 0:
            return render_template("result.html", pragnencies=pragnencies, glucose=glucose, bp=bp, st=st, insulin=insulin, bmi=bmi, dpf=dpf, age=age)
        elif round(result[0][0]) == 1:
            return  render_template("result1.html", pragnencies=pragnencies, glucose=glucose, bp=bp, st=st, insulin=insulin, bmi=bmi, dpf=dpf, age=age)
        

app.run(host="0.0.0.0", port=5000,debug=True)


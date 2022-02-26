from flask import Flask, render_template 
import pandas as pd
import os 
from prediction import predict

# create app 
app = Flask(__name__)


# page routes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/forecast")
def forecast():
    return render_template("forecast.html")




@app.route("/api/predict/<BUILD_YEAR>/<BEDROOMS>/<BATHROOMS>/<LAND_AREA>/<FLOOR_AREA>/<CBD_DIST>/<NEAREST_SCH_RANK>", methods=["GET"])
def do_predict(BUILD_YEAR, BEDROOMS,BATHROOMS,LAND_AREA, FLOOR_AREA,CBD_DIST,NEAREST_SCH_RANK):
    user_input = {
        "BUILD_YEAR": float(BUILD_YEAR), 
        "BEDROOMS": float(BEDROOMS),
        "BATHROOMS": float(BATHROOMS),
        "LAND_AREA": float(LAND_AREA), 
        "FLOOR_AREA": float(FLOOR_AREA),
        "CBD_DIST": float(CBD_DIST),
        "NEAREST_SCH_RANK": float(NEAREST_SCH_RANK)
 
    }
    prediction = predict(user_input)

    return {"prediction": prediction}

if __name__ == "__main__":
    app.run(debug=True)

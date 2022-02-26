import pandas as pd 
import joblib 

def predict(user_inputs):
    # load model binaries 
    model = joblib.load("static/py/model.sav")
    encoder = joblib.load("static/py/encoder.sav")
    X_scaler = joblib.load("static/py/x_scaler.sav")
    y_scaler  = joblib.load("static/py/y_scaler.sav")

    # get the user input data 
     # get the user input data 
    BUILD_YEAR = user_inputs["BUILD_YEAR"]
    BEDROOMS = user_inputs["BEDROOMS"]
    BATHROOMS = user_inputs["BATHROOMS"]
    LAND_AREA = user_inputs["LAND_AREA"]
    FLOOR_AREA = user_inputs["FLOOR_AREA"]
    CBD_DIST = user_inputs["CBD_DIST"]
    NEAREST_SCH_RANK = user_inputs["NEAREST_SCH_RANK"]

    
    
    # store pressure and humidty into df 
    input_df = pd.DataFrame({
        "BUILD_YEAR": [BUILD_YEAR],
        "BEDROOMS": [BEDROOMS],
        "BATHROOMS": [BATHROOMS],
        "LAND_AREA": [LAND_AREA],
        "FLOOR_AREA": [FLOOR_AREA],
        "CBD_DIST": [CBD_DIST],
        "NEAREST_SCH_RANK": [NEAREST_SCH_RANK]
    })

    # scale the X input df 
    X_scaled = X_scaler.transform(input_df)


    # obtain prediction (y) 
    prediction_scaled = model.predict(X_scaled)
    
    # scale prediction to human readable terms i.e. celcius 
    prediction = y_scaler.inverse_transform(prediction_scaled)
    return prediction[0][0]
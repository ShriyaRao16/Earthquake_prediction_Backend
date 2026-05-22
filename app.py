from flask import Flask, render_template
import Earthquickprediction
import numpy as np
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict")
def predict():

    latitude = 13.08
    longitude = 80.27
    timestamp = datetime.datetime.now().timestamp()

    input_data = np.array([[timestamp, latitude, longitude]])
    input_scaled = scaler_X.transform(input_data)

    prediction = model.predict(input_scaled)
    prediction = scaler_y.inverse_transform(prediction)

    magnitude = prediction[0][0]
    depth = prediction[0][1]

    return f"Predicted Magnitude: {magnitude:.2f} | Depth: {depth:.2f} km"

if __name__ == "__main__":
    app.run(debug=True)
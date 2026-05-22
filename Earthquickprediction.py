import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import requests
import smtplib
from email.mime.text import MIMEText

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from keras.models import Sequential
from keras.layers import Dense

# -----------------------------
# 1. LOAD DATASET
# -----------------------------
data = pd.read_csv("dataset.csv")
data = data[['Date','Time','Latitude','Longitude','Depth','Magnitude']]

# Convert Date + Time → Timestamp
timestamps = []
for d, t in zip(data['Date'], data['Time']):
    try:
        ts = datetime.datetime.strptime(d+' '+t, '%m/%d/%Y %H:%M:%S')
        timestamps.append(ts.timestamp())
    except:
        timestamps.append('ValueError')

timestamps = pd.Series(timestamps)
data['Timestamp'] = timestamps.values

final_data = data.drop(['Date','Time'], axis=1)
final_data = final_data[final_data['Timestamp'] != 'ValueError']
final_data['Timestamp'] = final_data['Timestamp'].astype(float)

print(final_data.head())

# -----------------------------
# 2. PLOT EARTHQUAKE MAP
# -----------------------------
from mpl_toolkits.basemap import Basemap

m = Basemap(projection='mill',
            llcrnrlat=-80,
            urcrnrlat=80,
            llcrnrlon=-180,
            urcrnrlon=180,
            resolution='c')

longitudes = final_data["Longitude"].tolist()
latitudes = final_data["Latitude"].tolist()

x, y = m(longitudes, latitudes)

plt.figure(figsize=(12,10))
plt.title("All Earthquake Locations")

m.plot(x, y, "o", markersize=2, color='blue')
m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='coral')
m.drawmapboundary()

plt.show()

# -----------------------------
# 3. PREPARE ML DATA
# -----------------------------
X = final_data[['Timestamp','Latitude','Longitude']]
y = final_data[['Magnitude','Depth']]

scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

X_train = scaler_X.fit_transform(X_train)
X_test = scaler_X.transform(X_test)

y_train = scaler_y.fit_transform(y_train)
y_test = scaler_y.transform(y_test)

# -----------------------------
# 4. BUILD NEURAL NETWORK
# -----------------------------
model = Sequential()

model.add(Dense(16, activation='relu', input_shape=(3,)))
model.add(Dense(16, activation='relu'))
model.add(Dense(2))

model.compile(optimizer='adam',
              loss='mse',
              metrics=['mae'])

model.fit(
    X_train,
    y_train,
    batch_size=10,
    epochs=20,
    validation_data=(X_test, y_test)
)

# -----------------------------
# 5. MODEL EVALUATION
# -----------------------------
[test_loss, test_mae] = model.evaluate(X_test, y_test)

print("Test Loss:", test_loss)
print("Test MAE:", test_mae)

# -----------------------------
# 6. USER LOCATION DETECTION
# -----------------------------
def get_user_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()

        loc = data['loc']
        latitude, longitude = loc.split(',')

        print("User Location:", latitude, longitude)

        return float(latitude), float(longitude)

    except:
        print("Location detection failed")
        return None, None

user_lat, user_lon = get_user_location()

# -----------------------------
# 7. PREDICTION USING USER LOCATION
# -----------------------------
current_time = datetime.datetime.now().timestamp()

input_data = np.array([[current_time, user_lat, user_lon]])

input_scaled = scaler_X.transform(input_data)

prediction = model.predict(input_scaled)

prediction = scaler_y.inverse_transform(prediction)

pred_magnitude = prediction[0][0]
pred_depth = prediction[0][1]

print("Predicted Magnitude:", pred_magnitude)
print("Predicted Depth:", pred_depth)

# -----------------------------
# 8. SAFETY INSTRUCTIONS
# -----------------------------
def show_safety_instructions():

    tips = [
        "DROP to the ground",
        "Take COVER under a table",
        "HOLD ON until shaking stops",
        "Stay away from windows",
        "Move to open area if outside",
        "Do not use elevators"
    ]

    print("\nEARTHQUAKE SAFETY INSTRUCTIONS")
    print("--------------------------------")

    for tip in tips:
        print("-", tip)

show_safety_instructions()

# -----------------------------
# 9. EMAIL ALERT SYSTEM
# -----------------------------
def send_email(recipient, subject, message):

    sender_email = "shriyaraob@gmail.com"
    sender_password = "aouk skoe ufnt ukuc"

    msg = MIMEText(message)

    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

        server.login(sender_email, sender_password)

        server.sendmail(sender_email, recipient, msg.as_string())

    print("Alert Email Sent!")

# -----------------------------
# 10. ALERT LOGIC
# -----------------------------
if pred_magnitude > 5:

    alert_message = f"""
EARTHQUAKE ALERT

Predicted Magnitude: {pred_magnitude:.2f}
Predicted Depth: {pred_depth:.2f} km

Location:
Latitude: {user_lat}
Longitude: {user_lon}

Stay Safe!
"""

    send_email(
        "shriyarao2024@gmail.com",
        "⚠ Earthquake Alert",
        alert_message
    )

else:

    print("No significant earthquake predicted.")
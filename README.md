# Earthquake_prediction_Backend
An AI-powered prediction system developed using Deep Learning and Python to predict earthquake risk based on past geographical coordinates.

This project processes location-based inputs such as latitude and longitude and uses a deep learning model to generate earthquake risk predictions, estimated magnitude, and depth information.

# Aim
To develop a deep learning-based backend application capable of analyzing geographical data and predicting earthquake risks accurately and efficiently.
# Features
Accepts latitude and longitude as input<br>
🤖 Uses Deep Learning for prediction<br>
📊 Predicts earthquake risk levels<br>
🌡 Estimates earthquake magnitude and depth<br>
⚡ Fast backend processing<br>
🔗 Easy integration with frontend applications<br>
📧 Mail alerts 
# Technologies Used
•Python<br>
•Deep Learning<br>
•TensorFlow / Keras<br>
•Pandas<br>
•NumPy<br>
•Scikit-learn<br>
•Flask / FastAPI<br>
# Project Structure
```
Earthquake_prediction_Backend
 │── model
 │── dataset
 │── app.py
 │── requirements.txt
 │── README.md
```
# Workflow
1.)User provides latitude and longitude<br>
2.)Input data is preprocessed<br>
3.)Deep learning model analyzes the data<br>
4.)Earthquake risk level is predicted<br>
5.)Estimated magnitude and depth are generated<br>
6.)Results are returned to the application<br>
7.)Email Alerts
# Installation
Clone the repository
```
git clone https://github.com/ShriyaRao16/Earthquake_prediction_Backend.git
```
Install dependencies
```
pip install -r requirements.txt
```
Run the Project
```
python app.py
```
# Example Output
```
Location: California, USA
Risk Level: Moderate
Estimated Magnitude: 5.4
Depth: 12 km
```
# SMTP Configuration
The email service is implemented using Python’s built-in``` smtplib``` library and Google Mail SMTP server.
```
Gmail SMTP Settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
```

# Google Account Setup
To enable email alerts using Gmail:

1.)Turn on 2-Step Verification in your Google Account.<br>
2.)Generate an App Password from Google Security settings.<br>
3.)Use the generated App Password in the application instead of your actual Gmail password.<br>

# Required Libraries
```
pip install secure-smtplib
```
# Future Enhancements
‣ Real-time earthquake API integration<br>
‣ Improved deep learning architecture<br>
‣ Live monitoring dashboard<br>
‣ Mobile app deployment<br>
‣ Notification and alert system ( SMS features)<br>

# Conclusion
This project demonstrates how Deep Learning can be integrated with backend systems to create intelligent earthquake prediction applications. It combines AI, data processing, and predictive analytics to provide meaningful earthquake risk insights.
# 👩‍💻 Author
Shriya Rao






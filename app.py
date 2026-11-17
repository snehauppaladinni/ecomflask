from flask import Flask
SHIPPING_ANNOUNCEMENT = "arriving soon"
@app.route('/')
def home():
  return "welcome"

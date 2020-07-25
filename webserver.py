from flask import Flask
from threading import Thread

app = Flask('')
#e
@app.route('/')
def home():
  return"Webserver OK, Discord bot ok"
  
def run():
  app.run(host="0.0.0.0",port=8080)
      
def keep_alive():
  t=Thread(target=run)
  t.start()

import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'LazyDeveloper'

os.system("git clone https://lionyt69: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@github.com/lionyt69/LazyPrincessV2 okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")

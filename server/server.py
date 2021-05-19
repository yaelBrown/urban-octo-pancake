from flask import Flask
import subprocess
import sys

from main import Main

app = Flask(__name__)

def runMain():
  res = subprocess.run([sys.executable, "main.py"])


if __name__ == "__main__":
  app.run(port=5000, debug=True)
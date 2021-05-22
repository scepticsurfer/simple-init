# when this file was named __init__.py the program didn't work
# after renaming the file to app.py the program works 
from flask import Flask
app = Flask(__name__)
import stream
import os
from app import app

client = stream.connect(app.config['API_KEY'], app.config['API_SECRET'])
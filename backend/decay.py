import math
from datetime import datetime

def decay(salience, timestamp_str, rate=0.01):
    timestamp = datetime.fromisoformat(timestamp_str)
    age = (datetime.utcnow() - timestamp).total_seconds() / (60*60*24)  # age in days
    return salience * math.exp(-rate * age)

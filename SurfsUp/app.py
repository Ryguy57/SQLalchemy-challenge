# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################

# Create an instance of Flask
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return (
        "Welcome to the Climate App!<br>"
        "Available Routes:<br>"
        "/api/v1.0/precipitation<br>"
        "/api/v1.0/stations<br>"
        "/api/v1.0/tobs<br>"
        "/api/v1.0/<start><br>"
        "/api/v1.0/<start>/<end>"
    )
# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Perform your precipitation analysis here and convert to dictionary
    # precipitation_data = ...
    # Create a dictionary with date as key and prcp as value
    # precipitation_dict = ...
    return jsonify(precipitation_dict)
# Temperature observations route
@app.route("/api/v1.0/tobs")
def tobs():
    # Perform your temperature observations analysis here
    # tobs_data = ...
    return jsonify(tobs_data)
# Start date route
@app.route("/api/v1.0/<start>")
def temp_stats_start(start):
    # Perform temperature stats calculation from start date to end of dataset
    # temp_stats = ...
    return jsonify(temp_stats)
# Start and end date route
@app.route("/api/v1.0/<start>/<end>")
def temp_stats_start_end(start, end):
    # Perform temperature stats calculation from start date to end date
    # temp_stats = ...
    return jsonify(temp_stats)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

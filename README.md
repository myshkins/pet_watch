# Pet Watch

The inspiration for this project came from Chancho the chinchilla. He's a 15 year old chinchilla who is very particular about the climate around him. Chinchillas generally don't tolerate temperatures outside the range of 60-75 degrees Farenheit. Thus, I created this app as a way to monitor the temperature of my apartment when I'm away. 


## Project Architecture
##### Stack
The tech stack for the app is Flask, Postgres, SQLAlchemy, Gunicorn, and Nginx. The frontend is served up with basic html and CSS. Matplotlib is used to render the temperature graph.  The temperature data comes from a Raspberry Pi 4b with an attached SenseHat temperature sensor that sits in my apartment.  

##### Data
I wrote a systemd service file to run the `pi_temp_sender.py` script on the Raspberry pi. That script runs continuously, sending a temperature data point to the Postgres database which is hosted on my VPS. 

##### Backend
I've used Docker to deploy this app on my VPS. There are three components to the backend: a Postgres Database, a Flask API, and the Flask app. Each of these sits inside it's own Docker container, and they are all networked together. The Flask app uses the factory pattern and blueprints. Though blueprints may be overkill for such a simple app, I do plan on adding more functionality in the future, so hopefully this structure will pay off. 

## Future Plans
There are a number of features I would like to add to this project. 

##### Time Windows
As of right now, the temperature data is only available in a 24 hour view. My next step is to build functionality for different time windows to allow views of 3 hours, 3 days, 1 week, etc.

##### Camera functionality
The Raspberry Pi comes with an input slot for a small camera lens. A useful feature I plan on adding is photo and video capturing in order to check in on lil Chancho. I'd like to be able to show a live feed from the camera and/or take snapshots 

##### Picture Gallery
Following the camera feature, I'd like to also add a photo gallery page. 

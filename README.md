# Mtcars-Flask-Api

model variable:

Outcome Variable: mpg

Predictors : cyl disp hp drat wt qsec gear

**1. To run this API, go to  your directory to the docker folder and run:**

`docker-compose up`

If it has created the localhost server correctly you will not get your prompt back. 

**2. You will need to open a new terminal (be in the same directory) and run the following curl command **

`curl http://localhost:5000/`

You should get the following response:

The server is up.

**3. To predict MPG, we will pass these through a json formatted input through a curl POST request to the API. This is done as**

curl -H "Content-Type: application/json" -X POST -d '{"cyl":"6","disp":"200","hp":"220","drat":"4.2","wt":"2.5","qsec":"12","gear":"2"}' "http://localhost:5000/predict_mpg"}

his should return { "predict mpg": 16.30032090294849 }

You can change some of the values to see the prediction change. To stop your server running the API, type `ctrl-C`. As usual, check to see if you have any docker containers running using `docker container ls` and stop them through `docker container kill <container-name>`

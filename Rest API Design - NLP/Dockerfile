# Root Image Source
FROM python:3.7-slim

# Fundamental support dependencies
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install manpages-dev -y
RUN apt-get install libblas-dev liblapack-dev gfortran -y
RUN pip install --upgrade pip

# Copy Directory Contents
COPY . .
RUN pip install -r requirements.txt
#RUN ["chmod", "+x", "docker_entry"]

ENTRYPOINT ["flask", "run","--host=0.0.0.0"]

#comments for reference
# docker build . -t test
# docker run -d -p 5000:5000 test

#curl --location --request GET 'http://localhost:5000/api/v1/classify' \
#--header 'Content-Type: application/json' \
#--data-raw '{"text":["Hello World","testing"
#  ]
#}
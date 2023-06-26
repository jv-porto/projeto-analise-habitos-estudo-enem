#syntax=docker/dockerfile:1

# defining base image
FROM python:3.11.0rc2-alpine3.16

# defining work directory
WORKDIR /rest_api

# copying local files to WORKDIR inside container
COPY . .

# installing libraries from requirements.txt
RUN pip3 install -r requirements.txt

# running the application
CMD ["python", "main.py"]

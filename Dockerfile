FROM python:3.9 

WORKDIR /app

COPY flask_req.txt flask_req.txt

RUN pip3 install -r flask_req.txt

COPY . .



CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
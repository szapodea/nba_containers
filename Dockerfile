FROM python:3.8-alpine
WORKDIR /docker_dir

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /docker_dir

EXPOSE 8082

CMD ["python", "./app.py"]

FROM python:buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod -R 777 /usr/src/app

EXPOSE 5007

CMD [ "python", "./server.py" ]

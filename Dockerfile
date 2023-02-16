FROM python:3.11.2

WORKDIR /app

COPY ./requirements.txt /app

RUN apt update && \
    apt upgrade -y && \
    pip install -r requirements.txt

#RUN chmod +x /docker-entrypoint-initdb.d/road_data.sh
#load data local infile '/data/release_1.csv' into table releases FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;
COPY . /app

EXPOSE 80

CMD python main.py

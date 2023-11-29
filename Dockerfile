FROM python

ENV DOCKERIZE_VERSION v0.6.1


RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz


COPY /api.py /app/api.py

COPY /params.py /app/params.py

COPY /.env /app/.env

RUN pip install flask

RUN pip install mysql-connector-python

RUN pip install python-dotenv

WORKDIR /app

EXPOSE 4000

CMD python api.py
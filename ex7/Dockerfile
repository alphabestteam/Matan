FROM python

copy ./flask /app

RUN pip install flask

copy ./app1.py /app

EXPOSE 5001

CMD python /app/app1.py
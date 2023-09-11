FROM python:3.9-bookworm

RUN useradd huami

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . .
ENV FLASK_APP huami.py

RUN chown -R huami:huami ./
USER huami

EXPOSE 8000
ENTRYPOINT ["gunicorn","-b", "0.0.0.0:8000","-w","4", "huami:app"]

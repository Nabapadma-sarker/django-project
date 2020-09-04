FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN python3 -m pip install --user virtualenv --no-warn-script-location
RUN python3 -m virtualenv venv/
RUN . venv/bin/activate
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
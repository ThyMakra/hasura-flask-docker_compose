FROM python:3.6

# Bundle app source
COPY . /app

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "python", "-u", "app.py" ]
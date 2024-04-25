# FROM  python:3.10.12-slim-bookworm
FROM python:3.10-slim

# Install the necessary packages to compile MariaDB client library
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    bash \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

ENV SECURITY_PARAMETER=128 
ENV LIBRARY=DEFAULT
ENV DATASET=ADULT
ENV NUM_SLOTS=8192

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY model .
COPY utils.py .
COPY demo.py .

CMD [ "python", "./demo.py" ]

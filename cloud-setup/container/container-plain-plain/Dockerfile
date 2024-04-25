FROM  python:3.10.12-slim-bookworm

ENV SECURITY_PARAMETER=128 
ENV LIBRARY=DEFAULT
ENV DATASET=ADULT
ENV NUM_SLOTS=8192

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY model .
COPY utils.py .
COPY demo.py .

CMD [ "python", "./demo.py" ]
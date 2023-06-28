FROM python:3

COPY requirements.txt /tmp/pip-tmp/

RUN pip install --upgrade pip
RUN pip install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp


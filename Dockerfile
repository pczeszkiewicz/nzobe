FROM python:3.7
ENV PYTHONBUFFERED 1
RUN mkdir /nozbe
WORKDIR /nozbe
ADD requirements.txt /nozbe/
RUN pip install -r requirements.txt
ADD . /nozbe
RUN ["chmod", "+x", "/nozbe/entrypoint.sh"]

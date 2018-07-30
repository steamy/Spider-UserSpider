FROM python:3.6

ADD . /code
WORKDIR /code
RUN pip install  -r requirement.txt -i https://mirrors.aliyun.com/pypi/simple
CMD scrapy carwl users -s LOG_FILE=users.log

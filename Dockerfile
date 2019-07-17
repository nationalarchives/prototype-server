FROM python:alpine
WORKDIR server
COPY ./ .
RUN apk update && \
                apk add yarn build-base libffi-dev openssl-dev openjdk8-jre && \
                yarn  && \
                pip install -r requirements.txt
CMD yarn offline:docker
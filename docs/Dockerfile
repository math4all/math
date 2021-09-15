FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1
ENV LIVE_RELOAD_SUPPORT='true' \
    AUTO_UPDATE='true' \
    UPDATE_INTERVAL=15
ENV XDG_CONFIG_HOME=~/.config


RUN apk update \
    && apk add --virtual build-deps gcc make python3-dev musl-dev \
    && apk add --no-cache libffi-dev bash curl g++ libxslt-dev linux-headers coreutils \
    && apk add build-base libzmq zeromq-dev jpeg-dev zlib-dev libjpeg cairo-dev cairo cairo-tools pango-dev gdk-pixbuf-dev fontconfig 

RUN apk add --no-cache make

# Headless Chrome
RUN apk --update --upgrade --no-cache add udev chromium chromium-chromedriver \
    && chromium-browser --version

ADD ./requirements.txt /tmp/

WORKDIR /tmp
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apk del build-deps

ADD . /code/

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

WORKDIR /code/

EXPOSE 8000
EXPOSE 9000

CMD /./entrypoint.sh

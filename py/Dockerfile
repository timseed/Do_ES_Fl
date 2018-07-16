FROM frolvlad/alpine-python3
MAINTAINER tim@sy-edm.com

run pip3 install elasticsearch flask && \
    pip install --upgrade pip

add run.sh  /run.sh
run chmod +x /run.sh
add test.py  /test.py

CMD "/run.sh"

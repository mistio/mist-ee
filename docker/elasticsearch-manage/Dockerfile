FROM amaas-eos-mw1.cec.lab.emc.com:5070/milos/main/python3:latest

RUN pip install --no-cache-dir elasticsearch==7.10.1 certifi ipdb

COPY . /opt/elasticsearch-manage

WORKDIR /opt/elasticsearch-manage

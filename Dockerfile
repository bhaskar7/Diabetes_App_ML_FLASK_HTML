FROM centos

RUN yum install python3 -y &&\
    yum install python3-devel -y &&\
    pip3 install --upgrade pip &&\
    pip3 install keras &&\
    pip3 install tensorflow==2.2 &&\
    pip3 install flask 

WORKDIR /

COPY templates templates/

COPY static static/

COPY app.py /

COPY dia_flask_model.h5 /

EXPOSE 5000

ENTRYPOINT python3 app.py

 

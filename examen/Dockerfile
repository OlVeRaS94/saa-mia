FROM python:3.6
RUN pip3 install experta
RUN pip3 install notebook
RUN pip3 install scikit-fuzzy
RUN pip3 install numpy
RUN pip3 install matplotlib
RUN pip3 install scipy
WORKDIR /home/MIA2324
#VOLUME .
CMD jupyter notebook --allow-root --ip=0.0.0.0 --port=8888 --no-browser
#ENTRYPOINT "jupyter notebook --allow-root --ip=0.0.0.0 --port=8888 --no-browser"

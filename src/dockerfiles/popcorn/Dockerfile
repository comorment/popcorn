FROM ubuntu:20.04

ENV TZ=Europe
ENV DEBIAN_FRONTEND noninteractive

# Essential tools
WORKDIR /tmp
COPY /scripts/apt_get_essential.sh .
RUN chmod +x apt_get_essential.sh
RUN bash apt_get_essential.sh

WORKDIR /tmp
COPY /scripts/install_mambaforge.sh .
RUN chmod +x install_mambaforge.sh
RUN bash install_mambaforge.sh

# set up python env.
RUN mamba install python=3.10.6 \
    numpy=1.23.3 \
    scipy=1.9.1 \
    pandas=1.5.0 \
    statsmodels=0.13.2 \
    bottleneck=1.3.5 \
    "h5py=3.7.0=nompi*" \
    --yes

RUN mamba install \
    psutil=5.9.3 \
    dill=0.3.5.1 \
    more-itertools=9.0.0 \
    --yes

RUN yes | pip install cbgen==1.0.2
RUN yes | pip install bgen-reader==4.0.8 
RUN yes | pip install bed-reader==0.2.24

#?    wheel \
#psutil>=5.6.7
#dill>=0.2.9
#bgen-reader>=4.0.7
#wheel>=0.34.2
#bed-reader>=0.2.5
#more-itertools>=8.7.0

RUN yes | pip install pysnptools==0.5.4 --no-dependencies

WORKDIR /tools/popcorn
RUN git clone https://github.com/brielin/Popcorn.git . && \
    git reset --hard ef4455a970d4104832cca02510c555d9220b1414 && \
    pip install . --no-dependencies

# cleanup for smaller image size
RUN mamba clean -a -y
RUN pip cache purge 

WORKDIR /tools


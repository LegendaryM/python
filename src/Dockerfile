FROM nvidia/cuda:11.4.1-cudnn8-devel-ubuntu18.04

# 还需要一个chk.tar.gz
WORKDIR /code
COPY . /code

RUN gpg --keyserver keyserver.ubuntu.com --recv A4B469963BF863CC
RUN gpg --export --armor A4B469963BF863CC | apt-key add -
RUN apt-get update
RUN apt-get install -y vim wget unzip ffmpeg
RUN apt-get install build-essential -y


# install base env
RUN cd /code \
    && wget --no-check-certificate https://mirrors.bfsu.edu.cn/anaconda/miniconda/Miniconda3-py38_4.11.0-Linux-x86_64.sh \
    && bash Miniconda3-py38_4.11.0-Linux-x86_64.sh -b -p /opt/conda \
    && rm -f Miniconda3-py38_4.11.0-Linux-x86_64.sh \
    && ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh \
    && echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc

RUN . ~/.bashrc \
    && conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge \
    && conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2 \
    && conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/ \
    && conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r \
    && conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free \
    && conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main \
    && conda config --set show_channel_urls yes \
#    && conda env create -f project_based/conda_base.yml
    && conda create -n torch1.13 python=3.7

RUN . ~/.bashrc \
    && conda activate torch1.13 \
    && pip install --upgrade -r /code/requirements.txt  -i  https://pypi.tuna.tsinghua.edu.cn/simple/ --timeout 600  \
    # api
    && pip install fastapi -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
    && pip install "uvicorn[standard]" -i https://pypi.tuna.tsinghua.edu.cn/simple/


# 6、运行服务
#CMD ["uvicorn", "http_api2:app", "--host", "0.0.0.0", "--port", "80"]
EXPOSE  22
EXPOSE  80
CMD /usr/sbin/sshd -D

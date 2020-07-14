FROM python:3-alpine
LABEL MAINTAINER="Barre Kevin"
LABEL DESCRIPTION="Simple Python3 for simple python script"
LABEL VERSION=1

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 HOME=/home/ast
ENV PATH=${HOME}/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH

SHELL ["/bin/sh", "-c"]

ARG USERNAME=ast
ARG USER_UID=1000

WORKDIR ${HOME}

RUN adduser \
	--disabled-password \
	--gecos "" \
	--home "$(pwd)" \
	--uid $USER_UID \
	$USERNAME

USER $USERNAME

COPY cdcp.py ${HOME}

ENTRYPOINT python3 fbtree.py



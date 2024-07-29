FROM python:3.9-slim

# Install system dependencies
RUN apt-get update \
    && apt-get install -y \
        curl \
        wget \
        gcc \
        g++ \
        openssl \
        gnupg \
        supervisor \
        nginx \
        vim

# Install Node.js and yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && curl -sL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get update \
    && apt-get install -y \
        nodejs \
        yarn

RUN yarn install && \
    yarn add express cors fs nodemon

WORKDIR /etc/nginx

COPY ./html /etc/nginx/html

# Set the working directory
WORKDIR /opt/app

# Copy the application files into the container
COPY ./Markov .

WORKDIR /opt/app/MarkovProprietary

# Set path variables
ENV MARKOV_HOME=/opt/app/MarkovProprietary/pipelinestages
ENV LIGHTDOCK_HOME=/opt/app/lightdock
ENV GEMMI_HOME=/opt/app/gemmi
ENV PATH=$PATH:$LIGHTDOCK_HOME/bin:$MARKOV_HOME/bin:$GEMMI_HOME/bin
ENV PYTHONPATH=$PYTHONPATH:$LIGHTDOCK_HOME:$MARKOV_HOME:$GEMMI_HOME

WORKDIR /opt/app/./lightdock

# Create virtual environment
RUN python -m venv venv \
    && /bin/bash -c "source venv/bin/activate" \
    && pip install --upgrade pip \
    && pip install -e . cython pyparsing==2.4.7 requests pandas openpyxl \
    && pip install flask jinja2 markupsafe gunicorn flask-cors

RUN chmod u+x run_server.sh

# unzip files
RUN cd ../MarkovProprietary/pipelinestages/make_tables/python && python unzip.py

# Copy supervisord.conf into the container
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose ports for Node.js applications
EXPOSE 3000
EXPOSE 4000
EXPOSE 8000
# Define the command to run your application
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

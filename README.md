<div align="center"> 

# Mazer-Blog-Framework

<img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="python">
<img src="https://img.shields.io/badge/Node.js-v20+-rgb(67,141,64).svg" alt="node">
<img src="https://img.shields.io/badge/Vue.js-v3-rgb(53,73,94).svg" alt="vue">
<img src="https://img.shields.io/badge/PostgreSQL-16-rgb(51,103,145).svg" alt="postgre">
<img src="https://img.shields.io/badge/Flask-v3-rgb(58,169,191).svg" alt="flask">

<br>
A All-in-one Blog Framework
<br>
Powered by Vue / Node.js / PostgreSQL / Flask

You can download the build from [releases](https://github.com/Tyuwwe/Mazer-Blog-Framework/releases)


</div>

## Installation

### 1. SQL Server

Download PostgreSQL from [here](https://www.postgresql.org/download/).

Follow the PostgreSQL installation guide to install the SQL server.

You might have to set a safe password of the SQL server.

### 2. Python

The MBF was developed under Python 3.10 and Python 3.12, so most modern Python verison should be fine.

All needed packages are listed in `./mazer-studio-v2-server/requirements.txt` file. In most situations you just need to use `pip install -r requirements.txt` in `./mazer-studio-v2-server` folder and all packages will be install automatically.

### 3. Pre-firstrun

According your SQL server configuraion, you might have to modify the server config in `./mazer-studio-v2-server/config.py` file, which is list below.

```
SQLALCHEMY_DATABASE_URI = 'postgresql://{Username}:{Password}@{IP}/{DB}'
```

### 4. Open Local Web Server

There are many ways to launch a local web server, for example, use Node.js (you have to [download ](https://nodejs.org/)it) to open a server:

```shell
# Install npm serve package
npm install --global serve

# Launch serve in release/Frontend folder
serve
```

### 5. Run Python Flask

Enter folder & run `python ./app.py`, the server will connect PostgreSQL and print logs.

## Build

If you want to build on your own environment, you have to install [Node.js](https://nodejs.org/) first.

Its quite simple to build a Vue project:

```shell
# Install necessary packages
npm install

# Run build in source/mazer-studio-v2
npm run build
```

The generated file will shown in `/dist` folder.

## Troubleshoot

It's a pretty early version now, if you have met any bugs, please create a new [issue](https://github.com/Tyuwwe/Mazer-Blog-Framework/issues), I will fix them.

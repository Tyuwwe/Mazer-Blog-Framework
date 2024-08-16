# Mazer-Blog-Framework

The Mazer Blog Framework (MBF) is a Frontend + Backend All-in-one Framework.

Powered by Vue / Node.js / PostgreSQL / Flask

You can download the build from [releases](https://github.com/Tyuwwe/Mazer-Blog-Framework/releases).

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
# Run build in source/mazer-studio-v2
npm run build
```

The generated file will shown in `/dist` folder.

## Troubleshoot

It's a pretty early version now, if you have met any bugs, please create a new [issue](https://github.com/Tyuwwe/Mazer-Blog-Framework/issues), I will fix them.

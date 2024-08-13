/* Users */
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    usr VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    psw TEXT NOT NULL,
    usr_role INT NOT NULL,
    usr_desc TEXT,
	avt VARCHAR(200) DEFAULT '/static/image/default.png'
);

/* System Log */
CREATE TABLE syslog (
    log_id SERIAL PRIMARY KEY,
    evt_id INT NOT NULL,
    evt_text TEXT NOT NULL,
    evt_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

/* Pages */
CREATE TABLE pages (
    pgs_id SERIAL PRIMARY KEY,
    md_url VARCHAR(100) UNIQUE NOT NULL,
    ht_url VARCHAR(100) UNIQUE
);

/* Articles */
CREATE TABLE articles (
    auid VARCHAR(100) PRIMARY KEY,
    md_url VARCHAR(100) UNIQUE NOT NULL,
    ht_url VARCHAR(100) UNIQUE,
    author_email VARCHAR(50) NOT NULL
);
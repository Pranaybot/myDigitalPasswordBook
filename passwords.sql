CREATE TABLE USERS
(
user VARCHAR(50) PRIMARY KEY NOT NULL,
masterPassword VARCHAR(100) NOT NULL
);

CREATE TABLE PASSES
(
user VARCHAR(50) NOT NULL,
userName VARCHAR(50),
site VARCHAR(100) NOT NULL,
password VARCHAR(100) NOT NULL,
CONSTRAINT pk PRIMARY KEY (user, site)
);


/*INSERT INTO USERS VALUES('Aydin', 'myPassword');
INSERT INTO PASSES VALUES('Aydin','adogru', 'yahoo.com', '324224');*/


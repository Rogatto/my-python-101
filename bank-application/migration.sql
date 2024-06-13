create table account (
    first_name varchar(255), 
    last_name varchar(255), 
    gender varchar(255), 
    bank_balance number, 
    account_identity varchar(255),
    PRIMARY KEY (account_identity)
);

create table login (
    username varchar(255), 
    password varchar(255),
    account_identity varchar(255),
    FOREIGN KEY (account_identity) REFERENCES account(account_identity)
);

create table merchant (
    merchant_name varchar(255), 
    merchant_identity varchar(255),
    PRIMARY KEY (merchant_identity)
);
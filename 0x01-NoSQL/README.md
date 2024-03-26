# NoSQL with MongoDB

![alt text](image.png)

This project focuses on understanding and implementing NoSQL concepts, specifically utilizing MongoDB as the database management system. By the end of this project, you will have gained proficiency in working with MongoDB, querying data, and understanding the fundamentals of NoSQL databases.

## Overview

In this project, we delve into the world of NoSQL databases, particularly MongoDB, to understand its principles, advantages, and practical implementation. NoSQL databases offer flexibility and scalability, making them suitable for modern applications where structured data is not a necessity. Through this project, we aim to grasp the core concepts of NoSQL, differentiate it from SQL databases, and gain hands-on experience with MongoDB.

## Installation

### To install MongoDB 4.2 on Ubuntu 18.04, follow these steps:

- `$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -`
- `$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/`
- `$ sources.list.d/mongodb-org-4.2.list`
- `$ sudo apt-get update`
- `$ sudo apt-get install -y mongodb-org`

### To verify the installation and check the MongoDB version:
`$ sudo service mongod status`
`$ mongo --version`

### To install PyMongo:
`$ pip3 install pymongo`

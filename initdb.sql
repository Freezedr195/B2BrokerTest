create database b2broker;
create user b2brokerdbuser identified by "b2brokerdbpassword";
grant all privileges on b2broker.* to b2brokerdbuser@'%';

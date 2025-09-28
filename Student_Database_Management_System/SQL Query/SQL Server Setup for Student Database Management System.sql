CREATE DATABASE student_database;
USE [student_database];
CREATE TABLE STUDENTS (ID int, FIRST_NAME varchar(100), Last_Name varchar(100), DOB DATE, Email_Address varchar(200), course varchar(60));
INSERT INTO STUDENTS VALUES (4034, 'Joel', 'Cesula', '2001-04-21', 'jcesula@gmail.com', 'Python 101');
INSERT INTO STUDENTS VALUES (5324, 'Alesia', 'Hoxha', '2002-02-11', 'ahoxha@gmail.com', 'Web Development 101');
INSERT INTO STUDENTS VALUES (1132, 'Taulant', 'Xhaka', '2004-10-14', 'txhaka@gmail.com', 'DevOps 101');
INSERT INTO STUDENTS VALUES (5058, 'Helena', 'Proko', '2000-08-12', 'hproko@gmail.com', 'C# 1010');
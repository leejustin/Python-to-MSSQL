Python to Microsoft SQL
============
There exists some sparse documentation on getting connected to Microsoft SQL on a Linux environment.  Here, I go over the steps that I used to get Python to interface with MS SQL using TSQL on a Red Hat Linux environment.  Any Fedora-based distro should be pretty much the same steps -- other distros will have slight variations in commands but the concept will be the same.

This solution helped me resolve this error message:
```
Login failed. The login is from an untrusted domain and cannot be used with Windows authentication.
```

Prerequisites
--------------
1. yum should be installed
2. pip should be installed
3. an instance of Microsoft SQL server to interface with

Installing Packages
--------------
1. Install FreeTDS:
```
sudo yum install freetds
```
FreeTDS is an open-source interface that allows you to natively speak to MS SQL Server:
http://www.freetds.org/

2. Install pymssql
```
sudo pip install pymssql
```
pymssql is a wrapper for FreeTDS that allows you to interface with MS SQL Server using Python.
http://pymssql.org/en/stable/

Configurations
--------------
Once the steps in the installation are complete, you will need to edit the FreeTDS configuration file to add the details for the database connection.

1. Navigate to the directory and you should see the file freetds.conf
```
cd /etc/freetds.conf
```
2. Open the file for editing.  I am a vim user but you can use whatever editor that you prefer.
```
vim freetds.conf
```
3. At the bottom of this file, add the following lines.  The HOST_IP is the IP address that the SQL server is hosted on.  HOST_PORT is the port to connect to -- it's typically set as port 1433.  SOURCE_IP is from where the connection will be coming from -- in my case, it's the RHEL server that I'm setting these configs on.
```
# Testing the configuration
[testconnection]
	host = HOST_IP
	port = HOST_PORT
	tds version = 8.0
	client charset = UTF-8
	driver = freetds
	trace = no
	trusted domain = SOURCE_IP
```
Test the Connection
--------------
To test that a connection can be made to the database with TSQL, run the command in your command line.  My username had a special character in it (a '-' symbol) and putting the entire username string in single quotes helped resolve any errors.  I liked sticking this command in a shell script so that I could easily test my connection and make any database changes without needing to hop into my Windows machine.
```
tsql -H testconnection -p 1433 -U 'USERNAME' -P PASSWORD
```
This should connect to the database and you would be able to interface with the database through the command line with commands. Example:
```
USE TEST_DB;

SELECT * FROM TEST_DB;


```
If the tsql command doesn't work, then you should look at your installation of tssql that was done with yum.

Interace with Python
--------------
Refer to documentation from pymssql to see how to use Python to directly interface with the database.  I have scrapped together a simple script that you can reference.

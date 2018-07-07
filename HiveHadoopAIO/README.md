Hadoop/Hive All In One (HAIO). 
Can be used for learning Hadoop/Hive etc. purpose.

## Prerequisites

* Vagrant 
```
$ vagrant --version
Vagrant 1.8.5
```

* Ansible
```
$ ansible --version
ansible 2.2.0.0
```

## Usage

```
vagrant up
```

## Test

### Verify Hadoop Services is up
http://192.168.33.12:50070/

### Put a file

```
[hadoop@hadoop ~]$ hdfs dfs -mkdir /user
[hadoop@hadoop ~]$ hdfs dfs -mkdir /user/hadoop
[hadoop@hadoop ~]$ hdfs dfs -put /var/log/boot.log
```

```
Permission  Owner Group Size  Last Modified Replication Block Size  Name
-rw-r--r--  hadoop  supergroup  6 B 7/31/2017, 11:43:49 AM  1 128 MB  boot.log
```

###  Verify applications for cluster
http://192.168.33.12:8088/cluster

### Verify hive
```
[vagrant@hadoop ~]$ sudo su - hadoop
[hadoop@hadoop ~]$ hive
which: no hbase in (/opt/hive/bin:/opt/hadoop-2.7.3/bin:/sbin:/bin:/usr/sbin:/usr/bin:/opt/hadoop-2.7.3/sbin:/opt/hadoop-2.7.3/bin:/home/hadoop/.local/bin:/home/hadoop/bin)
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/opt/apache-hive-2.3.0-bin/lib/log4j-slf4j-impl-2.6.2.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/hadoop-2.7.3/share/hadoop/common/lib/slf4j-log4j12-1.7.10.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.apache.logging.slf4j.Log4jLoggerFactory]

Logging initialized using configuration in jar:file:/opt/apache-hive-2.3.0-bin/lib/hive-common-2.3.0.jar!/hive-log4j2.properties Async: true
Hive-on-MR is deprecated in Hive 2 and may not be available in the future versions. Consider using a different execution engine (i.e. spark, tez) or using Hive 1.X releases.
hive> CREATE TABLE test (id int, name string, age int);
OK
Time taken: 6.338 seconds
hive> CREATE DATABASE testdb;
OK
Time taken: 0.049 seconds
hive> show tables;
OK
test
Time taken: 0.089 seconds, Fetched: 1 row(s)
hive> show databases;
OK
default
testdb
Time taken: 0.019 seconds, Fetched: 2 row(s)
hive> drop table test;
OK
Time taken: 1.668 seconds

CREATE TABLE IF NOT EXISTS employee ( eid int, name String,
    salary String, destination String)
COMMENT 'Employee details'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;
```

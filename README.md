# ADB_YCSB_YugabyteDB_CockroachDB
In this project, we performed benchmarking between YugabyteDB and CockroachDB using Yahoo Cloud Serving Benchmark (YCSB). We then compared its performance against MySQLDB.
<br/><br/>

# Installation 
Steps to be followed for benchmarking YugabyteDB and CockroachDB using YCSB is provided in [document here](https://github.com/SonyShrestha/ADB_YCSB_YugabyteDB_CockroachDB/blob/main/Advanced%20Database.pdf) under Chapter 5.
<br/><br/>

# Code
The code is organized in following way.
-  Inside cockroachdb folder, db.properties file is present which contains configuration providing access information to CockroachDB
-  Inside mysqldb folder, db.properties file is present which contains configuration providing access information to MySQLDB
-  Inside yugabytedb folder, db.properties file is present which contains configuration providing access information to YugabyteDB
-  ycsb_benchmark.py is the python script that will excute ycsb command for performing benchmarking between YugabyteDB and CockroachDB
-  INFOH415.pptx is the file that was prepared for the purpose of presentation
-  Advanced Database.pdf is the report prepared for this project
-  custom_use_case/create_table.sql contains DDL Script for creating 3 tables for E-commerce platform
-  custom_use_case/olap_queries.sql contains OLAP queries which were executed in YugaByteDB and CockroachDB 
-  custom_use_case/workload_custom contains configuration for customer workload 
-  benchmarkig_plot.ipynb contains script to generate benchmarking plots
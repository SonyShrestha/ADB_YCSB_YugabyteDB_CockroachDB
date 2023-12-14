import subprocess
import os
import psycopg2



## static parameters
record_counts=[1000,10000,100000]
operation_counts=[1000,10000,100000]
worloads = ['a','b','c','d','e','f']
load_or_run=['load','run']

table_name = 'usertable'
db_name='Y'
directory ="/Users/john/ycsb-0.17.0"

def run_bash_command(command,directory,output_file):
    try:
        os.chdir(directory)
        result = subprocess.run(f'{command} > "{output_file}"', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Command output:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print("Command output:\n", e.stdout)
        print("Command error:\n", e.stderr)

def connect_to_database(db_name):
    try:
        if db_name=='Y':
        # 1.  Connection parameters for yugabytedb
            host = "localhost"
            port = 5433
            database = "ycsb"
            user = "yugabyte"
            password = "yugabyte"
        elif db_name=='C':

        # 2. Connection parameters for cockroachdb
            host = "localhost"
            port = 26257
            database = "ycsb"
            user = "max"
            password = "roach"
        else:
            print('Invalid DB parameter')
            exit(-1)

        connection_string = f"host={host} port={port} dbname={database} user={user} password={password}"

        connection = psycopg2.connect(connection_string)
        return connection
    except psycopg2.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

def truncate_table(connection, table_name):
    try:
        cursor = connection.cursor()
        truncate_query = f"TRUNCATE TABLE {table_name};"
        cursor.execute(truncate_query)
        connection.commit()
        print(f"Table {table_name} truncated successfully.")
    except psycopg2.Error as err:
        print(f"Error truncating table: {err}")
    finally:
        cursor.close()

for wl in worloads:
    for rec in record_counts:
        for op in operation_counts:
            for lr in load_or_run:
                if lr=='load':
                    connection = connect_to_database(db_name)
                    if connection:
                        try:
                            truncate_table(connection,table_name)
                        except psycopg2.Error as err:
                            print('connection failed')
                        finally:
                            connection.close()

                if db_name=='Y':
                    command = """./bin/ycsb.sh {load_or_run} jdbc 
                        -s -P ./yugabyte-binding/yugabyte.properties 
                        -P workloads/workload{workload_name} -p recordcount={recordcount_name} 
                        -p operationcount={operationcount_name} 
                    """.format(
                            workload_name=wl,
                            recordcount_name=rec,
                            operationcount_name=op,
                            load_or_run=lr
                        )
                elif db_name=='C':
                    command = """./bin/ycsb.sh {load_or_run} jdbc 
                        -s -P ./cockroach-binding/cockroach.properties 
                        -P workloads/workload{workload_name} -p recordcount={recordcount_name} 
                        -p operationcount={operationcount_name}
                    """.format(
                    workload_name=wl,
                    recordcount_name=rec,
                    operationcount_name=op,
                    load_or_run=lr
                     )
                else:
                    print('Invalid DB parameter!!')
                    exit(-1)
                output_file = "./log/lr_{load_or_run}-wl_{workload_name}-rc_{recordcount_name}-oc_{operationcount_name}.txt".format( workload_name=wl,
                        recordcount_name=rec,
                        operationcount_name=op,
                        load_or_run=lr)
                run_bash_command(command,directory,output_file)
            
                


import psycopg2

#Syntax for the setups array
arr = [{'Name': 'Sample', 'Dut': '192.168.1.10'}]

conn = psycopg2.connect(
    host="192.168.1.1", # hostname or IP of DB
    database="guacamole_db", # name od DB
    user="test", # any user with permissions
    password="test" # his password
)

#SSH
# ssh_insert_conn = "INSERT INTO guacamole_connection (connection_id, connection_name, parent_id, protocol, max_connections, max_connections_per_user, connection_weight, failover_only, proxy_port, proxy_hostname, proxy_encryption_method) VALUES ("+conn_id+", '" + arr[setup_id]['Name']  + "-"+arr[setup_id]['Dut']+"', NULL, 'ssh', NULL, NULL, NULL, 'f', NULL, NULL, NULL);"
# ssh_insert_conn_perm = "INSERT INTO guacamole_connection_permission (entity_id, connection_id, permission) VALUES (1, "+conn_id+", 'READ'), (1, "+conn_id+", 'UPDATE'), (1, "+conn_id+", 'DELETE'), (1, "+conn_id+", 'ADMINISTER');"
# ssh_insert_conn_param = "INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ("+conn_id+", 'enable-sftp', 'true'), ("+conn_id+", 'hostname', '" + arr[setup_id]['Dut'] + "'), ("+conn_id+", 'password', 'test'), ("+conn_id+", 'port', '22'), ("+conn_id+", 'username', 'test');"



#RDP
# rdp_insert_conn = "INSERT INTO guacamole_connection (connection_id, connection_name, parent_id, protocol, max_connections, max_connections_per_user, connection_weight, failover_only, proxy_port, proxy_hostname, proxy_encryption_method) VALUES ("+conn_id+", '" + guacamole_platforms[setup_id]['Name'] + "-"+guacamole_platforms[setup_id]['Controller IP']+"', NULL, 'rdp', NULL, NULL, NULL, 'f', NULL, NULL, NULL);"
# rdp_insert_conn_perm = "INSERT INTO guacamole_connection_permission (entity_id, connection_id, permission) VALUES (1, "+conn_id+", 'READ'), (1, "+conn_id+", 'UPDATE'), (1, "+conn_id+", 'DELETE'), (1, "+conn_id+", 'ADMINISTER');"
# rdp_insert_conn_param = "INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ("+conn_id+", 'hostname', '" + guacamole_platforms[setup_id]['Controller IP'] + "'), ("+conn_id+", 'password', 'test'), ("+conn_id+", 'console-audio', 'true'), ("+conn_id+", 'port', '3389'), ("+conn_id+", 'domain', 'example.org.com'), ("+conn_id+", 'normalize-clipboard', 'windows'), ("+conn_id+", 'security', 'nla'), ("+conn_id+", 'ignore-cert', 'true'), ("+conn_id+", 'resize-method', 'display-update'), ("+conn_id+", 'username', 'test');"
      

cursor = conn.cursor()
for i in range(len(arr)):
    conn_id = str(i + 1)
    setup_id = i
    ssh_insert_conn = "INSERT INTO guacamole_connection (connection_id, connection_name, parent_id, protocol, max_connections, max_connections_per_user, connection_weight, failover_only, proxy_port, proxy_hostname, proxy_encryption_method) VALUES ("+conn_id+", '" + arr[setup_id]['Name']  + "-"+arr[setup_id]['Dut']+"', NULL, 'ssh', NULL, NULL, NULL, 'f', NULL, NULL, NULL);"
    ssh_insert_conn_perm = "INSERT INTO guacamole_connection_permission (entity_id, connection_id, permission) VALUES (1, "+conn_id+", 'READ'), (1, "+conn_id+", 'UPDATE'), (1, "+conn_id+", 'DELETE'), (1, "+conn_id+", 'ADMINISTER');"
    ssh_insert_conn_param = "INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ("+conn_id+", 'enable-sftp', 'true'), ("+conn_id+", 'hostname', '" + arr[setup_id]['Dut'] + "'), ("+conn_id+", 'password', 'test'), ("+conn_id+", 'port', '22'), ("+conn_id+", 'username', 'test');"

    #print(ssh_insert_conn)
    #print(ssh_insert_conn_perm)
    #print(ssh_insert_conn_param)
    cursor.execute(ssh_insert_conn)
    cursor.execute(ssh_insert_conn_perm)
    cursor.execute(ssh_insert_conn_param)



conn.commit()
cursor.close()
conn.close()

# Overwiew

Had to add about 150 setups to the [guacamole](https://github.com/apache/guacamole-server) server so here is a script that will insert these from an array into a database.

I used `pyexcel` library to create the array out of an excel file. If you want to do it without entering the array and get your data straight from an excel file you can do that with `pandas`. 

Something like that should work
```python
platformList = pd.read_excel(r"EXCEL SETUPS PATH PATH")
platformList = platformList.set_index("Name")[["Dut"]].to_dict("index")
platformList = {k: [v["Dut"] for k, v in platformList.items()}
```
Here are the inserts used in the code
- RDP
```sql
INSERT INTO guacamole_connection (connection_id, connection_name, parent_id, protocol, max_connections, max_connections_per_user, connection_weight, failover_only, proxy_port, proxy_hostname, proxy_encryption_method) VALUES ("+conn_id+", '" + guacamole_platforms[setup_id]['Name'] + "-"+guacamole_platforms[setup_id]['Controller IP']+"', NULL, 'rdp', NULL, NULL, NULL, 'f', NULL, NULL, NULL);
INSERT INTO guacamole_connection_permission (entity_id, connection_id, permission) VALUES (1, "+conn_id+", 'READ'), (1, "+conn_id+", 'UPDATE'), (1, "+conn_id+", 'DELETE'), (1, "+conn_id+", 'ADMINISTER');
INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ("+conn_id+", 'hostname', '" + guacamole_platforms[setup_id]['Controller IP'] + "'), ("+conn_id+", 'password', 'test'), ("+conn_id+", 'console-audio', 'true'), ("+conn_id+", 'port', '3389'), ("+conn_id+", 'domain', 'example.org.com'), ("+conn_id+", 'normalize-clipboard', 'windows'), ("+conn_id+", 'security', 'nla'), ("+conn_id+", 'ignore-cert', 'true'), ("+conn_id+", 'resize-method', 'display-update'), ("+conn_id+", 'username', 'test');
```
- SSH
```sql
INSERT INTO guacamole_connection (connection_id, connection_name, parent_id, protocol, max_connections, max_connections_per_user, connection_weight, failover_only, proxy_port, proxy_hostname, proxy_encryption_method) VALUES ("+conn_id+", '" + guacamole_platforms[setup_id]['Name']  + "-"+guacamole_platforms[setup_id]['Dut IP']+"', NULL, 'ssh', NULL, NULL, NULL, 'f', NULL, NULL, NULL);
INSERT INTO guacamole_connection_permission (entity_id, connection_id, permission) VALUES (1, "+conn_id+", 'READ'), (1, "+conn_id+", 'UPDATE'), (1, "+conn_id+", 'DELETE'), (1, "+conn_id+", 'ADMINISTER');
INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ("+conn_id+", 'enable-sftp', 'true'), ("+conn_id+", 'hostname', '" + guacamole_platforms[setup_id]['Dut IP'] + "'), ("+conn_id+", 'password', 'test'), ("+conn_id+", 'port', '22'), ("+conn_id+", 'username', 'test');
```

# update-server.conf-using-python-file-operator

This is a task to demonstrate "file operator" capability in Python from DevOps perspective.

There is a db upgrade happening in the Organization and teh db port has been changed to a new db port via automation. This is a simple task and can be done manually with few steps.
As a DevOps Engineer, you have to be compliant and version control the tasks for future audits and best practices.

Lets leverage principle of automation to achieve this requirement.

Requirement/ User Story: As a DevOps Engineer I need to update server.conf file to update db port to a new db port as part of db upgrade.

Task: In the given server.conf file Update db_port from 3306 to db_port to 9306

Solution Steps:

1. Read the given server.conf file
2. Store the content of the file to a list
3. Open the file in "write" mode
4. Update the db_port property

server.config Before Running

[database]
db_host = 192.168.1.100
db_port=3306
db_user = admin
db_password = secret123
db_name = devops_db


Running the Script
python server_conf_updates.py

server.config After Running

[database]
db_host = 192.168.1.100
db_port=9306
db_user = admin
db_password = secret123
db_name = devops_db

# This script updates the db_port in the server.conf file to new db_port value as per upgrade instructions received from Database Engineering team

def server_conf_update(file_path, key, value): # file_path - path of the server.conf , key - property of the server.conf file to be updated, value is the variable to pass to the function
    
    
    with open(file_path, "r") as file:  # read the content of given server.conf file
        lines = file.readlines()
        
    with open(file_path, "w") as file:  # write or update the db_port value 
        for line in lines:
             if key in line:
                 file.write(key + " = "  + value + "\n")
             else:
                file.write(line)


# Path of the server.conf file
server_conf_file = "server.conf"

# key and new value to be updated
key = "db_port"
new_port = "9360"


server_conf_update("server.conf", "db_port", "9306") # update the server.conf file

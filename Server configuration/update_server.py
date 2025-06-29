def server_config(file_path,key,value):

    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    with open(file_path, 'w') as file:
         for line in lines:
             if key in line:
                 file.write(key + '=' + value + '\n') 
             else: 
                file.write(line)
key_value = "server_conf"
key = "MAX_CONNECTIONS"
value = "200"
server_config(key_value,key,value)

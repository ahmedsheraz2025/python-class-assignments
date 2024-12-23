user_names = ["ali","ahmed","bilal","umair","basit"]

def insert_value(user_names,index,value):
    user_names.insert(index, value)
    return user_names
insert_value(user_names, 3,"sami")
result = print(user_names)
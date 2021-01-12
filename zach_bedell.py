import yaml
info = [{'first_name': "Zach", "last_name":"Bedell", "company":"Boeing", "email":"zachary.bedell@boeing.com", "github_username":"okidailthief"}]

with open("new_file.yaml", 'w') as file:
    yaml.dump(info, file)

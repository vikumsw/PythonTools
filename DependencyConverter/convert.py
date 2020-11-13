import re

file1 = open('DependencyConverter\old.txt', 'r') 
Lines = file1.readlines() 
file2 = open('DependencyConverter\\new.txt', 'w') 

lenght = len(Lines)

count = 0
# Strips the newline character 
file2.writelines('dependencies = [\n')

for line in Lines:
    count = count+1
    #print("\t {{ \"project\": \"{}\", \"name\": \"{}\"}},\n".format("mtech_1","database_SOCI_Core"))

    tokens = line.strip().replace('\"','').replace('@','/').replace(', \\','').strip().split('/')
    #print(tokens)
    project = tokens[2]
    package = tokens[0]
    file2.writelines("\t {{ \"project\": \"{}\", \"name\": \"{}\"}}".format(project,package))
    if count != lenght:
        file2.writelines(",")

    file2.writelines("\n")

"database_SOCI_Core/4.20.0.t1@mtech_1/conan_testing", \


file2.writelines(']\n')

file2.close() 




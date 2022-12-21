#!/usr/bin/python3
################################################################################
# Remove id sequences from the file

################################################################################
#V1
# This will erease each line which is identical including sequence lines
################################################################################ 
'''
import re
#with open("TP53unique-db.txt", "w") as database_output:
    
with open("testdb.txt", "r") as database_file:      #Open the file in the script
                    
    database_lines = database_file.readlines()  # Create a list of each line in the script

    db_lines = []   #create an empty database with only unique fasta sequences    
    
    for line in database_lines:     #iterate over each line in the list. 

        if line not in db_lines:
            db_lines.append(line)
           
    print(db_lines)
        
database_file.close()
#database_output.close()

################################################################################
#V2
# This will erease the fasta sequence on check on header sequence
################################################################################ 
import re

with open("testdb.txt", "r") as database_file:      #Open the file in the script
                    
    database_lines = database_file.readlines()  # Create a list of each line in the script

    db_lines = []   #create an empty database with only unique fasta sequences 
    header_set = set()    # Create 
        

    for line in database_lines:     #iterate over each line in the list. 

        if re.search("^\>", line):
            
            if line not in header_set:
                header_set.add(line)
                db_lines.append(line)
                flag = 0
            else:
                flag = -1
                continue
          
        if flag == 0:
            db_lines.append(line)
        elif flag == -1:
            continue
        
print(header_set)
print(db_lines)
        
database_file.close()
'''
################################################################################
# V3
# Make it write the results to a dockx
################################################################################ 
import re

with open("TP53db", "r") as database_file:      #Open the file in the script

    w = open("TP53unique-db.txt", "w")

    database_lines = database_file.readlines()  # Create a list of each line in the script

    db_lines = []   #create an empty database with only unique fasta sequences 
    header_set = set()    # Create 
        

    for line in database_lines:     #iterate over each line in the list. 

        if re.search("^\>", line):
            
            if line not in header_set:
                header_set.add(line)
                #db_lines.append(line)
                flag = 0
            else:
                flag = -1
                continue
          
        if flag == 0:
            w.write(line)
        elif flag == -1:
            continue

w.close()        
database_file.close()

#with open("TP53unique-db.txt", "w") as output_file:
#
#
#    for line in db_lines:
#        
#        output_file.write(line)
#
#output_file.close()




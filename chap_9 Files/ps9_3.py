#write a program to generate multiplication tables from 2 to 20 and write it to the different files.
#place these files in a folder for a 13 year old

for i in range(2,21):
    table = ''
    for j in range(1,11):
        table = table + f"{i}X{j} = {i*j}\n"
    with open(f"tables/{i}.txt","w") as f:
        f.write(table)

import string 
import re
import json 
import pydoop.hdfs as hdfs 

def count_words(file, num=True):

    r = None

    if num:
        r = '[a-zA-Z0-9@\s]+'
    else:
        r = '[a-zA-ZA\s]+'

    d = {}
    w = []
    with open(file, 'r') as file:
        
        for line in file:
            line = line.lower()
            line = ''.join(re.findall(r, line))
            w += line.split()


    for words in w:
        d[words] = d.get(words,0) + 1

    return d



def send_file(file):
    print("Saving to HDFS")

    dest = 'hdfs://localhost:9000/Task-002/python_output.txt'
    hdfs.put(file, dest)
    print("Saved to HDFS")

def save_output(dic):
    dumps = json.dumps(dic, sort_keys = True, indent=4)
    with open('python_output.txt', "w") as file:
        file.write(dumps)
        

def main():
    print("Retrieving file: ")
    file = count_words('Shakespeare.txt')
    print("Reading the output")
    print("Saving the output")
    save_output(file)
    send_file("python_output.txt")
    print("Completed")
    print(file)


main()
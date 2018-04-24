#!/usr/bin/python
#coding:UTF-8

import codecs

def convert_read_file(path):
    with open(path, 'r') as files:
        lines = files.readlines()
        result = []
        flag= '密码：'
        trip_ = '\n'
        for file in lines:
            file_str =file.strip(trip_)
            cipher = {'cipher_no':file_str[file_str.find(flag,0,len(file_str))+len(flag):len(file_str)]}
            result.append(cipher)
        return result
    

if __name__ == '__main__':
   print convert_read_file('/home/facheng/backup/test.txt')
        


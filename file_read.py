#!/usr/bin/python
#coding:UTF-8

import codecs

def convert_read_file(path):
    with open(path, 'r') as files:
        lines = files.readlines()
        result = []
        flag= ''
        trip_ = '\n'
        for file in lines:
            file_str =file.strip(trip_)
            cipher = {'cipher_no':file_str[file_str.find(flag,0,len(file_str))+len(flag):len(file_str)],'bindSource':1, 'smsyzm':'775344', 'mobileNum':'18721975196','rnd':0.8444005282553888}
            #cipher = {'cipher_no':'57A8-3F9A-8283-2B4B','bindSource':1, 'smsyzm':'775344', 'mobileNum':'187','rnd':0.8619496435248866}
            result.append(cipher)
        return result
    

if __name__ == '__main__':
   print convert_read_file('/home/facheng/backup/test.txt')
        


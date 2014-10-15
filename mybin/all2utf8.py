#!/usr/bin/env python
# -*- coding=utf8 -*-

import chardet
import sys

# print sys.argv

filelist=sys.argv[1:]
# print filelist
# exit()
# open file

not_converted=[]
for ifile in filelist :
    # print ifile
    try:
        inputfile=open(ifile, 'r')

    except IOError:
        print "can not open file ", ifile
        continue

    # read file content
    content=inputfile.read()
    # print content
    encoding=chardet.detect(content)['encoding']
    inputfile.close()
    # print encoding
    # convert to utf8
    if encoding!='utf-8':
        content_utf8 = content.decode(encoding)
        print content_utf8
        ss=raw_input("is the content correct?")
        if ss=='y':
            outputfile=open(ifile,'w')
            outputfile.write(content_utf8.encode('utf-8'))
            outputfile.close()
        else:
            not_converted=not_converted.append(ss)
            continue

print "not converted files are", not_converted




# write to file

# print content_utf8.encode('utf8')
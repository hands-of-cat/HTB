#!/usr/bin/python3
import subprocess

input=input('> ').strip()
utf=[]
for i in input:
    utf.append("\\u00"+hex(ord(i)).split('x')[1])

pdata = ''.join(utf)

adata = "curl "
adata += "-X POST -H 'Content-Type: application/json;charset=utf-8' "
adata += "http://multimaster/api/getColleagues -d \"{\\\"name\\\":\\\""
adata += pdata
adata += "\\\"}\""

subprocess.run(adata, shell=True)

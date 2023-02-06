from django.shortcuts import render, redirect
import mysql.connector


fn=''
ln=''
s=''
em=''
pwd=''

# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        connection=mysql.connector.connect(
        host="localhost",
        database="website",
        port=3307,
        username="root",
        password="")

        cursor=connection.cursor()

        data=request.POST

        for key,value in data.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                fn=value
            if key=="sex":
                fn=value
            if key=="email":
                fn=value
            if key=="password":
                fn=value

        query="insert into users (first_name,last_name,sex,email,password) values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd) 
        # query="insert into users values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        
        cursor.execute(query)
        connection.commit()

    return render (request,"signup_page.html")


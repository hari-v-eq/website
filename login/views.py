from django.shortcuts import render
import mysql.connector

em=''
pwd=''

# Create your views here.
def loginaction(request):
    global em,pwd
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
           
            if key=="email":
                fn=value
            if key=="password":
                fn=value
            
        query="select * from users where email ='{}' and password='{}'".format(em,pwd)
        
        cursor.execute(query)
        t=tuple(cursor.fetchall())
        if t==():
            return render (request,"error.html")
        else:
            return render(request,"welcome.html")

    return render (request,"login_page.html")

 
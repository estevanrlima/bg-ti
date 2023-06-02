from django.shortcuts import render
import mysql.connector

def connect_db():
    my_db = mysql.connector.connect(
        host="bgtreinamentos.mysql.pythonanywhere-services.com",
        user="bgtreinamentos",
        password="Bgdata.2022",
        database="bgtreinamentos$bgrecords"
    )
    return my_db

def index(request):

    db = connect_db()

    return render(request, 'tests/index.html', {db: db})
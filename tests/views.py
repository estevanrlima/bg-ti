from django.shortcuts import render
import mysql.connector

def connect_db():
    my_db = mysql.connector.connect(
        host="bgtreinamentos.mysql.pythonanywhere-services.com",
        user="bgtreinamentos",
        password="Bgdata.2022",
        database="bgtreinamentos$bgrecords"
    )

    cursor = my_db.cursor()
    cursor.execute("SELECT UserEmail FROM HadRecords")
    email = cursor.fetchone()  # Fetch the first row
    cursor.close()
    my_db.close()

    return email[0] if email else None

def index(request):

    email = connect_db()

    return render(request, 'tests/index.html', {'db': email})
from flask import Flask ,render_template,request,redirect,url_for
app=Flask(__name__)
import psycopg
conn=psycopg.connect(
            host="localhost",
            user="postgres",
            dbname="rohan",
            password="12345"

        )
cur=conn.cursor()


@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        choice=request.form["choice"]
        if choice=="principal":
            return redirect(url_for("password"))
        elif choice=="teacher":
            return redirect(url_for("teacher"))
        elif choice=="student":
            return redirect(url_for("student"))
        elif choice=="parents":
            return("IN PROGRESS")
        else:
            return ("invalid input!")
    return render_template("login.html")

@app.route("/student",methods=["POST","GET"])
def student():
    if request.method=="POST":
        choice=request.form["choice"]
        if choice=="view timetable":
            return redirect(url_for("viewtimetable"))
        elif choice=="view results":
            return redirect(url_for("viewresults"))
    return render_template("student.html")

@app.route("/viewresults",methods=["POST","GET"])
def viewresults():
    if request.method=="POST":
         cur.execute(
             "SELECT rollno,exam_result FROM result"
         )
         result=cur.fetchall()
    return render_template("viewresults.html",result=result)



@app.route("/viewtimetable",methods=["POST","GET"])
def viewtimetable():
    if request.method=="GET":
        cur.execute(
            "SELECT sub,date,venue FROM timetable"
        
        )
        tb=cur.fetchall()

    return render_template("viewtimetable.html",tb=tb)

@app.route("/teacher",methods=["POST","GET"])
def teacher():
    if request.method=="POST":
        choice=request.form["choice"]
        if choice=="timetable":
            return redirect (url_for("timetable"))
        elif choice=="syllabus":
            return redirect (url_for("syllabus"))
        elif choice=="upload result":
            return redirect (url_for("uploadresult"))
        else:
            return("invalid input")
    return render_template("teacher.html")

@app.route("/uploadresult",methods=["POST","GET"])
def uploadresult():
    if request.method=="POST":

        rollno=request.form["rollno"]
        exam_result=request.form["exam_result"]

        cur.execute(
            "INSERT INTO result (rollno,exam_result) VALUES(%s,%s)",
            (rollno,exam_result)
        )

        conn.commit()
    return render_template("uploadresult.html")


@app.route("/timetable",methods=["GET","POST"])
def timetable():
    if request.method=="POST":
        sub=request.form["subject"]
        date=request.form["date"]
        venue=request.form["venue"]
        
        cur.execute(
            "INSERT INTO timetable (sub,date,venue) VALUES(%s,%s,%s)",
            (sub,date,venue)
        )
        
        conn.commit()
        
        return ("sucessfully update!")
    return render_template("timetable.html")

@app.route("/syllabus",methods=["GET","POST"])
def syllabus():
    if request.method=="POST":

     return ("in progress")
    return render_template("syllabus.html")
        
            

@app.route("/principal password",methods=["GET","POST"])
def password():
    if request.method=="POST":
      password=request.form["password"]
      if password=="rohan":
          return redirect (url_for("principal"))
      else:
          return ("incorrect password")
    return render_template("password.html")

@app.route("/principal",methods=["GET","POST"])
def principal():
    if request.method=="POST":
       



        choice=request.form["choice"]
        
           
        if choice=="add teacher":
            return redirect(url_for("add"))
        elif choice=="del teacher":
            return redirect(url_for("delete"))
        elif choice=="update teacher":
            return redirect(url_for("update"))
        elif choice=="salary status":
            return redirect(url_for("viewstatus"))
            
            
            
    return render_template("principal.html")



@app.route("/add",methods=["GET","POST"])
def add():
    if request.method=="POST":
        name=request.form["name"]
        age=int(request.form["age"])
        gender=request.form["gender"]
        salary=int(request.form["salary"])
        subject=request.form["subject"]
        salary_status=request.form["status"]

        cur.execute(
         "INSERT INTO teachers(name,age,gender,salary,subject,salary_status) VALUES(%s,%s,%s,%s,%s,%s)",
          (name,age,gender,salary,subject,salary_status)
         )
        conn.commit()  
        return ("added sucessfully!")
    
    return render_template("add.html")


@app.route("/del",methods=["GET","POST"])
def delete():
    if request.method=="POST":
       name=request.form["name"]
       cur.execute(
        "DELETE FROM teachers  WHERE name=%s ",
        (name,)
       )
       conn.commit()
       return ("TEACHER REMOVED SUCESSFULLY!")
    return render_template("del.html")

@app.route("/update",methods=["GET","POST"])
def update():
    if request.method=="POST":
        name=request.form["name"]
        id=int(request.form["id"])
        cur.execute(
            "UPDATE teachers SET name=%s WHERE id=%s" ,
            (name,id)

        )
        conn.commit()
        return("updated sucessfully!")
    return render_template("update.html")
@app.route("/salary_status",methods=["GET","POST"])
def viewstatus():
    if request.method=="GET":
        cur.execute(
            "SELECT name ,salary , salary_status ,subject FROM teachers"
        )
        rows=cur.fetchall()
        
    return render_template("viewstatus.html",rows=rows)


app.run(debug=True) 

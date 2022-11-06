from flask import *
from dbm import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Author')
def Author():
    return render_template('/Author.html')

@app.route('/user')
def user():
    return render_template('/user.html')

@app.route('/addpost')
def addpost():
    return render_template('/addpost.html')

@app.route('/post')
def post():
    return render_template('/post.html')

@app.route('/uaddpost')
def uaddpost():
    return render_template('/uaddpost.html')

@app.route('/uhome')
def uhome():
    return render_template('/uhome.html')

# USER DATABASE

@app.route('/uinsertdata',methods=['post'])
def uinsertdata():
    fname = request.form['userfname']
    lname = request.form['userlname']
    email = request.form['useremail']
    password = request.form['userpassword']
    mobile = request.form['usermobile']
    city = request.form['usercity']
    data = (fname,lname,email,password,mobile,city)
    uinsert(data)
    print("Record inserted!")
    return redirect('/user')

@app.route("/udetails")
def udetails():
    d = showudata()
    return render_template("udetails.html",ulist = d)

@app.route('/uedit')
def uedit():
    email = request.args.get('email')
    data = ueditdetails(email)
    return render_template('uedit.html',t = data[0])

@app.route('/uupdatedata',methods=['post'])
def uupdatedata():
    fname = request.form['userfname']
    lname = request.form['userlname']
    email = request.form['useremail']
    password = request.form['userpassword']
    mobile = request.form['usermobile']
    city = request.form['usercity']
    t = (fname,lname,email,password,mobile,city,email)
    uupdate(t)
    return redirect('/user')

@app.route("/udelete")
def udelete():
    email = request.args.get('email')
    udrop(email)
    return redirect("/udetails")

@app.route('/ulogin',methods=["post"])
def ulogin():
    email = request.form['uemail']
    password = request.form['upassword']
    t = (email,password)
    t1 = uloginbyemail(email)
    if t in t1:
        return redirect('/uhome')
    else:
        return redirect('/user')





# AUTHOR DATABASE

@app.route('/ainsertdata',methods=['post'])
def ainsertdata():
    authorfname = request.form['authorfname']
    authorlname = request.form['authorlname']
    authoremail = request.form['authoremail']
    authorpassword = request.form['authorpassword']
    authormobile = request.form['authormobile']
    authorcity = request.form['authorcity']
    data = (authorfname,authorlname,authoremail,authorpassword,authormobile,authorcity)
    ainsert(data)
    print("Record inserted!")
    return redirect('/Author')

@app.route("/adetails")
def adetails():
    d = showadata()
    return render_template("adetails.html",alist = d)

app.route("/udetails")
def udetails():
    d = showudata()
    return render_template("udetails.html",ulist = d)

@app.route('/aedit')
def aedit():
    email = request.args.get('email')
    data = aeditdetails(email)
    return render_template('aedit.html',t = data[0])

@app.route('/aupdatedata',methods=['post'])
def aupdatedata():
    fname = request.form['authorfname']
    lname = request.form['authorlname']
    email = request.form['authoremail']
    password = request.form['authorpassword']
    mobile = request.form['authormobile']
    city = request.form['authorcity']
    t = (fname,lname,email,password,mobile,city,email)
    aupdate(t)
    return redirect('/adetails')

@app.route("/adelete")
def adelete():
    email = request.args.get('email')
    adrop(email)
    return redirect("/adetails")

@app.route('/alogin',methods=["post"])
def alogin():
    email = request.form['aemail']
    password = request.form['apassword']
    t = (email,password)
    t1 = aloginbyemail(email)
    if t in t1:
        return redirect('/addpost')
    else:
        return redirect('/Author')





# BLOG

@app.route('/binsertdata',methods=['post'])
def binsertdata():
    bname = request.form['bname']
    btitle = request.form['btitle']
    bblog = request.form['bblog']
    bdata = (bname,btitle,bblog)
    binsert(bdata)
    print("Record inserted!")
    return redirect('/addpost')

@app.route("/bdetails")
def bdetails():
    d = showbdata()
    return render_template("bdetails.html",blist = d)

@app.route("/bdetails1")
def bdetails1():
    d = showbdata1()
    return render_template("bdetails1.html",blist = d)

@app.route('/bedit')
def bedit():
    name = request.args.get('name')
    data = beditdetails(name)
    return render_template('bedit.html',t = data[0])

@app.route('/bupdatedata',methods=['post'])
def bupdatedata():
    name = request.form['bname']
    title = request.form['btitle']
    blog = request.form['bblog']
    t = (name,title,blog)
    print(t)
    bupdate(t)
    return redirect('/bedit')

@app.route("/bdelete")
def bdelete():
    name = request.args.get('name')
    bdrop(name)
    return redirect("/bdetails")

if __name__ == "__main__":
    app.run(debug=True)
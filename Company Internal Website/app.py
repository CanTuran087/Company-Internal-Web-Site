from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import pypyodbc
import hashlib
import json
import query, ifMethod

app = Flask(__name__)
app.static_folder = 'static'
app.template_folder = 'template'
app.secret_key = 'gizli_anahtar'

def connection():

    s = '' #Server Name
    d = '' #Database NAme
    u = '' #Username
    p = '' #Password

    cstr = 'DRIVER={SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD=' + p
    print(cstr)
    conn = pypyodbc.connect(cstr)
    return conn

@app.route("/")
def main():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    birthdayList = []
    announcementList = []

    conn = connection()
    cursor = conn.cursor()
    cursor.execute(query.sqlQuery(1))

    for row in cursor.fetchall():
        birthdayList.append(
            {
                "NAME": row[0],
                "YAS": row[3],
                "KACGUNKALDI": row[4]
            })
    
    cursor.execute(query.sqlQuery(4))

    for row2 in cursor.fetchall():
        base64Files = [row2[i] for i in range(1, 31)]
        margedBase64 = ''.join(base64Files)

        announcementList.append({
            "STEXT": row2[0],
            "BASE64FILE": margedBase64,
            "ID": row2[32]
        })

    if announcementList == []:
        announcementList.append({
            "STEXT": "Duyuru Bulunmamaktadır",
            "BASE64FILE": "static/img/efecanias.jpg",
            "ID":""
        })

    cursor.execute(query.sqlQuery(7))
    results = cursor.fetchall()
    base64Files_2 = [result[i] for result in results for i in range(30)]

    if base64Files_2:
        margedBase64_2 = ''.join(base64Files_2)
    else:
        margedBase64_2 = 'static/img/employes.jpg'
    
    return render_template("home.html", birthday=birthdayList, announcement=announcementList, employeeIMG = margedBase64_2)


@app.route("/birthday")
def birthday():
    birthdayList = []

    conn = connection()
    cursor = conn.cursor()
    cursor.execute(query.sqlQuery(1))

    for row in cursor.fetchall():
        base64Files = [row[i] for i in range(5, 35)]
        margedBase64 = ''.join(base64Files)

        birthdayList.append(
            {
                "NAME": row[0],
                "BIRTHDAY": row[1],
                "EMAIL": row[2],
                "YAS": row[3],
                "KACGUNKALDI": row[4],
                "BASE64FILE": margedBase64
            })

    return render_template("birthday.html", birthday=birthdayList)

@app.route("/employee")
def employee():
    employeeList = []

    conn = connection()
    cursor = conn.cursor()
    cursor.execute(query.sqlQuery(6))

    for row in cursor.fetchall():
        employeeList.append(
            {
                "NAME": row[0],
                "COMPANY": row[1],
                "PLANT": row[2],
                "STEXT": row[3],
                "EMAIL": row[4],
                "BLOODTYPE": row[5],
                "WIRELESSPHONE": row[6]
            })

    return render_template("employee.html", employee=employeeList)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    conn = connection()
    cursor = conn.cursor()

    cursor.execute(query.sqlQuery(8))
    results = cursor.fetchall()
    base64Files = [result[i] for result in results for i in range(30)]

    if base64Files:
        margedBase64 = ''.join(base64Files)
    else:
        margedBase64 = 'static/img/about-efe.jpg';
    
    cursor.execute(query.sqlQuery(9))

    aboutTextResult = cursor.fetchone()

    if aboutTextResult:
        aboutText = aboutTextResult[0]
    else:
        aboutText = """ """; # Sample About Us Text
    
    return render_template("about.html", mergeBase64 = margedBase64, aboutStext = aboutText)

@app.route("/management-login")
def managementLogin():
    return render_template("management-login.html")

@app.route("/loginUp", methods=["GET", "POST"])
def loginUp():
    error = None
    username = request.form['username']
    password = request.form['password']
    userControl = []

    if request.method == "POST":
        if username == '' or password == '':
            error = "Boş Alanları Doldurunuz !"
        else:
            conn = connection()
            cursor = conn.cursor()

            if username == 'USER1' or username == 'USER2': #Sadece İlgili Kişiler Girebilir

                sha256_obj = hashlib.sha256(str(password).encode())
                pass1 = sha256_obj.hexdigest()
                cursor.execute(query.sqlQuery(2, username, pass1))
                userControl = cursor.fetchall()

                if userControl != []:
                    session['username'] = username
                    return redirect(url_for('management'))
                else:
                    error = "Parola Hatalı !"

            else:
                error = "Sadece İlgili Kişiler Bu Panele Girebilir"

    return render_template("management-login.html", errors=error)

@app.route("/management")
def management():
    employeeList = []
    announcementList = []
    username = session.get("username")

    conn = connection()
    cursor = conn.cursor()
    cursor.execute(query.sqlQuery(10))

    for row in cursor.fetchall():
        employeeList.append(
            {
                "NAME": row[0]
            })
    
    cursor.execute(query.sqlQuery(4))

    for row in cursor.fetchall():
        base64Files = [row[i] for i in range(1, 31)]
        margedBase64 = ''.join(base64Files)

        announcementList.append({
            "STEXT": row[0],
            "BASE64FILE": margedBase64,
            "FILENAME": row[31],
            "ID": row[32],
            "CREATEDBY": row[33],
            "CREATEDAT": row[34],
        })

    return render_template("management.html", employeeLists = employeeList, announcementLists = announcementList, username=username)

@app.route("/managementAnnouncement", methods=["POST"])
def managementAnnouncement():
    substrings = []
    username = session.get("username")

    if request.method == "POST":
        data = request.json
        base64img = data.get("base64img")
        filePath = data.get("filePath")
        base64img2 = data.get("base64img2")
        filePath2 = data.get("filePath2")
        base64img3 = data.get("base64img3")
        filePath3 = data.get("filePath3")
        base64img4 = data.get("base64img4")
        filePath4 = data.get("filePath4")
        base64img5 = data.get("base64img5")
        filePath5 = data.get("filePath5")
        textParagraphAbout = data.get("textParagraphAbout")
        textParagraphAnnouncement = data.get("textParagraphAnnouncement")
        textParagraphManagementAnnouncement = data.get("textParagraphManagementAnnouncement")
        tableIdInput = data.get("tableIdInput")
        check = data.get("check")
        employee = data.get("employee")
        employeeUserName = data.get("employeeUserName")

        if base64img != "" and base64img != " " and base64img is not None:
            ifMethod.ifMethod(1, base64img, substrings, connection(), username, filePath)

        if base64img2 != "" and base64img2 != " " and base64img2 is not None:
            ifMethod.ifMethod(2, base64img2, connection(), username, employee, employeeUserName, filePath2)

        if (base64img3 != "" and base64img3 != " " and base64img3 is not None) or (textParagraphAbout != '' and textParagraphAbout != '<br>' and textParagraphAbout is not None):
            ifMethod.ifMethod(3, base64img3, connection(), username, filePath3, textParagraphAbout)

        if (base64img4 != "" and base64img4 != " " and base64img4 is not None) or (textParagraphAnnouncement != '' and textParagraphAnnouncement != '<br>' and textParagraphAnnouncement is not None):
            ifMethod.ifMethod(4, base64img4, connection(), textParagraphAnnouncement, username, filePath4)

        if (tableIdInput != "" and (base64img5 != "" and base64img5 != " " and base64img5 is not None)) or (tableIdInput != "" and textParagraphManagementAnnouncement != '' and textParagraphManagementAnnouncement != '<br>' and textParagraphManagementAnnouncement is not None):
            ifMethod.ifMethod(5, base64img5, connection(), textParagraphManagementAnnouncement, username, filePath5, tableIdInput)

        if tableIdInput != "" and check == "okey":
            ifMethod.ifMethod(6, connection(), tableIdInput)
    
    else:
        print("Yanlış HTTP isteği türü")
        return jsonify({"success": False})


@app.route("/managementAnnouncementDetailButton", methods=["POST"])
def managementAnnouncementDetailButton():
    localAnnouncementID = request.json.get('localAnnouncementID')
    session['localAnnouncementID'] = localAnnouncementID

    data_for_js = {'key1': localAnnouncementID}
    """json_data = json.dumps(data_for_js)
    print(json_data)"""
    return jsonify(data_for_js)


@app.route("/management-announcement-detail")
def managementAnnouncementDetail():
    conn = connection()
    cursor = conn.cursor()
    margedBase64 = ""
    base64FilePath = ""
    detailStext = ""
    localAnnouncementID = None
    localAnnouncementID = session.get("localAnnouncementID")
    announcementDetailControl = []
    announcementDetail = []

    print("Adım 1 : " + localAnnouncementID)

    cursor.execute(query.sqlQuery(22, localAnnouncementID))
    announcementDetailControl = cursor.fetchone()

    if localAnnouncementID != "" and announcementDetailControl is not None:
        cursor.execute(query.sqlQuery(24, localAnnouncementID))
        print(query.sqlQuery(24, localAnnouncementID))

        for row in cursor.fetchall():
            base64Files = [row[i] for i in range(9, 38)]
            margedBase64 = ''.join(base64Files)
            announcementDetail.append(row[8])
            base64FilePath = str(announcementDetail[0])
            announcementDetail = []
            announcementDetail.append(row[2])
            detailStext = str(announcementDetail[0])

    return render_template("management-announcement-detail.html", margedBase64 = margedBase64, base64FilePath = base64FilePath, detailStext = detailStext)


@app.route("/managementAnnouncementDetailSave", methods=["POST"])
def managementAnnouncementDetailSave():
    username = session.get("username")

    if request.method == "POST":
        data = request.json
        base64img6 = data.get("base64img6")
        filePath6 = data.get("filePath6")
        textParagraphAnnouncementDetail = data.get("textParagraphAnnouncementDetail")
        localIMGSrc = data.get("localIMGSrc")
        localParagraph = data.get("localParagraph")
        localAnnouncementID = data.get("localAnnouncementID")
        localFilePath = data.get("localFilePath")

        if localAnnouncementID == "" or localAnnouncementID is not None:
            ifMethod.ifMethod(7, connection(), base64img6, filePath6, textParagraphAnnouncementDetail, localIMGSrc, localParagraph, localFilePath, username)
        
        else:
            ifMethod.ifMethod(8, connection(), base64img6, filePath6, textParagraphAnnouncementDetail, localIMGSrc, localParagraph, localAnnouncementID, localFilePath, username)
    
    else:
        print("Yanlış HTTP isteği türü")
        return jsonify({"success": False})
    

@app.route('/ShowAnnouncementDetail', methods=["GET", "POST"])
def ShowAnnouncementDetail():
    announcementID = None
    
    if request.method == "POST":
        data = request.json
        announcementID = data.get("globalID")
        session['announcementID'] = str(announcementID)
        
        return redirect(url_for('announcementDetail'))

@app.route("/announcement-detail")
def announcementDetail():
    announcementID = str(session.get("announcementID"))
    conn = connection()
    cursor = conn.cursor()
    margedBase64 = ""
    detailMargedBase64 = ""
    stext = ""
    detailStext = ""
    nextAnnouncement = []
    margedBase64_2 = ""
    
    cursor.execute(query.sqlQuery(25, announcementID))

    for row in cursor.fetchall():
        base64Files = [row[i] for i in range(9, 38)]
        margedBase64 = ''.join(base64Files)
        stext = row[2]


    cursor.execute(query.sqlQuery(24, announcementID))

    for row in cursor.fetchall():
        base64Files = [row[i] for i in range(9, 38)]
        detailMargedBase64 = ''.join(base64Files)
        detailStext = row[2]
        

    cursor.execute(query.sqlQuery(26, announcementID))

    for row in cursor.fetchall():
        base64Files = [row[i] for i in range(2, 31)]
        margedBase64_2 = ''.join(base64Files)
        
        nextAnnouncement.append({
            "ID": row[0],
            "STEXT": row[1],
            "BASE64FILE": margedBase64_2,
        })

    return render_template("announcement-detail.html", margedBase64=margedBase64, stext=stext, detailMargedBase64=detailMargedBase64, detailStext=detailStext, nextAnnouncement=nextAnnouncement)

if __name__ == '__main__':
    app.run(debug=True)
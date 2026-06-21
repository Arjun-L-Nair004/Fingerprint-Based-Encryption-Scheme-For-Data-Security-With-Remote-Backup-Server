from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
from myapp.models import *


def login(request):
    request.session['lid']=""
    return render(request,'index.html')

def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    lg=Login.objects.filter(username=username,password=password)
    if lg.exists():
        lg1=Login.objects.get(username=username,password=password)
        request.session['lid']=lg1.id
        if lg1.type=="admin":
            return HttpResponse('''<script>alert('Admin login successful!');
            window.location='/FST/admin_home'</script>''')
        elif lg1.type=="user":
            return HttpResponse('''<script>alert('User login successful!');
                        window.location='/FST/user_home'</script>''')
        else:
            return HttpResponse('''<script>alert('Login unsuccessful!');window.location='/FST/login'</script>''')

    else:
        return HttpResponse('''<script>alert('User does not exist!');window.location='/FST/login'</script>''')


def logout(request):
        request.session['lid']= ''
        return HttpResponse('''<script>alert('Logged Out !');window.location='/FST/login/'</script>''')


#admin

def admin_home(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')
    return render(request,'Admin/adminindex.html')






def changepassword(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    return render(request,'Admin/Changepswd.html')

def changepswd_post(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    oldpassword=request.POST['textfield']
    newpassword=request.POST['textfield2']
    confirmpassword=request.POST['textfield3']
    cp=Login.objects.filter(password=oldpassword,id=request.session['lid'])
    if cp.exists():
        r=Login.objects.get(password=oldpassword,id=request.session['lid'])
        if newpassword==confirmpassword:
            cp1 = Login.objects.filter(password=oldpassword,id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert('Password Updated successfully!');
                window.location='/FST/login'</script>''')
        else:
            return HttpResponse('''<script>alert('Password Mismatch!');
                    window.location='/FST/admin_home'</script>''')
    else:
        return HttpResponse('''<script>alert('User not Found!');
                window.location='/FST/admin_home'</script>''')


def sendreply(request,id):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    return render(request, 'Admin/Sendreply.html',{"cid":id})

def sendreply_post(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    Reply=request.POST['textfield']
    cid=request.POST['id']
    rep=Complaint.objects.filter(id=cid).update(status="Replied",reply=Reply)
    return HttpResponse('''<script>alert('Replied!');
                    window.location='/FST/viewcomp'</script>''')


def viewcomp(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    comp= Complaint.objects.all()
    return render(request,'Admin/viewcomplaint.html',{"data":comp})


def viewcomplaint_post(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    fromdt=request.POST['textfield']
    todt=request.POST['textfield2']
    comp = Complaint.objects.filter(date__range=[fromdt,todt])
    return render(request, 'Admin/viewcomplaint.html', {"data": comp})


def viewfeed(request):

    if request.session['lid'] == '':
        return redirect('/FST/login/')

    feed=Feedback.objects.all()
    return render(request,'Admin/viewfeed.html',{"data":feed})


def viewfeed_post(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')


    fromdat=request.POST['textfield']
    todat=request.POST['textfield2']
    feed = Feedback.objects.filter(date__range=[fromdat,todat])
    return render(request, 'Admin/viewfeed.html', {"data": feed})

def viewrev_rat(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    rev=Review.objects.all()
    return render(request,'Admin/Viewreview&rating.html',{"data":rev})


def viewrev_rat_post(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    revfrom=request.POST['textfield']
    revto=request.POST['textfield2']
    rev = Review.objects.filter(date__range=[revfrom,revto])
    return render(request, 'Admin/Viewreview&rating.html', {"data": rev})


def viewusers(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    res=User.objects.all()
    return render(request,'Admin/Viewusers.html',{"data":res})

def viewusers_post(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    uname=request.POST['textfield']
    res = User.objects.filter(name__icontains=uname)
    return render(request, 'Admin/Viewusers.html', {"data": res})



#User


def user_home(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    return render(request,'User/userindex.html')


def changepassword_user(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    return render(request,'User/Changepswd.html')


def changepassword_post(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    oldpassword=request.POST['textfield']
    newpassword=request.POST['textfield2']
    confirmpassword=request.POST['textfield3']
    cp = Login.objects.filter(password=oldpassword, id=request.session['lid'])
    if cp.exists():
        r = Login.objects.get(password=oldpassword, id=request.session['lid'])
        if newpassword == confirmpassword:
            cp1 = Login.objects.filter(password=oldpassword, id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert('Password Updated successfully!');
                    window.location='/FST/login'</script>''')
        else:
            return HttpResponse('''<script>alert('Password Mismatch!');
                        window.location='/FST/admin_home'</script>''')
    else:
        return HttpResponse('''<script>alert('User not Found!');
                    window.location='/FST/admin_home'</script>''')


def download(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')
    res=Upload.objects.filter(USER__LOGIN__id=request.session['lid'])
    return render(request,'User/Download.html',{"data":res})


def editprofile(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')
    eobj= User.objects.get(LOGIN_id=request.session['lid'])
    return render(request, 'User/edit profile.html', {"data":eobj})




def editprofile_post(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    name=request.POST['textfield']
    place=request.POST['textfield2']
    district=request.POST['textfield3']
    state=request.POST['textfield4']
    pin=request.POST['textfield5']
    gender=request.POST['radio']
    email=request.POST['textfield6']
    phoneno=request.POST['textfield7']
    dob=request.POST['textfield8']

    if 'fileField' in request.FILES:


        photo=request.FILES['fileField']

        fs = FileSystemStorage()
        date = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        fs.save(date, photo)
        path = fs.url(date)

        robj = User.objects.get(LOGIN__id=request.session['lid'])
        robj.name = name
        robj.place = place
        robj.district = district
        robj.state = state
        robj.pin = pin
        robj.gender = gender
        robj.email = email
        robj.phone = phoneno
        robj.dob = dob
        robj.photo = path
        robj.save()
    else:

        robj = User.objects.get(LOGIN__id=request.session['lid'])
        robj.name = name
        robj.place = place
        robj.district = district
        robj.state = state
        robj.pin = pin
        robj.gender = gender
        robj.email = email
        robj.phone = phoneno
        robj.dob = dob
        robj.save()


    return HttpResponse('''<script>alert('Updated Succesfully!');
                    window.location='/FST/viewprof'</script>''')


def sendcomp(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    return render(request,'User/Send COMP&7RPLY.html')

def sendcomp_post(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    complaint=request.POST['textfield']
    sc=Complaint()
    sc.date=datetime.now()
    sc.complaint=complaint
    sc.reply='Pending'
    sc.status='Pending'
    sc.USER=User.objects.get(LOGIN_id=request.session['lid'])
    sc.save()
    return HttpResponse('''<script>alert('Complaint Send!');
                    window.location='/FST/user_home'</script>''')

def sendfeed(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    return render(request,'User/Sendfeed.html')

def sendfeed_post(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    feed=request.POST['textfield']
    sf=Feedback()
    sf.date=datetime.now()
    sf.feedback=feed
    sf.USER=User.objects.get(LOGIN_id=request.session['lid'])
    sf.save()
    return HttpResponse('''<script>alert('Feedback Send!');
                    window.location='/FST/user_home'</script>''')



def sendrev_rat(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    return render(request,'User/Sendrev&rat.html')

def sendrev_rat_post(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    rev=request.POST['textfield']
    rat=request.POST['textfield2']
    sr=Review()
    sr.date=datetime.now()
    sr.review=rev
    sr.rating=rat
    sr.USER=User.objects.get(LOGIN_id=request.session['lid'])
    sr.save()
    return HttpResponse('''<script>alert('Thank You For your Response!');
                    window.location='/FST/user_home'</script>''')



def udetails(request):

    return render(request,'User/userreg.html')

def udetails_post(request):
    # if request.session['lid'] == '':
    #     return redirect('/FST/login/')


    name=request.POST['textfield']
    place=request.POST['textfield2']
    district=request.POST['textfield3']
    state=request.POST['textfield4']
    pin=request.POST['textfield5']
    gender=request.POST['radio']
    email=request.POST['textfield6']
    phoneno=request.POST['textfield7']
    dob=request.POST['textfield8']
    psw=request.POST['textfield9']
    cpsw=request.POST['textfield10']
    photo=request.FILES['fileField']

    import random
    lobj=Login()
    lobj.username=email
    lobj.password=psw
    lobj.type='user'
    lobj.save()


    fs=FileSystemStorage()
    date=datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    fs.save(date,photo)
    path=fs.url(date)


    robj=User()
    robj.name=name
    robj.place=place
    robj.district=district
    robj.state=state
    robj.pin=pin
    robj.gender=gender
    robj.email=email
    robj.phone=phoneno
    robj.dob=dob
    robj.photo=path
    robj.LOGIN=lobj
    robj.save()
    return HttpResponse('''<script>alert('Registered Succesfully!');
                    window.location='/FST/login'</script>''')



def upload(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    return render(request,'User/upload.html')




def upload_post(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')
    choosefile = request.FILES['fileField']
    fingile = request.FILES['fing']

    fs = FileSystemStorage()
    date = datetime.now().strftime("%Y%m%d%H%M%S") + choosefile.name
    filepath = fs.save(date, choosefile)
    path = fs.url(filepath)




    ##########

    import boto3


    # Creating an S3 access object
    obj = boto3.client("s3")
    # Uploading a png file to S3 in
    # 'mygfgbucket' from local folder
    obj.upload_file(
        Filename="C:\\Users\\noufa\\PycharmProjects\\FBESFDSWRBS\\media\\"+date,
        Bucket="dsvarfst",
        Key=date
    )




    ##########



    fs1 = FileSystemStorage()
    date1 = "fing"+datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    filepath1 = fs1.save(date1, fingile)
    path2 = fs.url(filepath1)




    #############################################
    import cv2
    import fingerprint_feature_extractor
    import math
    import numpy as np
    from scipy.spatial import Delaunay
    import hashlib
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import padding
    import os

    img = cv2.imread('C:\\Users\\noufa\\PycharmProjects\\FBESFDSWRBS\\media\\'+date1, 0)

    FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(
        img, spuriousMinutiaeThresh=10, invertImage=False, showResult=True, saveResult=True
    )

    print("Bifurcations:", FeaturesBifurcations)
    print("Terminations:", FeaturesTerminations)

    pp = []

    def distance(p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    def find_angle(A, B, C):
        a = distance(B, C)
        b = distance(A, C)
        c = distance(A, B)

        angle_A = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
        angle_A_degrees = math.degrees(angle_A)
        return angle_A_degrees

    for idx, curr_minutiae in enumerate(FeaturesTerminations):
        pp.append([curr_minutiae.locX, curr_minutiae.locY])

    for idx, curr_minutiae in enumerate(FeaturesBifurcations):
        pp.append([curr_minutiae.locX, curr_minutiae.locY])

    points = np.array(pp)

    tri = Delaunay(points)

    k=""

    print("Delaunay Triangulation Points:")
    for i in tri.points:
        print(i)

    angle_sum_list = []

    secret_key = os.urandom(32)
    iv = os.urandom(16)

    def aes_encrypt(data, key, iv):

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data.encode()) + padder.finalize()

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        return encrypted_data

    for i in tri.simplices:
        A = tri.points[i[0]]
        B = tri.points[i[1]]
        C = tri.points[i[2]]

        angle_A = find_angle(A, B, C)
        angle_B = find_angle(B, C, A)
        angle_C = find_angle(C, A, B)

        print(f"Angles of triangle {i}:")
        print(f"Angle at A: {math.floor(angle_A)} degrees")
        print(f"Angle at B: {math.floor(angle_B)} degrees")
        print(f"Angle at C: {math.floor(angle_C)} degrees")

        distance_AB = distance(A, B)
        distance_BC = distance(B, C)
        distance_CA = distance(C, A)

        print(f"Distances between points A, B, C:")
        print(f"Distance AB: {distance_AB}")
        print(f"Distance BC: {distance_BC}")
        print(f"Distance CA: {distance_CA}")

        k = k+str(math.floor(angle_A)) + str(math.floor(angle_B)) + str(math.floor(angle_C)) + str(
            math.floor(distance_AB)) + str(math.floor(distance_BC)) + str(math.floor(distance_CA))

    print(f"Concatenated angles (k): {k}")

    hash_object = hashlib.sha256(k.encode())
    hash_value = hash_object.hexdigest()

    #############################################

    file_name = fs.location + '/' + filepath  # Get the full path
    encrypted_file = file_name + '.aes'
    orgfp=file_name


    import pyAesCrypt


    pyAesCrypt.encryptFile(file_name, encrypted_file, str(hash_value))

    aobj=Upload()
    aobj.date=datetime.now().date()
    aobj.file=encrypted_file
    aobj.title=orgfp
    aobj.USER=User.objects.get(LOGIN_id=request.session['lid'])
    aobj.save()

    os.remove('C:\\Users\\noufa\\PycharmProjects\\FBESFDSWRBS\\media\\'+date1)

    # decrypted_file = file_name + '.decrypted'
    # pyAesCrypt.decryptFile(encrypted_file, decrypted_file, str(password))
    return HttpResponse(
        '''<script>alert('Upload and Encryption Successful');window.location="/FST/user_home/"</script>''')


def download_files(request,id):

    request.session["fid"]=id
    return render(request,"user/downloadbyfing.html")


def downloadpost(request):


    fss=request.FILES["img"]

    from datetime import  datetime
    fname= datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"


    fs = FileSystemStorage()

    filepath1 = fs.save(fname, fss)
    path2 = fs.url(filepath1)

    #############################################
    import cv2
    import fingerprint_feature_extractor
    import math
    import numpy as np
    from scipy.spatial import Delaunay
    import hashlib
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import padding
    import os

    img = cv2.imread('C:\\Users\\noufa\\PycharmProjects\\FBESFDSWRBS\\media\\' + fname, 0)

    FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(
        img, spuriousMinutiaeThresh=10, invertImage=False, showResult=True, saveResult=True
    )

    print("Bifurcations:", FeaturesBifurcations)
    print("Terminations:", FeaturesTerminations)

    pp = []

    def distance(p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    def find_angle(A, B, C):
        a = distance(B, C)
        b = distance(A, C)
        c = distance(A, B)

        angle_A = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
        angle_A_degrees = math.degrees(angle_A)
        return angle_A_degrees

    for idx, curr_minutiae in enumerate(FeaturesTerminations):
        pp.append([curr_minutiae.locX, curr_minutiae.locY])

    for idx, curr_minutiae in enumerate(FeaturesBifurcations):
        pp.append([curr_minutiae.locX, curr_minutiae.locY])

    points = np.array(pp)

    tri = Delaunay(points)

    print("Delaunay Triangulation Points:")
    for i in tri.points:
        print(i)

    angle_sum_list = []

    secret_key = os.urandom(32)
    iv = os.urandom(16)

    def aes_encrypt(data, key, iv):

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data.encode()) + padder.finalize()

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        return encrypted_data
    k=""

    for i in tri.simplices:
        A = tri.points[i[0]]
        B = tri.points[i[1]]
        C = tri.points[i[2]]

        angle_A = find_angle(A, B, C)
        angle_B = find_angle(B, C, A)
        angle_C = find_angle(C, A, B)

        print(f"Angles of triangle {i}:")
        print(f"Angle at A: {math.floor(angle_A)} degrees")
        print(f"Angle at B: {math.floor(angle_B)} degrees")
        print(f"Angle at C: {math.floor(angle_C)} degrees")

        distance_AB = distance(A, B)
        distance_BC = distance(B, C)
        distance_CA = distance(C, A)

        print(f"Distances between points A, B, C:")
        print(f"Distance AB: {distance_AB}")
        print(f"Distance BC: {distance_BC}")
        print(f"Distance CA: {distance_CA}")

        k = k+str(math.floor(angle_A)) + str(math.floor(angle_B)) + str(math.floor(angle_C)) + str(
            math.floor(distance_AB)) + str(math.floor(distance_BC)) + str(math.floor(distance_CA))

    print(f"Concatenated angles (k): {k}")



    hash_object = hashlib.sha256(k.encode())
    hash_value = hash_object.hexdigest()




    f=Upload.objects.get(id=request.session["fid"])

    try:

        import pyAesCrypt

        mm=f.file.split(".")
        ext= mm[len(mm)-2]
        from datetime import  datetime
        fname3= datetime.now().strftime("%Y%m%d%H%M%S"+"dwnl"+ "."+ext)

        pyAesCrypt.decryptFile(f.file, "C:\\Users\\noufa\\PycharmProjects\\FBESFDSWRBS\\media\\"+fname3, str(hash_value))

        return  HttpResponse("<a href='/media/"+fname3+"'>Download</a>")
    except:
        return HttpResponse("<script>alert('Finger not matched');window.location='/FST/download/#ar'</script>")



def viewprof(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    vobj=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'User/view profile.html',{"data":vobj})


def viewreply(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    data=Complaint.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,'User/viewreply.html',{'data':data})

def viewreply_post(request):
    if request.session['lid'] == '':
        return redirect('/FST/login/')

    fromrep=request.POST['textfield']
    torep=request.POST['textfield2']
    return




def downloads3(request,fid):

    import  os


    Data=Upload.objects.get(id=fid)
    fname= Data.file.split('/')[1]


    import boto3
    # Creating an S3 access object
    obj = boto3.client("s3")

    # obj.head_object(Bucket="dsvarfst", Key=fname)

    # Downloading a csv file
    # from S3 bucket to local folder


    print(fname,"=====================================")


    obj.download_file(
        Filename="C:\\Users\\noufa\\PycharmProjects\\FBESFDSWRBS\\media\\s3\\"+fname.replace(".aes",""),
        Bucket="dsvarfst",
        Key=fname.replace(".aes","")
    )

    return  HttpResponse(
        "<center><a href='/media/s3/"+fname.replace(".aes","")+"' download>Download</a><center>"
    )








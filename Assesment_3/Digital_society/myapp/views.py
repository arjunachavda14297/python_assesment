from django.shortcuts import render,redirect
from .models import Contact,User,Event,Notice,Special_Team,Society_Member,Visitors
from django.conf import settings

# only special team add House Owner and Watchman 
# Special team added only by Administration


# Create your views here.

def index(request):
    special_team=Special_Team.objects.all()
    notices=Notice.objects.all().order_by('-date')
    events=Event.objects.all().order_by('-date')

    members=Society_Member.objects.all()

    return render(request,'index.html',{'notices':notices,'events':events,'special_team':special_team,'members':members})

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def notice(request):
    return render(request,'notice.html')

def login(request):
    if request.method=="POST":
        user=User()
        user.email=request.POST['email']
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.password==request.POST['password']:
                request.session['email']=user.email
                request.session['fname']=user.fname
                msg="successfully"
                return render(request,'login.html',{'msg':msg})
            else:
                msgl="Incorrect Password"
                return render(request,'login.html',{'msgl':msgl,'user':user})
        except:
            society_member=Society_Member()
            society_member.email=request.POST['email']
            try:
                society_member=Society_Member.objects.get(email=request.POST['email'])
                if society_member.password==request.POST['password']:
                    request.session['semail']=society_member.email
                    request.session['fname']=society_member.fname
                    msg="successfully"
                    return render(request,'login.html',{'msg':msg,'society_member':society_member})
                else:
                    msgl="Incorrect Password"
                    return render(request,'login.html',{'msgl':msgl,'society_member':society_member}) 
            except:
                steam=Special_Team()
                steam.email=request.POST['email']
                try:
                    steam=Special_Team.objects.get(email=request.POST['email'])
                    if steam.password==request.POST['password']:
                        request.session['stemail']=steam.email
                        request.session['fname']=steam.fname
                        msg="successfully"
                        return render(request,'login.html',{'msg':msg})
                    else:
                        msgl="Incorrect Password"
                        return render(request,'login.html',{'msgl':msgl,'steam':steam})
                except:
                    msgl="Invalid Email"
                    return render(request,'login.html',{'msgl':msgl})
    else:
        return render(request,'login.html')

def forgot(request):
    return render(request,'forgot.html')

def contact(request):
    if request.method=="POST":
        Contact.objects.create(
            name=request.POST['fname'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        msg="Successfully Submited"
        return render(request,'contact.html',{'msg':msg})
    else:
        return render(request,'contact.html')

def signup(request):
    if request.method=="POST":    
        try:
            User.objects.get(email=request.POST['email'])
            msg="Email Already Registered"
            return render(request,'signup.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    mobile=request.POST['mobile'],
                    email=request.POST['email'],
                    profile_pic=request.FILES['profile'],
                    password=request.POST['password'],
                    usertype=request.POST['usertype']
                )
                msg="Successfully Registered"
                return render(request,'signup.html',{'msg':msg})
            else:
                msg="Password & Confirm Password Does Not Matched"
                return render(request,'signup.html',{'msg':msg})
    else:
        return render(request,'signup.html')

def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        return render(request,'login.html')
    except:
        try:
            del request.session['semail']
            del request.session['fname']
            return render(request,'login.html')
        except:
            try:
                del request.session['stemail']
                del request.session['fname']
                return render(request,'login.html')
            except:
                return render(request,'index.html')

def change_password(request):
    if request.method=="POST":
        user=User.objects.get(email=request.session['email'])
        if user.password==request.POST['old_password']:
            if request.POST['new_password']==request.POST['cnew_password']:
                user.password=request.POST['new_password']
                user.save()
                return redirect('logout')
            else:
                msg="New Password And Confirm New Password Does Not Matched"
                return render(request,'change_password.html',{'msg':msg})
        else:
            msg="Incorrect Old Password"
            return render(request,'change_password.html',{'msg':msg})
    else:
        return render(request,'change_password.html')

def change_profile(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.mobile=request.POST['mobile']
        try:
            user.profile_pic=request.FILES['profile_pic']
        except:
            pass
        user.save()
        request.session['fname']=user.fname
        request.session['profile_pic']=user.profile_pic.url
        msg="Profile Updated Successfully"
        return render(request,'change_profile.html',{'user':user,'msg':msg})
    else:
        return render(request,'change_profile.html',{"user":user})

def add_notice(request):
    if request.method=="POST":
        Notice.objects.create(
            notice=request.POST['notice']
        )
        msg="Notice Add Successfully"
        return render(request,'add_notice.html',{'msg':msg})
    else:
        return render(request,'add_notice.html')

def add_event(request):
    user=Society_Member.objects.get(email=request.session['semail'])
    if request.method=="POST":
        Event.objects.create(
            user=user,
            event_name=request.POST['event'],
            location=request.POST['location'],
            date=request.POST['datetime']
        )
        msg="Event Add Successfully"
        return render(request,'add_event.html',{'msg':msg})
    else:
        return render(request,'add_event.html')

def notice(request):
    notices=Notice.objects.all().order_by('-date')
    return render(request,'notice.html',{'notices':notices})

def event(request):
    events=Event.objects.all().order_by('-date')
    return render(request,'event.html',{'events':events})

def add_member(request):
    if request.method=="POST":
        if request.POST['password']==request.POST['cpassword']:
            Society_Member.objects.create(
                member_type=request.POST['member_type'],
                fname=request.POST['fname'],
                lname=request.POST['lname'],
                mobile=request.POST['mobile'],
                email=request.POST['email'],
                block=request.POST['block'],
                house=request.POST['house'],
                profile_pic=request.FILES['profile'],
                password=request.POST['password']
            )
            msg="Member Added Successfully"
            return render(request,'add_member.html',{'msg':msg})
        else:
            msg1="Password and Confirm Password Does Not Matched."
            return render(request,'add_member.html',{'msg1':msg1})
    else:
        return render(request,'add_member.html')

def member_change_password(request):
    if request.method=="POST":
        user=Society_Member.objects.get(email=request.session['semail'])
        if user.password==request.POST['old_password']:
            if request.POST['new_password']==request.POST['cnew_password']:
                user.password=request.POST['new_password']
                user.save()
                return redirect('logout')
            else:
                msg="New Password And Confirm New Password Does Not Matched"
                return render(request,'member_change_password.html',{'msg':msg})
        else:
            msg="Incorrect Old Password"
            return render(request,'member_change_password.html',{'msg':msg})
    else:
        return render(request,'member_change_password.html')

def member_change_profile(request):
    user=Society_Member.objects.get(email=request.session['semail'])
    if request.method=="POST":
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.mobile=request.POST['mobile']
        try:
            user.profile_pic=request.FILES['profile_pic']
        except:
            pass
        user.save()
        request.session['fname']=user.fname
        request.session['profile_pic']=user.profile_pic.url
        msg="Profile Updated Successfully"
        return render(request,'member_change_profile.html',{'user':user,'msg':msg})
    else:
        return render(request,'member_change_profile.html',{"user":user})

def special_member(request):
    special_team=Special_Team.objects.all()
    return render(request,'special_member.html',{'special_team':special_team})

def member(request,member_type):
    mt=member_type
    if mt=='watchman':
        member=Society_Member.objects.filter(member_type='watchman')
        return render(request,'member.html',{'member':member,'mt':mt})
    
    elif mt=='block1':
        member=Society_Member.objects.filter(block='Block 1')
        return render(request,'member.html',{'member':member,'mt':mt})
    
    elif mt=='block2':
        member=Society_Member.objects.filter(block='Block 2')
        return render(request,'member.html',{'member':member,'mt':mt})

    elif mt=='block3':
        member=Society_Member.objects.filter(block='Block 3')
        return render(request,'member.html',{'member':member,'mt':mt})

    elif mt=='block4':
        member=Society_Member.objects.filter(block='Block 4')
        return render(request,'member.html',{'member':member,'mt':mt})

    elif mt=='block5':
        member=Society_Member.objects.filter(block='Block 5')
        return render(request,'member.html',{'member':member,'mt':mt})
    
    elif mt=='all':
        member=Society_Member.objects.all()
        return render(request,'member.html',{'member':member,'mt':mt})

    else:
        member=Society_Member.objects.all()
        return render(request,'member.html',{'member':member})

def add_visitor(request):
    if request.method=="POST":
        try:
            member=Society_Member.objects.get(mobile=request.POST['mmobile'])
            Visitors.objects.create(
                member=member,
                fname=request.POST['fname'],
                lname=request.POST['lname'],
                person=request.POST['person'],
                mobile=request.POST['mobile'],
                vehicle_no=request.POST['vehicle']
            )
            msg="Member Added Successfully"
            return render(request,'visitors.html',{'msg':msg})
        except:
            msg1="No House Owner Finds."
            return render(request,'visitors.html',{'msg1':msg1})
    else:
        return render(request,'visitors.html')
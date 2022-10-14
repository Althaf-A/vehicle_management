from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import redirect, render

# Create your views here. 

def login(request):
    return render(request, 'login.html')

def register(request):
    designations=designation.objects.all()

    return render(request, 'register.html',{'designations':designations})

def Account_login(request):
    Admin = designation.objects.get(designation="admin")
    User = designation.objects.get(designation="user")
    if request.method == 'POST':
        username  = request.POST['uname']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            request.session['SAdm_id'] = user.id
            return redirect( 'Super_Admin_Dash')

        elif useroradminregistration.objects.filter(username=request.POST['uname'], password=request.POST['password'],designation=Admin.id):
                
                member=useroradminregistration.objects.get(username=request.POST['uname'], password=request.POST['password'])
                request.session['Adid'] = member.designation_id
                request.session['usernamets1'] = member.username
                request.session['Adm_id'] = member.id 
                mem=useroradminregistration.objects.filter(id= member.id)
                
                return redirect( 'Admin_Dash')

        elif useroradminregistration.objects.filter(username=request.POST['uname'], password=request.POST['password'],designation=User.id):
                
                member=useroradminregistration.objects.get(username=request.POST['uname'], password=request.POST['password'])
                request.session['usid'] = member.designation_id
                request.session['usernamets1'] = member.username
                request.session['Usr_id'] = member.id 
                mem1=useroradminregistration.objects.filter(id= member.id)
                
                return redirect( 'User_Dashboard')
        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'login.html', context)
    return render(request,'login.html')


def Account_Registrtion(request):
    if request.method == 'POST':
        designations=designation.objects.all()
        acc = useroradminregistration()
        acc.firstname = request.POST['fname']
        acc.username = request.POST['uname']
        desi_id = request.POST['desig']
        acc.designation_id = desi_id
        acc.password = request.POST['password']
        acc.save()
        return redirect('login')
    else:
      messages.info(request, 'Password doesnt match. Register Again')
      return redirect('Account_Registrtion')

############### user start here #############

def User_Dashboard(request):
    if 'Usr_id' in request.session:
        if request.session.has_key('Usr_id'):
            Usr_id = request.session['Usr_id']
            mem4 = useroradminregistration.objects.filter(id=Usr_id)
    vehicle=vehicle_registration.objects.all()
    userpro=useroradminregistration.objects.get(id=Usr_id)
    return render(request, 'User_Dashboard.html', {'vehicle':vehicle,'userpro':userpro})

def User_logout(request):
    request.session.flush()
    return redirect("/")

############ admin start here ##############

def Admin_Dash(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
            mem4 = useroradminregistration.objects.filter(id=Adm_id)
    vehicle=vehicle_registration.objects.all()
    adpro=useroradminregistration.objects.get(id=Adm_id)
    return render(request, 'Admin_Dash.html', {'vehicle':vehicle,'adpro':adpro})

def Admin_edit(request, id):
    vehicle=vehicle_registration.objects.get(id=id)
    return render(request, 'Admin_edit.html', {'vehicle':vehicle})


def Admin_Update(request, id):
    try:
        if request.method=="POST":
            vehicle_update_Admin=vehicle_registration.objects.get(id=id)
            vehicle_update_Admin.vehiclenumber=request.POST.get('vnumber')
            vehicle_update_Admin.vehicletype=request.POST.get('vtype')
            vehicle_update_Admin.vehiclemodal=request.POST.get('vmodal')
            vehicle_update_Admin.vehicledescription=request.POST.get('vdescription')
            vehicle_update_Admin.save()
            return redirect('Admin_Dash')
    except:
        return redirect('Admin_edit')

def Admin_logout(request):
    request.session.flush()
    return redirect("/")

################ super admin start hear ##############

def Super_Admin_Dash(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
    vehicle=vehicle_registration.objects.filter(user_id=SAdm_id)
    adpro=User.objects.get(id=SAdm_id)
    return render(request, 'Super_Admin_Dash.html', {'vehicle':vehicle,'adpro':adpro})
    
def Super_Admin_Vehicle_Add(request):
    return render(request,'Super_Admin_Vehicle_Add.html')

def Super_Admin_Vehicle_Registration(request):
      if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.method=="POST":
            vregistration=vehicle_registration()
            vregistration.vehiclenumber = request.POST['vnumber']
            vregistration.vehicletype = request.POST['vtype']
            vregistration.vehiclemodal = request.POST['vmodal']
            vregistration.vehicledescription = request.POST['vdescription']
            vregistration.user_id=SAdm_id
            vregistration.save()
            return redirect('Super_Admin_Dash')
        else:
            return redirect('Super_Admin_Vehicle_Add')
def Super_Admin_edit(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
    
    vehicle=vehicle_registration.objects.filter(user_id=SAdm_id)
    vehicle=vehicle_registration.objects.get(id=id)
    return render(request, 'Super_Admin_edit.html', {'vehicle':vehicle})

def Super_Admin_Update(request, id):
    try:
        if request.method=="POST":
            vehicle_update_Super_Admin=vehicle_registration.objects.get(id=id)
            vehicle_update_Super_Admin.vehiclenumber=request.POST.get('vnumber')
            vehicle_update_Super_Admin.vehicletype=request.POST.get('vtype')
            vehicle_update_Super_Admin.vehiclemodal=request.POST.get('vmodal')
            vehicle_update_Super_Admin.vehicledescription=request.POST.get('vdescription')
            vehicle_update_Super_Admin.save()
            return redirect('Super_Admin_Dash')
    except:
        return redirect('Super_Admin_edit')

def Super_Admin_Delete_Vehicle(request,  id):
    vehicle=vehicle_registration.objects.get(id = id)
    vehicle.delete()
    return redirect('Super_Admin_Dash')

def logout(request):
    auth.logout(request)
    return redirect('login')





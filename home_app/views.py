from django.shortcuts import render, HttpResponse , redirect
from home_app.models import Registration_Data ,Contacts
from django.contrib.auth.models import User  , auth
from django.contrib import messages
from django.contrib.auth import authenticate ,login, alogin , logout

from recommendation import models

from home_app import views






def index(request):
    #return HttpResponse("this is about page ")
    return render(request,'index.html')


#about us page
def about(request):
    return render(request,'about.html')

#contact us page
def contact(request):
    #return HttpResponse("this is contact page ")
    return render(request,'contact.html')

#login us page
def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username=username, password=password)

        if user is not None:
            alogin(request, user)

            messages.success(request,"User is Login Sussessfully")
            return redirect('/') # is may get error
        else:
            messages.error(request," Invalid cradintanl ")
            return redirect('/')

    return render(request,'login.html')


#Registration us page
def Registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST['email']
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        password = request.POST['password']
        answer = request.POST.get('answer')
        security = request.POST.get('security')


        registration = Registration_Data(name=name , email=email,password=password,mobile=mobile,address=address ,security=security,answer=answer)
        registration.save()

        # create users
        myuser = User.objects.create_user(username=email, email=email, password=password)
        myuser.first_name = name
        myuser.last_name = name
        myuser.save()
        messages.success(request, "user is save")
        return render(request,'login.html')

    return render(request, 'Registration.html')




#login

def handlesignin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        print(username)
        print(password)


        user = authenticate(username=username, password=password)

    if user is not None:
        auth.login(request,user)
        print("in login funciton 646544444444444444444444444444444444444444444444444444444444444444444444")

        messages.success(request,"User is Login Sussessfully")
        return redirect('/') # is may get error
    else:
        messages.error(request," Invalid cradintanl ")
        return redirect('/login')

    return render(request,'index.html')



#logout
def handlelogout(request):
    print("in logout funciton 646544444444444444444444444444444444444444444444444444444444444444444444")
    logout(request)

    return render(request,'index.html')





#handling the constact us page
def handlecontact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        message = request.POST.get('message')



        print(name)
        print(mobile)
        print(email)
        print(message)


        contact = Contacts(name=name,mobile=mobile,email=email,message=message)
        contact.save()


    return render(request,'index.html')







#this is filtering the catagoris wise recommendation
def filter(request):
    return render(request,'filter.html')






# display menu categories wise

def Veg_categories(request):
    vegetarian_products = models.Menu.objects.filter(category='Veg')

    return render(request, 'categories.html', {'vegetarian_products': vegetarian_products})


    print(menu)


    return render(request,'categories.html')







# display menu categories wise

def Non_Veg_categories(request):
    vegetarian_products = models.Menu.objects.filter(category='Non-Veg')

    return render(request, 'categories.html', {'vegetarian_products': vegetarian_products})


    print(menu)


    return render(request,'categories.html')







# display menu categories wise

def seafood_categories(request):
    vegetarian_products = models.Menu.objects.filter(category='Seafood')

    return render(request, 'categories.html', {'vegetarian_products': vegetarian_products})


    print(menu)


    return render(request,'categories.html')







# display menu categories wise

def beverage_categories(request):
    vegetarian_products = models.Menu.objects.filter(category='Beverage')

    return render(request, 'categories.html', {'vegetarian_products': vegetarian_products})


    print(menu)


    return render(request,'categories.html')




# display menu categories wise

def dessert_categories(request):
    vegetarian_products = models.Menu.objects.filter(category='Dessert')

    return render(request, 'categories.html', {'vegetarian_products': vegetarian_products})


    print(menu)


    return render(request,'categories.html')


# display menu categories wise

def vegan_categories(request):
    vegetarian_products = models.Menu.objects.filter(category='Vegan')

    return render(request, 'categories.html', {'vegetarian_products': vegetarian_products})


    print(menu)


    return render(request,'categories.html')




def breakfast_categories(request):
    vegetarian_products = models.Menu.objects.filter(category='Breakfast')

    return render(request, 'categories.html', {'vegetarian_products': vegetarian_products})


    print(menu)


    return render(request,'categories.html')







#static
def birini(request):
    return render(request,'birini.html')


#static
def birini(request):
    return render(request,'birini.html')


#static
def cake(request):
    return render(request,'cake.html')


#static
def paneer(request):
    return render(request,'paneer.html')


#static
def virgin(request):
    return render(request,'virgin.html')


#static
def haka(request):
    return render(request,'haka.html')


#static
def pasta(request):
    return render(request,'pasta.html')







from django.shortcuts import render
from django.http import HttpResponse
from home_app.models import Order



def handle_order(request):
    if request.method == 'POST':
        # Retrieve form data
        card_number = request.POST.get('card_number')
        expiration_date = request.POST.get('expiration_date')
        cvv_code = request.POST.get('cvv_code')
        card_holder_name = request.POST.get('card_holder_name')
        amount = request.POST.get('amount')


        order = Order(card_number=card_number, expiration_date=expiration_date, cvv_code=cvv_code, card_holder_name=card_holder_name,amount=amount)

        order.save()

        # registration = Registration_Data(name=name, email=email, password=password, mobile=mobile, address=address,
        #                                  security=security, answer=answer)
        # registration.save()

        return render(request,'ThankYou.html')  # You can customize the response as needed

    return HttpResponse('Invalid request method')  # Handle other HTTP methods if needed















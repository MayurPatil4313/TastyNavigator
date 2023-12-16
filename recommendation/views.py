from django.shortcuts import render
from django.shortcuts import render, HttpResponse , redirect
from .models import Menu
from recommendation.models import Contacts
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Menu, CartItem
from django.contrib.auth.decorators import login_required


from django.http import JsonResponse


from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import CartItem
from django.contrib.auth.decorators import login_required



import mysql.connector
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from django.shortcuts import render
import mysql.connector
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel




import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import mysql.connector


import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import mysql.connector

from django.contrib.auth import authenticate ,login, alogin , logout





# Create your views here.
def recommendation(request):
    menus = Menu.objects.all()

    context = {
        'menus' : menus
    }

    return render(request,'recommendation.html',context)




#handling the constact us page
def handlecontact(request):
    if request == "POST":
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contacts(name=name,mobile=mobile,email=email,message=message)
        contact.save()






















#this is filtering the catagoris wise recommendation
def filter(request):

    if request.method == "POST":
        mincal = float(request.POST.get('mincal'))
        maxcal = float(request.POST.get('maxcal'))
        minprice = float(request.POST.get('minprice'))
        maxprice = float(request.POST.get('maxprice'))
        userrating = float(request.POST.get('userrating'))




        print(mincal)
        print(maxcal)
        print(minprice)
        print(maxprice)
        print(userrating)




        # Connect to the database and fetch data
        # Make sure to replace the connection parameters with your actual database credentials
        db_config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'database': 'tastynavigator',
            #'port' : 3306,

        }

        menu_dish = Menu.objects.all()


        df = pd.DataFrame(list(menu_dish.values()))
        # Create a connection string
        # engine = create_engine(
        #     "mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

        '''engine = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )'''

        min_calories = float(mincal)
        max_calories = float(maxcal)
        min_price = float(minprice)
        max_price = float(maxprice)
        min_user_rating = float(userrating)


        # Assuming you have a table named 'newdata'
        # query = "SELECT dish_name, calories, price, user_rating FROM menu"
        # df = pd.read_sql(query, con=engine)

        # Get user inputs for calorie and price ranges




        print(type(mincal))
        print(type(maxcal))
        print(type(minprice))
        print(type(maxprice))
        print(type(userrating))



        # Filter the dataframe based on user inputs
        filtered_df = df[
            (df['calories'] >= min_calories) & (df['calories'] <= max_calories) &
            (df['price'] >= min_price) & (df['price'] <= max_price) &
            (df['user_rating'] >= min_user_rating)
            ]

        # Check if there are dishes in the filtered criteria
        if not filtered_df.empty:

            # Data preprocessing for the filtered data
            # X_filtered = filtered_df[['calories', 'price', 'user_rating']]
            # scaler = StandardScaler()
            # X_filtered_scaled = scaler.fit_transform(X_filtered)

            features = ['calories', 'price', 'user_rating']
            X_filtered = filtered_df[features]
            scaler = StandardScaler()
            X_filtered_scaled = scaler.fit_transform(X_filtered)





            # Model training on the filtered data
            model = NearestNeighbors(n_neighbors=5,
                                     algorithm='ball_tree')  # Use neighbors for a more accurate distance measure
            model.fit(X_filtered_scaled)

            # Set a fixed radius value (replace with different values)
            radius = 18.0  # You can experiment with different radius values

            # Use the fixed radius value
            user_inputs_scaled = scaler.transform([[max_calories, max_price, min_user_rating]])

            # Find similar dishes within a distance threshold
            indices = model.radius_neighbors(user_inputs_scaled, radius=radius, return_distance=False)

            # Display recommendations

            # ...

            if len(indices[0]) > 0:
                menu_list = []
                print("Recommended dishes:")

                for idx in indices[0]:
                    recommended_dish = filtered_df.iloc[idx]

                    # Calculate and display the score of the individual recommendation
                    score = 1 / (1 + model.kneighbors([X_filtered_scaled[idx]])[0].mean())
                    print("Score: {score:.2f}")

                    menu_list.append({

                        'id': recommended_dish['id'],
                        'dish_name': recommended_dish['dish_name'],
                        'calories': recommended_dish['calories'],
                        'price': recommended_dish['price'],
                        'user_rating': recommended_dish['user_rating'],
                        'description': recommended_dish['description'],
                        'ingredients': recommended_dish['ingredients'],
                        'category': recommended_dish['category'],
                        'cuisine': recommended_dish['cuisine'],
                        'score': score
                    })

                    print("-------------------")

                # Calculate accuracy of recommendations
                accuracy = len(indices[0]) / len(filtered_df) * 100
                context = {'menu_list': menu_list}

                return render(request, 'recommendation.html', context)

                print("Accuracy of recommendations: {accuracy:.2f}%")
            else:
                print("No dishes found within the specified criteria.")
                return render(request, '404.html')



    return render(request,'filter.html')













def Ingredients(request):
    context = {}  # Initialize context

    if request.method == "POST":
        ingredients = request.POST.get('ingredients')

        # Connect to the MySQL database
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tastynavigator"
        )

        # Fetch data from the menu table
        newdata_query = "SELECT * FROM menu"
        newdata_df = pd.read_sql_query(newdata_query, db_connection)

        # Pre-process menu table
        newdata_df['ingredients'] = newdata_df['ingredients'].str.lower()
        newdata_df['ingredients'] = newdata_df['ingredients'].str.replace(',', ' ')

        # Create a TF-IDF vectorizer
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf_vectorizer.fit_transform(newdata_df['ingredients'])

        # Function to get dish recommendations based on user-entered ingredients
        def get_recommendations(user_inputs, num_recommendations=20):
            user_inputs = user_inputs.lower().split(',')
            user_tfidf = tfidf_vectorizer.transform(user_inputs)
            cosine_sim_user = linear_kernel(user_tfidf, tfidf_matrix).flatten()

            # Get indices of dishes sorted by similarity
            sim_indices = cosine_sim_user.argsort()[::-1]

            # Filter recommendations to include only dishes with all user-input ingredients
            filtered_recommendations = []
            for i in sim_indices:
                if i < len(newdata_df):
                    if all(ingredient in newdata_df['ingredients'].iloc[i].split() for ingredient in user_inputs):
                        dish_info = newdata_df.iloc[i]
                        score = cosine_sim_user[i]
                        filtered_recommendations.append((dish_info, score))

            # Check if there are recommendations
            if not filtered_recommendations:
                print("No recommendations found.")
                return []

            # Display all information of recommended dishes
            print("\nDish Recommendations:")
            menu_list = []
            for recommendation, score in filtered_recommendations[:num_recommendations]:
                menu_list.append({
                    'id': recommendation['id'],
                    'dish_name': recommendation['dish_name'],
                    'calories': recommendation['calories'],
                    'price': recommendation['price'],
                    'user_rating': recommendation['user_rating'],
                    'description': recommendation['description'],
                    'ingredients': recommendation['ingredients'],
                    'category': recommendation['category'],
                    'cuisine': recommendation['cuisine'],
                    'score': score
                })

            context['menu_list'] = menu_list
            print("this is redirect page")
            print(context)

            # Render the recommendation.html template with the context
            return render(request, 'recommendation.html', context)

        # Take user input for ingredients
        user_input_ingredients = ingredients

        # Get recommendations
        recommendations = get_recommendations(user_input_ingredients, num_recommendations=20)

        # Close the database connection
        db_connection.close()

        # Check if recommendations are found
        if recommendations:
            # Render the recommendation.html template with the context
            return render(request, 'recommendation.html', context)


        else:
            return render(request,'404.html')

    # Default rendering if no recommendation or if the request method is not POST
    return render(request, 'filter.html', context)






# add to cart functioality
@login_required
def add_to_cart(request, dish_id):
    dish = Menu.objects.get(pk=dish_id)

    #code for cart  the data in database

    # Create a CartItem instance with the dish details
    cart_item = CartItem(
        user=request.user,
        dish_id=dish_id,
        dish_name=dish.dish_name,
        description=dish.description,
        ingredients=dish.ingredients,
        price=dish.price,
        calories=dish.calories,
        cuisine=dish.cuisine,
        user_rating=dish.user_rating,
        category=dish.category,
    )

    # Save the cart item to the database
    cart_item.save()
    # end here



    return JsonResponse({'success': True})



from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import CartItem





@login_required
def remove_from_cart(request, dish_id):
    cart_item = get_object_or_404(CartItem, user=request.user, dish_id=dish_id)
    cart_item.delete()
    return JsonResponse({'success': True})







@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart_template.html', {'cart_items': cart_items})














#order page
from django.shortcuts import render
from .models import CartItem

def order(request):
    # Get the user's cart items
    cart_items = CartItem.objects.filter(user=request.user)

    description = CartItem.description
    # Calculate the total price
    #total_price = sum(cart_item.price for cart_item in cart_items)
    total_price = sum(cart_item.total_price() for cart_item in cart_items)

    # Pass the total_price to the template
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'description' : description,

    }

    return render(request, 'order.html', context)


# views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET

from .models import CartItem


@require_GET
def update_cart_quantity(request, dish_id, quantity):
    cart_item = get_object_or_404(CartItem, dish_id=dish_id, user=request.user)

    # Update the quantity in the CartItem model
    cart_item.quantity = quantity
    cart_item.save()

    return JsonResponse({'success': True})












# views.py
from django.http import JsonResponse
import logging


logger = logging.getLogger(__name__)

def update_cart_item_quantity(request, dish_id, new_quantity):
    try:
        logger.info("Updating quantity for dish   ",{dish_id},"to",{new_quantity})
        cart_item = CartItem.objects.get(dish_id=dish_id, user=request.user)
        cart_item.quantity = new_quantity
        cart_item.save()
        return JsonResponse({'success': True})
    except CartItem.DoesNotExist:
        logger.error("Item not found in the cart for dish ",{dish_id})
        return JsonResponse({'success': False, 'error': 'Item not found in the cart'})

















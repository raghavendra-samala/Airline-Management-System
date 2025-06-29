# Airline Management System

![image](https://user-images.githubusercontent.com/55591669/114278082-a10adb00-9a4b-11eb-9d72-fd427938c7b5.png)

This is the Airline Management System for Perl Air that we have developed as a part of Software Engineering Laboratory Course in Spring Semester of 2020-21 at CSE Department, IIT Kharagpur. 

This Website is built using the Django Framework in Python along with Bootstrap Framework for the FrontEnd. Crafted with simple User Interface and simple functionalities serving both the Airline Customers and Airline Managers alike.

This project is hosted on http://perlair.pythonanywhere.com/


# Main Features

* Securely creates and logins the users into the Management System
* Allows customers to add money into the exclusive Perl Air Wallet
* Allows users to book flights and personally select the seat numbers in their flights
* Allows users to delete or modify their bookings at an additional cost
* Allows users to view all their upcoming tickets
* Allows the Managers of the Airline to view the occupancy rates of different flights
* Allows the Managers to view the net profits earned by Perl Air in a specified time window
* Allows the Managers to modify the pricing and costs for various flight types in their fleet
* Allows the Managers to modify the flight schedules to best suit and maximize the Airline's profits

# Usage

You need to install the latest version of the Django framework along with its extensions like runscript and crispy-forms. You need not install Bootstrap as it would be delivered using CDN if you are connected to the Internet. You would need recent version of any well known Web Browser like Google Chrome, Microsoft Edge, Firefox, etc., to run the Website. 

Django can be installed by running
    
    pip install Django

Extensions can be installed by running

    pip install django-extensions

Install crispy-forms by running

    pip install django-crispy-forms

##

After downloading the AMS-package, you need open the CMD in the directory of airline-management-system/ams/ and run the command,

    python manage.py makemigrations

If the command raises an error, try commenting the lines...

Once the migrations are made, run the command,

    python manage.py migrate

Now, it is recommended that you create a superuser to avail the facilities of Django-admin, available at localhost:8000/admin
To do that, run,

    python manage.py createsuperuser
    
Now you can run the script that I have written which instantiates objects of classes Trips and Flights so that you have a basic Flight Schedule ready at hands to work on.
To do that, run

    python manage.py runscript scripts.ReinitialiseDatabase

Now you are ready to run the local server and use the Airline Management System Website. To do that, run,

    python manage.py runserver

The server starts at the address http://127.0.0.1:8000/ or localhost:8000
Use your web browser to run the website.


# Credits

* Framework : Django and Bootstrap
* Images : Unsplash (http://unsplash.com - CC0 licensed)
* Code Written by Matta Varun, B Sai Vamshi, V Sai Gokul - CSE Sophomores at IIT Kharagpur

#Study portal:

Study portal is a simple open-source website platform built on the Django Web Framework, designed to provide services for student to track their assignments, to-dos, save notes and refer to contents from other platforms all in one place when studying.  

#Getting Started

#Prerequisites

•	python

•	Pip install django

#Installation

•	clone Repository & Install Packages
o	git clone https://github.com/isaiassiele/Study-Portal.git
•	create a virtual environment inside  and activate virtual environment,
o	For Mac/ Linux
o	python3 -m venv myenv
o	source env/bin/activate


o	for windows
o	virtualenv venv
o	.\venv\Scripts\activate
•	install project dependencies from requirements.txt
o	pip install –r requirements.txt
•	migrate and start server
o	python manage.py makemigrations
o	python manage.py migrate
o	python manage.py runserver

Demo
•	http://isaiasportal.pythonanywhere.com

# Detailed explanation:
The website has six main pages and those are:
•The to-do page: which helps to store data in database and can be retrieved from the to-do page and when the task is done the user can mark it as completed or delete it. The user can update the information of the task at any time.

•The homework page: helps in organizing homework and assignments, by creating new assignments updating deleting and, marking as completed too.

•The notes pages: this page provides the student to keep note when studying.

•Wiki search page: this helps the student to look up a quick summary of a topic without having to visit the Wikipedia page or going through everything, and of course if the student wants to dive in deeper they can click on the summary and get directed to the specific page on the actual website.

•YouTube page: has almost the same functionality as the Wikipedia page but uses YouTube API, this too helps the student to look up videos without the hustle of opening new tabs and having to lose focus, which is the main reason for this website, to provide a service in one place so a student hasn’t have to get distracted by trying to actually study and not have to keep up with looking up in different platforms.

•The books page: The Books API is a way to search and access that content, as well as to create and view personalization around that content. Using this API when the student search for books the page will provide with the most relevant books based on the search and list it including basic information, thumbnail and link to the Google books preview site.

•Dictionary page: this page has a search box where a student can lookup words. The word will be search by the help of an API from https://dictionaryapi.dev.

Some secondary pages included are:

•Homepage: A beautiful simple user interface design that shows all functionalities where the user can browse to the other pages through.

•Profile page: this page provide all the list of the user’s/ student’s homework and to-do status in tabular form.

The website includes seven primary pages and those are:

•The to-do page: This aids in database data storage and retrieval, and after a job is finished, the user can mark it as completed or delete it. Anytime the user wants, they may change the task's information and update as needed.

•The homework page assists in managing homework and assignments by adding new tasks, modifying existing ones, eliminating unfinished ones, and marking them as finished. The notes page allows the learner to keep notes while they are learning.

•The notes pages: this page provides the student to keep note when studying.

•Wiki search page: This enables the student to seek for a brief overview of a subject without having to travel to the Wikipedia page or read through everything; of course, if the student would like to go deeper, they may click on the summary and be redirected to the relevant page on the real website. The main goal of this website is to provide a service in one location so a student doesn't have to get sidetracked while trying to actually study and doesn't have to keep up with looking up in different platforms.

•The YouTube page: uses the YouTube API, which again aids the student in looking up videos without the hassle of opening new tabs and having to lose focus.

•Dictionary page: A search box is available on this page for students to look up terms. With the use of an API from https://dictionaryapi.dev, the term will be searched and fetched to the user.

•The books page: The Books API of Google offers a mechanism to search for and access that content, as well as to make and see personalization based on it. Using the books website when a student searches for books using this API, the website will present the most pertinent books based on the search and display them along with basic details, a thumbnail, and a link to the Google Books sample site.

Additional pages comprised include:

•Homepage: A lovely, straightforward user experience that displays all capabilities and allows users to go to other pages.

•The user's/student's homework and to-do list is listed in tabular form on the profile page.

Django Structure/ Code Structure

![Screenshot 2023-04-19 095148](https://user-images.githubusercontent.com/116893742/233022973-1fbdeb3e-0f02-4220-84c0-9f4e519de09a.jpg)


studentStudyPortal Directory

1. studentStudyPortal /init.py 

An empty file that tells Python that this directory should be considered a Python package.

2. studentStudyPortal /settings.py

 Settings/configuration for this Django project.we declare all Installed app ( 'social_django', 'dashboard','crispy_forms', 'crispy_bootstrap5',).
We added social_core.backends.facebook.FacebookOAuth2   in AUTHENTICATION_BACKENDS to used social media authentication.
This is where we define login, logout urls, statics files location and others.

3. studentStudyPortal /urls.py

The URL declarations for this Django project is provided here and if it is not provided  here it should be provided in the other apps( directories) but still the app should be referred here for instance :  
Path ('',include('dashboard.urls')),
This code dictated that if the url has ‘ ’ ;i.e, emplty url refer to the dashboard/urls.py module.Other built in or third party views can be mentioned here like:
 	path('oauth/', include('social_django.urls', namespace='social')), 
This is a third party plugin used for social media based authentication.

4. studentStudyPortal /asgi.py

An entry-point for ASGI-compatible web servers to serve your project, which we didn’t need to add since 
pythonanywhere.com works for both.

5. studentStudyPortal /wsgi.py

 An entry-point for WSGI-compatible web servers to serve your project, which we didn’t need to add since pythonanywhere.com works for both.


DASHBOARD folder consists of 

1. _init_.py

This file has the same functionality just as in the _init_.py file in the Django project structure. It remains empty and is present just to indicate that the specific app directory is a package.

2. dashbord/admin.py

As the name suggests, this file is used for registering the models into the Django administration.A custom admin class is created by inheriting django AdminSite class.The puupose of this custom admin is to limit staff using into only user management and not IT-admin related permissions. 

3. dashbord/apps.py

This file deals with the application configuration of the apps. The default configuration is sufficient enough in most of the cases and hence we won’t be doing anything here in the beginning.

4. dashbord/models.py

This file contains the models of our web applications (usually as classes).
Models are basically the blueprints of the database we are using and hence contain the information regarding attributes and the fields etc of the database.
In this we have created three classes that needed data storage and those are to-do, notes and homework pages. All the classes inherit django model class and have foreign key of user with a cascade attribute in order to delete notes, to-dos and homework associated with the user. The built __str__() function is overridden so that the admin can see names and not object reference. 

5. dashbord/views.py

This file is a crucial one, it contains all the Views(usually as classes). Views.py can be considered as a file that interacts with the client. Views are a user interface for what we see when we render a Django Web application.
The view contains all the function that are called from urls. For homework, to-do and notes a “@required” or LoginRequiredMixin mixins are used to avoid accessing those site with put logging in.
The youtube, wiki , books and dictionary functions use API to fetch data from the site and integrate to respective templates based on logics defined.
Home functions renders the home template and the other functions do the same thing based on logics and data provided, the update_todo_info , delete_todo update_todo , delete_note, delete_homework, update_homework_info, update_homework and todo receive primary key extra parameter to delete or update the required info.
The NotesDetailsView class inherits the django generic DetailView class to fetch the data of given model which is notes model.
Unlike the login and logout built-in functions of django we have used our own register method but making email as mandatory and to be unique in forms module.

6. dashbord/forms.py

The NotesForm, HomeworkForm, TodoForm classes inherit the ModelForm class inorder to create a form based on an existing models defined in model.py modules. We called class meta to alter the attributes of the model in which we choose fields we wanted to display. Since the ModelForm class has the save function we can save the form into database too.
DashboardForm class inherits the basic Form class, and gave it a one field only and we used this form for multiple functions such as the wiki, youtube, books and dictionary which require one field.
DateInput class was created to make sure the due date for assignments and homework get a clean date time format, this is done by importing the DateInput subclass of Form class and use it in widgets of HomeWorkForm meta classs.

7. dashbord/urls.py

Just like the project urls.py file, this file handles all the URLs of our web application. This file is just to link the Views in the app with the host web URL. The settings urls.py has the endpoints corresponding to the Views.
In this project, the urls for all pages are listed including the names, to easily call them from templates.As for deleting and updating urls we have included id in int format which will proved us with the primary key of whatever needed to be accessed for updating, retrieval or deletion. 

8. Template tags directory:

This sub directory consists of :
•	dashbord/templatetags/__init__() module indicate that the specific app directory is a package.
•	dashbord/templatetags/__custom_tags module which stores a function to register a custom template that checks if a user belongs to a certain group.

9. Templates directory:

This subdirectory contains all the html templates we use to render the views from views module. Special mention is for base.html which is like a blanket that cover the other templates to be included. This is achieve by used djangos {% extends %} and {% block content}} tags there are also other tags we used such as {% if %}{% endif %} {% for %}{% endfor %} and third party tags such as crispy_form_tags.


 

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oWm-EAsM)
# Museum-Project
**Suyoung Jang**  30179959  suyoung.jang@ucalgary.ca

**Miri Kim**      30172825  miri.kim@ucalgary.ca 

**Martin Liu**    30161516  martin.liu@ucalgary.ca

## Tasks
**EERD:** All worked together in-person. Updating and Explanation: Bella

**Relational Model:** All worked together in-person. Updating: Bella

**Database Implementation:** Partially altogether in-person. Remotely: Miri

**Querys:** Partially altogether in-person. Remotely: Miri

**Python Application:** Website: Martin

## Requirements
**Museum** in the **Code** portion of the repo is a virtual environment **specifically** created to be on **python 3.11.6**, therefore, it must be installed.

The following libraries must also be installed (Use '**python** -m pip install **"library name here"**' in Command Prompt):\
asgiref==3.7.2\
Django==4.2.7\
django-cleanup==8.0.0\
django-htmx==1.17.2\
mysqlclient==2.2.0\
Pillow==10.1.0\
sqlparse==0.4.4\
tzdata==2023.3\
whitenoise==6.6.0

##  How Use and Run Website 
1) In a directory of your choice, open command prompt and initialize a virtual environment (py -3.11 -m venv {Name})
2) Activate the virtual environment with (Scripts\activate.bat)
3) In another directory, clone the repo and open cmd prompt (These specific commands are only for cmd prompt and not powershell)
4) Change directories to the repo
5) In the repo cd to Code\ArtObject
6) Run the following command to install all dependencies: py -m pip install -r requirements.txt  
7) Now run: py manage.py runserver. (*Note:* If py is not recognized, use 'python manage.py runserver', instead)\
   The site will now be at the url http://127.0.0.1:8000/ 

## Features
Admin Page:
  Username: Admin
  Password: admin

  -Can view all tables and edit each one
  -Can add/remove new users

Home Page:
  -Can be used to query all attributes of art pieces (ArtObject). All primary keys, foreign keys, and YearMade must be matched exactly to appear in search results. Searching for the title/art description of an art piece can be non-exact and case does not matter. The rest of the attributes must be exact in wording but is case insensitive
  -In addition, the home search bar can also be used to query collections. For borrowed, type "$borrowed" for all borrowed collections items or specify with a space to search for a borred collection name (ex: "$borrowed Name"). This applies to permanent collections as well. Both are case insensitive but wording must be exact.

Exhibits Page:
  -Can be used to query all attributes of exhibits (Exhibition). Searching for ExhibitName does not have to be exact and is case insensitive. Start and End date must be exact and in the form YYYY-MM-DD.

Art Page:
  -Can be used to query all attributes of art pieces (ArtObject). All primary keys, foreign keys, and YearMade must be matched exactly to appear in search results. Searching for the title/art description of an art piece can be non-exact and case does not matter. The rest of the attributes must be exact in wording but is case insensitive
  -Is a categorized version of the home page where user can see the different types of art

Collections Page:
  -Same search criteria for collections as the home page
  -Categorized search for collections

## To Do list:
- modify this file to include your group members information and tasks assigned per each
- modify this file to include any notes on how to use and run the program
- include any features you have added beyond the minimum requirements in a features list

## Organization:
- code folder: contains your main python application code
- sql scripts folder: contains all sql scripts required (database creation and initialization, sql script with query tasks in the handout, etc...)
- database design folder: EERD and relational schema
- optional data folder: has data files that you can sue to load data to your application if you use this optional implementation requirement

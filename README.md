# ConnectionsOnline

## WOW Project Group 6 - Daniel Cho (https://github.com/Daniel165c), Donell Jenkins (https://github.com/Djenkins1221), Infinite Rahming (https://github.com/IDivinePrince)


We are creating a website that provides users access to various resources that will aide in their successful reentry into society Post-release.

## CHECK WHICH PYTHON COMMAND LINE: 
- To check what to use on your command lines for running .py files
- If you are using a mac, it should be `python3`. 
- For windows 11, it should be `py`. 
- If these don't work --run `python -v` to check if the version is 2.7 or 3.8. 
- If it's 2.7, then use python3 -v to see if there is a new version of python available, and if it returns a newer python version, then the command should be `python3`. 
- If it's 3.x.x, then the command is `python`

## Create your virtual environment using (venv):
-  Type `py -m venv venv` into the command line.
- Then type the command `venv\Scripts\activate`

## How to Install Project dependencies with pip:
- Next type `pip freeze > requirements.txt` into the command line in order to install requirements.
- Now type `pip install django`
- To name your project to your specifications in django, type `django-admin startproject **PROJECTNAME** `
- After you've named your project, CD into that project and type `python manage.py runserver`
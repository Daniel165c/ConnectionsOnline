# ConnectionsOnline

## WOW Project Group 6 - Daniel Cho (https://github.com/Daniel165c), Donell Jenkins (https://github.com/Djenkins1221), Infinite Rahming (https://github.com/IDivinePrince)


We are creating a website that provides users access to various resources that will aide in their successful reentry into society Post-release.

## CHECK WHICH PYTHON COMMAND LINE: 
- To check what to use on your command lines for running .py files
- If you are using a mac, it should be `python3`. 
- For windows 11, it should be `py`. 
- If these don't work--run `python --version` to check if the version is 2.7 or 3.8. 
- If it's 2.7, then use python3 -v to see if there is a new version of python available, and if it returns a newer python version, then the command should be `python3`. 
- If it's 3.x.x, then the command is `python`

## Initial setup

Do this when setting up the project for the first time.

```sh
# 1. Create your virtual environment.
# Windows
py -m venv venv
# Mac
python -m venv venv

# 2. Activate your virtual environment.
# Windows
venv\Scripts\activate
# Mac
source venv/bin/activate

# 3. Install project dependencies.
pip install -r requirements.txt

# 4. cd into the project directory.
cd ConnectionsOnline

# 5. Run the database migrations.
python manage.py migrate

# 6. Run the project.
python manage.py runserver
```

## Updating

Do this if project dependencies or database migrations have changed.

```sh
# Always activate your virtual environment before anything:
# Windows
venv\Scripts\activate
# Mac
source venv/bin/activate

# If project dependencies have changed, redo pip install:
pip install -r requirements.txt

# If database migrations have changed, rerun migrations:
cd ConnectionsOnline
python manage.py migrate
```

## Running

```sh
# Always activate your virtual environment before anything:
# Windows
venv\Scripts\activate
# Mac
source venv/bin/activate

cd ConnectionsOnline
python manage.py runserver
```

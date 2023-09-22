## KU Polls: Online Survey Questions 
[![Django CI](https://github.com/PhumrapeeC/ku-polls/actions/workflows/django.yml/badge.svg)](https://github.com/PhumrapeeC/ku-polls/actions/workflows/django.yml)

An application to conduct online polls and surveys based
on the [Django Tutorial project][django-tutorial], with
additional features.

This app was created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at Kasetsart University.

## Install and Run

1. Activate the virtual environment
   ```
   # On Linux or MacOS:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```
2. Start the Django development server
   ```
   python manage.py runserver
   ```
   If you get a message that the port is unavailable, then run the server on a different port (1024 thru 65535) such as:
   ```
   python3 manage.py runserver 12345
   ```
3. Access the app in a web browser at <http://localhost:8000>
4. Exit the virtual environment by closing the window or by typing:
   ```
   deactivate
   ```

## Project Documents

All project documents are in the [Project Wiki](../../wiki/Home).

- [Vision Statement](../../wiki/Vision%20Statement)
- [Development Plan](../../wiki/Development%20Plan)
- [Domain Model](https://github.com/PhumrapeeC/ku-polls/wiki/Domain-Model)
- [Requirements](../../wiki/Requirements)
- [Iteration 1 Plan](https://github.com/PhumrapeeC/ku-polls/wiki/Iteration-1-Plan)
- [Iteration 2 Plan](https://github.com/PhumrapeeC/ku-polls/wiki/Iteration-2-plan)
- [Iteration 3 Plan](https://github.com/PhumrapeeC/ku-polls/wiki/Iteration-3-Plan)
- [Iteration 4 Plan](https://github.com/PhumrapeeC/ku-polls/wiki/Iteration-4-Plan)

[django-tutorial]: TODO-write-the-django-tutorial-URL-here

## Admin User
| Username  | Password        | 
|-----------|-----------------|
|   admin   | 1234 | 

## Demo User
| Username  | Password        | 
|-----------|-----------------|
|   snowden1   | kupoll11234 | 
|   snowden2   | kupoll21234 | 

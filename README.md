## KU Polls: Online Survey Questions 
[![Django CI](https://github.com/PhumrapeeC/ku-polls/actions/workflows/django.yml/badge.svg)](https://github.com/PhumrapeeC/ku-polls/actions/workflows/django.yml)

An application to conduct online polls and surveys based
on the [Django Tutorial project][django-tutorial], with
additional features.

This app was created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at Kasetsart University.

## Install and Run
### Using setup script
1. Clone the repository and change directory into the repo
   ```
   git clone https://github.com/Jwizzed/ku-polls.git
   cd ku-polls
   ```
### Manual Installation
1. Clone the repository
   ```
   https://github.com/PhumrapeeC/ku-polls.git
   ```
2. Change directory into the repo
   ```
   cd ku-polls
   ```
3. Create a virtual environment
   ```
   python -m venv .venv
   ```
4. Activate the virtual environment:
   ```
   # On Linux or MacOS:
   source .venv/bin/activate
   
   # On Windows:
   .venv\Scripts\activate
   ```
5. Create a .env file by copying the contents of sample.env
   
   ```
   # On Linux/MacOS:
   cp sample.env .env

   # On Windows:
   copy sample.env .env
   ```
   Note: After copying, make sure to edit the .env file to set any environment-specific values as needed.
6. Install the required packages
   ```
   pip install -r requirements.txt
   ```
7. Start the Django server
   ```
   python manage.py runserver
   ```

## Project Documents

All project documents are in the [Project Wiki](../../wiki/Home).

- [Vision Statement](../../wiki/Vision%20Statement)
- [Development Plan](../../wiki/Development%20Plan)
- [Requirements](../../wiki/Requirements)
- [Iteration 1 Plan](https://github.com/PhumrapeeC/ku-polls/wiki/Iteration-1-Plan)
- [Iteration 2 Plan](https://github.com/PhumrapeeC/ku-polls/wiki/Iteration-2-plan)
- [Iteration 3 Plan](https://github.com/PhumrapeeC/ku-polls/wiki/Iteration-3-plan)

[django-tutorial]: TODO-write-the-django-tutorial-URL-here

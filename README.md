# Catan
Project of the game Catan's Colons, fro the subject Software Engineer in 2019

It is a project carried out thanks to teamwork. The working group was appointed by professors from the university in which we studied

Some of us take care of the backend and the rest of the frontend. And at the end of each part, we put them together

## Steps for install and play:

$ git clone https://github.com/agusantarelli/Catan.git

### Install all the requirements and run the backend
- $ cd Catan/
- $ cd backend/
- $ python -m venv catangame
- $ source catangame/bin/activate
- $ pip install -r requiements.txt
- $ cd catan/
- $ python manage.py runserver

### Run the frontend 
- $ cd Catan/
- $ cd frontend/
- $ npm install
- $ echo 'REACT_APP_API="http://localhost:8000/"' > .env
- $ npm run mockapi & npm start

Then a window will open in the browser with the game.Enjoy it!

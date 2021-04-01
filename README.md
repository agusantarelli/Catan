# Catan
Project of the game Catan's Colons, fro the subject Software Engineer in 2019

Steps for install and play:

1. git clone https://github.com/agusantarelli/Catan.git

2. Lets install all of the backend's requirements and then we run server:
- cd Catan/
- cd backend/
- python -m venv catangame
- source catangame/bin/activate
- pip install -r requiements.txt
- cd catan/
- python manage.py runserver
3. Now open another terminal and follow this steps for the frontend:
- cd Catan/
- cd frontend/
- npm install
- echo 'REACT_APP_API="http://localhost:8000/"' > .env
- npm run mockapi & npm start
4. In the terminal that you install all for the frontend, it gives you an URL. Put it on the navegator's internet
4. Enjoy it!

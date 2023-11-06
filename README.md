Start virtualenv: source venv/bin/activate
Run development server: python manage.py runserver --settings=koskin.settings_dev
Create requirements: pip freeze > requirements.txt
Start frontend application: 
    export NODE_OPTIONS=--openssl-legacy-provider 
    npm install
    npm run start

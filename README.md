# PS

Setting up:
1. Clone this repository: ``git clone https://github.com/eddumpy/PS.git``
2. Ensure Postgres is installed on your computer, to install follow instructions at: https://www.postgresql.org/download/
3. You also need to make sure you have Postgis installed
4. Create a new Postgres user if you do not have one, if not follow: https://www.postgresql.org/docs/9.1/app-createuser.html
5. Once you have created a new user, open up the terminal window and run the command with the name of the user from step 3: ``psql -U <user>`` and then you will be prompted to enter the password for the user.
6. Then run the following commands in the psql shell:
    - ``CREATE DATABASE polestar;``
    - ``\c polestar;``
    - ``CREATE EXTENSION postgis;``
7. Now the database is ready to use, goto the `settings.py` in the settings folder of the code and then edit the following fields to the names of your user and database:
 - `DATABASE_USER = <user>`
 - `DATABASE_PASSWORD = <user_password>`
 
Running the code:
1. Create virtualenv and run `pip install -r requirements.pip`
2. Run the migrations: `./manage.py migrate`
3. Run the server `./manage.py runserver`
4. The API should now be accessible at `http://localhost:8000`
5. You now have access to the endpoints!

- `localhost:8000/api/ships`
- `localhost:8000/api/positions/<ship_imo>/`
- for running `index.html`, it is located at root:
`localhost:8000/`

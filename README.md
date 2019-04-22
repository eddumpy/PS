# PS

To run this code:
1. Clone this repository using the command:
 
    ``git clone https://github.com/eddumpy/PS.git``
2. Ensure Postgres is installed on your computer, to install follow instructions at: 
3. Open a new terminal window and create a new database in psql
4. Install postgis and create extension
5. Use details of database and enter it in the settings.py file
6. Once cloned create a new virtual environment in the same directory as the code.
7. Activate the virtual environment and run the below command for all installations needed:
    
    ``pip install -r requirements.pip``
8. Run the server ./manage.py runserver
9. You now have access to the endpoints!

`localhost:8000/api/ships`
`localhost:8000/api/positions/<ship_imo>/`

for index.html, it is located at root:
`localhost:8000/`
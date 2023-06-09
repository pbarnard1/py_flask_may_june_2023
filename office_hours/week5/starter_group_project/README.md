# This is starter code for the week 5 group challenge.

## Project set-up
1. Grab the .zip folder.  You might need to delete at least the Pipfile.lock - and maybe the Pipfile as well, depending on what you have installed in terms of Python version.  (Adrian is using version 3.10, while you likely are using 3.11.)
2. Find a place to unzip this folder.
3. Take the schema in the folder named "ERD_folder" and forward-engineer that schema.  You may rename the schema if you wish.
4. If necessary, please go to your mysqlconnection.py file and change the password.  Also change the port number in your server.py file if needed.
5. Install as needed.

## Creating an athlete in the database
Take a look at your schema so you can see what columns and tables you have.  Once you're done there, also take a look at the file named "add_athlete.html".

1. Go to your controllers folder and look for a file named "athletes.py".  You should see two main routes (plus the root route).  Are there any other routes you'll need?
2. In the "add_athlete.html", there are some pieces missing in your form.  Fill in the missing pieces.
3. In your models folder, you should see a file called "athlete.py".  Add the schema name as needed.
4. Write a class method that will allow you to add an athlete to your database.  Make sure you have the query correct!  Do you need to pass in a 'data' parameter?
5. In your "athletes.py" controller, add some code that will take your form and call on the class method to add the athlete to the database.  Don't forget to redirect to the route that shows all athletes!  Make sure you import your model (file)!
6. Go ahead and add an athlete through your form to test this out.  Now go to MySQL Workbench and double-check to make sure your athlete was added to the database.  If not, it's time to do some debugging!

## Grabbing all athletes from the database
Let's create a new class method that will grab all the athletes from your database.

1. Write the query that will grab all the athletes.  Make sure you store your rows of data you get back as a list of dictionaries into a new variable (you'll usually see this as "results", but you can use another name if you wish).
2. Create a new list that will hold a bunch of Athlete objects.
3. Write a loop that will go through each dictionary:
    - In your loop, create a new Athlete object - how would you do that?
    - Take this new Athlete object and add it to the list of Athlete objects.
4. Make sure you return this new list!
5. In your controller file, call on this class method and store the list in a new variable.  Make sure you pass this list to the HTML!

Now let's go to the HTML: you'll build either a table or an unordered list that will show all the athletes from the database. Make sure you include the id, full name and the sport at a minimum.

1. Add some sort of loop in the HTML to go through this list of athletes.  Make sure you end the loop!
2. Inside your loop, display at least the ID, full name and the sport.  
<h1>Book Catalogue Full-Stack Application - Running Guide</h1>

<p>This guide will walk you through the steps to set up and run the Book Catalogue Full-Stack Application locally. The application combines a React frontend with a Django API backend for managing a book catalogue.</p>

<h1>Prerequisites</h1>
<p>Before you begin, make sure you have the following installed on your system:</p>
<ul>
  <li>Python (>=3.6)</li>
  <li>Node.js (LTS version recommended)</li>
  <li>npm (comes with Node.js installation)</li>
</ul>

<h1>Installation</h1>
<h2>Set Up Django Backend</h2>
<h3>1.Install Python dependencies:</h3>
<p>pipenv shell</p>

<h2>Apply migrations:</h2>
<p>python manage.py migrate</p>

<h2>Run the Django development server:</h2>
<p>python manage.py runserver</p>

<h1>Set Up React Frontend</h1>
<h2>1.Navigate to the frontend directory:</h2>
<p>cd frontend</p>

<h2>Install Node.js dependencies:</h2>
<p>npm install</p>

<h2>Start the React development server:</h2>
<p>npm start</p>

<h1>Access the Application</h1>
<p>Open your web browser and navigate to http://localhost:8000 to access the Book Catalogue.</p>

<h1>Running the Application</h1>
<p>Django backend: http://localhost:8000</p>
<p>React frontend: http://localhost:3000</p>

<h1><b>NOTES (Django Admin Login)</b></h1>
<p>username: admin</p>
<p>password: admin</p>

<h1><b>API Endpoints</b></h1>
<h3>1. Get List of Books</h3>
<p>http://localhost:8000/api/books</p>

<h3>2. Get Single Book</h3>
<p>http://localhost:8000/api/books/id</p>

<h3>3. Add New Book</h3>
<p>http://localhost:8000/api/books</p>
<p><b>Method:</b> POST</p>

<h3>4. Update Book</h3>
<p>http://localhost:8000/api/books/id</p>
<p><b>Method: </b>PUT</p>


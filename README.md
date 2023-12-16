<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>User Service API</h1>

<p>This repository contains the source code for a Flask-based User Service API. The API provides endpoints for user registration, login, user information retrieval, user editing, and user deletion. It includes functionality for both regular users and administrators.</p>

<h2>Prerequisites</h2>

<p>Make sure you have the following installed:</p>

<ul>
    <li>Python (3.6 or higher)</li>
    <li>Flask</li>
    <li>Flask-Session</li>
    <li>Flask-Login</li>
    <li>SQLAlchemy</li>
    <li>jwt</li>
    <li>secrets</li>
    <li>[other dependencies]</li>
</ul>

<h2>Installation</h2>

<ol>
    <li>Clone the repository:</li>
</ol>

<pre><code>git clone https://github.com/your-username/user-service-api.git
cd user-service-api
</code></pre>

<ol start="2">
    <li>Install the dependencies:</li>
</ol>

<pre><code>pip install -r requirements.txt
</code></pre>

<h2>Configuration</h2>

<p>Open the <code>config.py</code> file and update the configuration settings as needed. Set the database connection details and any other relevant configurations.</p>

<h2>Database Setup</h2>

<p>Make sure to set up your database and apply the necessary migrations. For example, using Flask-Migrate:</p>

<pre><code>flask db init
flask db migrate
flask db upgrade
</code></pre>

<h2>Usage</h2>

<p>Run the Flask application:</p>

<pre><code>flask run
</code></pre>

<p>The API will be accessible at <code>http://127.0.0.1:5000/</code>.</p>

<h2>Endpoints</h2>

<ol>
    <li><strong>Admin User Registration</strong></li>
    <ul>
        <li><strong>Endpoint:</strong> <code>/api/admin/create</code></li>
        <li><strong>Method:</strong> <code>POST</code></li>
        <li><strong>Description:</strong> Register a new admin user.</li>
    </ul>
    <li><strong>Regular User Registration</strong></li>
    <ul>
        <li><strong>Endpoint:</strong> <code>/api/user/create</code></li>
        <li><strong>Method:</strong> <code>POST</code></li>
        <li><strong>Description:</strong> Register a new regular user.</li>
    </ul>
    <li><strong>User Login</strong></li>
    <ul>
        <li><strong>Endpoint:</strong> <code>/api/user/login</code></li>
        <li><strong>Method:</strong> <code>POST</code></li>
        <li><strong>Description:</strong> Log in a user and generate a JWT token.</li>
    </ul>
    <!-- Repeat for other endpoints -->
</ol>

<h2>Contributing</h2>

<p>Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.</p>

<h2>License</h2>

<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

</body>
</html>

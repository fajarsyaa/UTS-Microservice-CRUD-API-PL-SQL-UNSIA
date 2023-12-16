<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>UTS PL/SQL Kelompok 13</h1>
<h2>Anggota Kelompok</h2>
<ol>
    <li>MUKHAMAD FAJAR SYAIHU WALID</li>
    <li>RAFI ANDHIKA GALUH</li>
</ol>
<br/><br/>

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
        <li><strong>cUrl:</strong> <pre><code>curl --location 'http://127.0.0.1:5000/api/admin/create' \
--header 'Content-Type: application/json' \
--header 'Cookie: session=.eJwljsluwjAURf_F6wp5jGN2bYDiiEG0ZdwgPw9gQlJmAVX_vZa6PDpHV_cHrcPJn7eofTld_QtaR4faCJRlghKWgzegOA0yCzI3IfhgQm6ASRxIRoTLScgsAWrAAjAVOCPUeS4yr3IcPKeOSCoVS4py5QQQyq3yNMdcYoGdwZI76r1zgWGTGRcsGCJQOnI9-9P_G8oSX74r3yTwj3IL7zaOY6mnT01GUZ918yFsoTNdHRazolStFBFLZw-oe5fVZxLN7Lla6Dgoyr3vv8bxrsuGHc2Hu8191EkD9f65oL0K5vur3h3q5fyeetwalLITYSLtbUIjb-RtIyo4dI9FLL5qeJv2V7DMqlH_aKbo9w9x4WcD.ZX3G7g.5IY-aIefKkWZuE47uBRbTikQCcw' \
--data-raw '{
    "first_name":"administrator",
    "last_name":"ohhh",
    "email":"admin321@gmail.com",
    "username":"administrator",
    "password":"Admin@123"
}'</code></pre></li>
    </ul>
    <li><strong>Regular User Registration</strong></li>
    <ul>
        <li><strong>Endpoint:</strong> <code>/api/user/create</code></li>
        <li><strong>Method:</strong> <code>POST</code></li>
        <li><strong>Description:</strong> Register a new regular user.</li>
        <li><strong>cUrl:</strong> <pre><code>curl --location 'http://127.0.0.1:5000/api/user/create' \
--header 'Content-Type: application/json' \
--header 'Cookie: session=.eJwljsluwjAURf_F6wp5jGN2bYDiiEG0ZdwgPw9gQlJmAVX_vZa6PDpHV_cHrcPJn7eofTld_QtaR4faCJRlghKWgzegOA0yCzI3IfhgQm6ASRxIRoTLScgsAWrAAjAVOCPUeS4yr3IcPKeOSCoVS4py5QQQyq3yNMdcYoGdwZI76r1zgWGTGRcsGCJQOnI9-9P_G8oSX74r3yTwj3IL7zaOY6mnT01GUZ918yFsoTNdHRazolStFBFLZw-oe5fVZxLN7Lla6Dgoyr3vv8bxrsuGHc2Hu8191EkD9f65oL0K5vur3h3q5fyeetwalLITYSLtbUIjb-RtIyo4dI9FLL5qeJv2V7DMqlH_aKbo9w9x4WcD.ZX3G7g.5IY-aIefKkWZuE47uBRbTikQCcw' \
--data-raw '{
    "first_name":"user",
    "last_name":"biasa",
    "email":"userbiasa@gmail.com",
    "username":"user",
    "password":"User@123"
}'</code></pre></li>
    </ul>
    <li><strong>User Login</strong></li>
    <ul>
        <li><strong>Endpoint:</strong> <code>/api/user/login</code></li>
        <li><strong>Method:</strong> <code>POST</code></li>
        <li><strong>Description:</strong> Log in a user and generate a JWT token.</li>
        <li><strong>cUrl:</strong> <pre><code>curl --location 'http://127.0.0.1:5000/api/user/login' \
--header 'Content-Type: application/json' \
--header 'Cookie: session=.eJwljsluwjAURf_F6wp5jGN2bYDiiEG0ZdwgPw9gQlJmAVX_vZa6PDpHV_cHrcPJn7eofTld_QtaR4faCJRlghKWgzegOA0yCzI3IfhgQm6ASRxIRoTLScgsAWrAAjAVOCPUeS4yr3IcPKeOSCoVS4py5QQQyq3yNMdcYoGdwZI76r1zgWGTGRcsGCJQOnI9-9P_G8oSX74r3yTwj3IL7zaOY6mnT01GUZ918yFsoTNdHRazolStFBFLZw-oe5fVZxLN7Lla6Dgoyr3vv8bxrsuGHc2Hu8191EkD9f65oL0K5vur3h3q5fyeetwalLITYSLtbUIjb-RtIyo4dI9FLL5qeJv2V7DMqlH_aKbo9w9x4WcD.ZX3G7g.5IY-aIefKkWZuE47uBRbTikQCcw' \
--data '{
    "username":"user",
    "password":"user123"
}'</code></pre></li>
    </ul>
    <li><strong>Get All Users</strong></li>
    <ul>
        <li><strong>Endpoint:</strong> <code>/api/users</code></li>
        <li><strong>Method:</strong> <code>GET</code></li>
        <li><strong>Description:</strong> Retrieve information for all users.</li>
        <li><strong>cUrl:</strong> <pre><code>curl --location 'http://127.0.0.1:5000/api/users' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIiLCJleHAiOjE3MDI4MjgxNDIsImlzX2FkbWluIjpmYWxzZX0.LJ7DibQ7cvQ2i4n7vg5kbpEqCiCTmbBUHZbY6kNHqaU' \
--header 'Cookie: session=.eJwljsluwjAURf_F6wp5jGN2bYDiiEG0ZdwgPw9gQlJmAVX_vZa6PDpHV_cHrcPJn7eofTld_QtaR4faCJRlghKWgzegOA0yCzI3IfhgQm6ASRxIRoTLScgsAWrAAjAVOCPUeS4yr3IcPKeOSCoVS4py5QQQyq3yNMdcYoGdwZI76r1zgWGTGRcsGCJQOnI9-9P_G8oSX74r3yTwj3IL7zaOY6mnT01GUZ918yFsoTNdHRazolStFBFLZw-oe5fVZxLN7Lla6Dgoyr3vv8bxrsuGHc2Hu8191EkD9f65oL0K5vur3h3q5fyeetwalLITYSLtbUIjb-RtIyo4dI9FLL5qeJv2V7DMqlH_aKbo9w9x4WcD.ZX3G7g.5IY-aIefKkWZuE47uBRbTikQCcw'</code></pre></li>
    </ul>
    <li><strong>Edit User</strong></li>
    <ul>
        <li><strong>Endpoint:</strong> <code>/api/user/edit/<int:user_id></code></li>
        <li><strong>Method:</strong> <code>PUT</code></li>
        <li><strong>Description:</strong> Edit user information (admin access required).</li>
        <li><strong>cUrl:</strong> <pre><code>curl --location --request PUT 'http://127.0.0.1:5000/api/user/edit/20' \
--header 'client-api-key: fajarfajarfajar' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIiLCJleHAiOjE3MDI4MjgxNDIsImlzX2FkbWluIjpmYWxzZX0.LJ7DibQ7cvQ2i4n7vg5kbpEqCiCTmbBUHZbY6kNHqaU' \
--header 'Cookie: session=.eJwljsluwjAURf_F6wp5jGN2bYDiiEG0ZdwgPw9gQlJmAVX_vZa6PDpHV_cHrcPJn7eofTld_QtaR4faCJRlghKWgzegOA0yCzI3IfhgQm6ASRxIRoTLScgsAWrAAjAVOCPUeS4yr3IcPKeOSCoVS4py5QQQyq3yNMdcYoGdwZI76r1zgWGTGRcsGCJQOnI9-9P_G8oSX74r3yTwj3IL7zaOY6mnT01GUZ918yFsoTNdHRazolStFBFLZw-oe5fVZxLN7Lla6Dgoyr3vv8bxrsuGHc2Hu8191EkD9f65oL0K5vur3h3q5fyeetwalLITYSLtbUIjb-RtIyo4dI9FLL5qeJv2V7DMqlH_aKbo9w9x4WcD.ZX3G7g.5IY-aIefKkWZuE47uBRbTikQCcw' \
--data-raw '{
    "first_name":"administrator",
    "last_name":"adminnnn",
    "username":"admin",
    "email":"admin@gmail.com"
}'</code></pre></li>
    </ul>
    <li><strong>Delete User</strong></li>
    <ul>
        <li><strong>Endpoint:</strong> <code>/api/user/delete/<int:user_id></code></li>
        <li><strong>Method:</strong> <code>DELETE</code></li>
        <li><strong>Description:</strong> Delete a user (admin access required).</li>
        <li><strong>cUrl:</strong> <pre><code>curl --location --request DELETE 'http://127.0.0.1:5000/api/user/delete/20' \
--header 'client-api-key: fajarfajarfajar' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIiLCJleHAiOjE3MDI4MjgxNDIsImlzX2FkbWluIjpmYWxzZX0.LJ7DibQ7cvQ2i4n7vg5kbpEqCiCTmbBUHZbY6kNHqaU' \
--header 'Cookie: session=.eJwljsluwjAURf_F6wp5jGN2bYDiiEG0ZdwgPw9gQlJmAVX_vZa6PDpHV_cHrcPJn7eofTld_QtaR4faCJRlghKWgzegOA0yCzI3IfhgQm6ASRxIRoTLScgsAWrAAjAVOCPUeS4yr3IcPKeOSCoVS4py5QQQyq3yNMdcYoGdwZI76r1zgWGTGRcsGCJQOnI9-9P_G8oSX74r3yTwj3IL7zaOY6mnT01GUZ918yFsoTNdHRazolStFBFLZw-oe5fVZxLN7Lla6Dgoyr3vv8bxrsuGHc2Hu8191EkD9f65oL0K5vur3h3q5fyeetwalLITYSLtbUIjb-RtIyo4dI9FLL5qeJv2V7DMqlH_aKbo9w9x4WcD.ZX3G7g.5IY-aIefKkWZuE47uBRbTikQCcw' \
--data-raw '{
    "first_name":"okwe",
    "username":"muezaaa",
    "email":"jarxsa@gmail.com"
}'</code></pre></li>
    </ul>
    
</ol>

</body>
</html>

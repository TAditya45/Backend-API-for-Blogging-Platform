# Backend-API-for-Blogging-Platform

Backend API for Blogging Platform
This is a backend API for a blogging platform that allows users to create and manage their blogs and comments.

Technologies Used

            Python
            Django
            Django REST framework
            PostgreSQL              




Functionality
The API has the following endpoints:

      Users
                  GET /users: Returns a list of all users.
                  POST /users: Creates a new user.
                  GET /users/{id}: Returns the details of a specific user.
                  PUT /users/{id}: Updates the details of a specific user.
                  DELETE /users/{id}: Deletes a specific user.
                  
      Blogs
                  GET /blogs: Returns a list of all blogs.
                  POST /blogs: Creates a new blog.
                  GET /blogs/{id}: Returns the details of a specific blog.
                  PUT /blogs/{id}: Updates the details of a specific blog.
                  DELETE /blogs/{id}: Deletes a specific blog.
                  
      Comments
                  GET /comments: Returns a list of all comments.
                  POST /comments: Creates a new comment.
                  GET /comments/{id}: Returns the details of a specific comment.
                  PUT /comments/{id}: Updates the details of a specific comment.
                  DELETE /comments/{id}: Deletes a specific comment.
                  
      Friends
                  GET /users/{id}/level/{levelNo}: Returns a list of all friends at the specified level for the given user.


Testing
Unit tests for the API endpoints and friend finding functions are included in the tests directory. Run the tests using the following command:


Clone the repository to your local machine:

git clone https://github.com/TAditya45/Backend-API-for-Blogging-Platform

Install the required dependencies:

            pip install -r requirements.txt

Set up the database by running the following command:

            python manage.py migrate

Start the development server:
           
           python manage.py runserver

You can access the APIs using the following URLs:

            Users API: http://localhost:8000/users/

            Blogs API: http://localhost:8000/blogs/

            Comments API: http://localhost:8000/comments/

To retrieve the n-th level friends of a user, you can use the following API:

            GET /users/<user_id>/level/<level_no>/friends/

            For example, to retrieve the 2nd level friends of user with ID 1, use the following URL: http://localhost:8000/users/1/level/2/friends/


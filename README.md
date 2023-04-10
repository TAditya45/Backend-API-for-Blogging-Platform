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



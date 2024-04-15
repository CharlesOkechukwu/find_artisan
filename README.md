# FIND ARTISAN WEB APPLICATION

## Description
To solve the problem of people who moved into a new city or neigbourhood having difficulty to source great artisans, I came up with an idea of a web application to connect users to artisans around them.
This application would enable users in Nigeria locate service providres/artisans around them. It employs a simple feature to display artisans or service providres in the city of the user. The user can click on an artisan's profile to retrieve details about the various services the artisan offer, contact the artisan through the contact details provided by the artisan and after using the artisan's service, leave a review and rating of the service for future users to see.

The application is deployed here: http://web-01.codefotress.tech


### Technologies Used:
* Front-End: HTML, jinja, CSS and Jquery

* Backend: 
    - Framework: Flask
    - Database: MySQL
    - External Libraries used:
        * SQLAlchemy: Object-relational mapping
        * Bcrypt: passowrd encryption
        * Geopy(Nonatim): geocoding of addresses to latitude and longitude coordinates and calculation of distance from two points.

### Login page:
route: /api/login
Recieves two inputs which includes the email and password of the user and on sucessful verification, logs in the user. Only a logged in user can leave a review of an artisan.

### Signup page:
route: /api/signup
Enables a user register for the findartisan service, only registered users can leave reviews of an artisan. It requires the following fields:
* name
* email
* address
* city
* state
* country
* password
On sucessful registration, the user is now allowed to add their service if he/she is an artisan.

![homepage](/api/static/images/home.png)

### Add Services
When adding a service you render, you must be logged in or have an account. In the form that is displayed, the user would enter the following information:
Business name, business address, service to render, city, state, country, phone number, email, bio and photos. You can also update the records of a service or delete a service.

### Find Artisan
To search for an artisan near you, user is to enter the service he/she is in search for, the service would be autocompleted based on the services already registered in the database, the user if logged in would have his/her address and details already filled. The user is to use the filter to determine the range of the search, the user can decide to limit search to only artisans close to him/her not more than 30 kilometers from the current location of the user, or search within his/her current city, state or country.

![Display](/api/static/images/display.png)

The results are displayed and the user can click to expand the details of each artisan, where the user can see the review of the service rendered by the artisan.

The user would also be able get the contact details of the artisan, and also make a review of the service of the artisan after using the artisan's service.

![artisan](/api/static/images/singlepage.png)

### Authors:
Charles Okechukwu
I worked alone on this project.
LinkedIn: https://www.linkedin.com/in/charles-okechukwu-6a0b171ba/
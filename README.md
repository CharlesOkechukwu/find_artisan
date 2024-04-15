# FIND ARTISAN WEB APPLICATION

## Description
This application would enable users in Nigeria locate service providres/artisans around them. It employs a simple feature to display artisans or service providres in the city of the user. The user can click on an artisan's profile to retrieve details about the various services the artisan offer, contact the artisan through the contact details provided by the artisan and after using the artisan's service, leave a review and rating of the service for future users to see.

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
![homepage](https://github.com/CharlesOkechukwu/find_artisan/api/static/images/home.png)
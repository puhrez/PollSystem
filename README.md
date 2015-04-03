#Engagement Polling System

###Testing
to test: run nosetests


###Objective
To create a system where users may easily create polls which engage users in deep thinking about issues and measures where priorities lie in regard to those issues.

###Stack
#####Backend Stack
- RESTful API written in Python with flask
- Persistence in PostgreSQL
- Deployment on Heroku
- Integration testing with Travis

###Models and Relationships*

<img src="https://s3.amazonaws.com/nighnight.com/assets/LPSchemeDesignV2.png" alt="Schema Design v2" style="width: 100%;"> 

* token needs no longer has is_upperbound or is_lowerbound, and now has an int value.



###EndPoints
**/api/user(?offset=0&limit=0)**

* GET - Retrieves all users starting from the record at offset + 1, only taking to limit
* POST - Creates a new user

**/api/user/<userid>(?fields=\**kwargs)**

* GET - Retrieves the information for user with id userid
* PUT - Updates the user's information
* DELETE - Deletes the user

**/api/polls(?offset=0&limit=0)**

* GET - Retrieves all polls starting from the record at offset + 1, only taking o limit
* POST - Creates a new poll

**/api/polls/<pollid>(?fields=\**kwargs)**

* GET - Retrieve the information for poll with id pollid
* PUT - Update the poll's information
* DELETE - Deletes the Poll

**/api/questions(?offset=0&limit=0)**

* GET - Retrieves all questions starting from the record at offset + 1, only taking to limit
* POST - Creates a new question

**/api/questions/<questionid>(?fields=\**kwargs)**

* GET - Retrieves the information for user with id questionid
* PUT - Updates the question's information
* DELETE - Deletes the question

**/api/effects(?offset=0&limit=0)**

* GET - Retrieves all effects starting from the record at offset + 1, only taking to limit
* POST - Creates a new effects

**/api/effects/<effectsid>(?fields=\**kwargs)**

* GET - Retrieves the information for effect with id effectid
* PUT - Updates the effect information
* DELETE - Deletes the effect

**/api/tokens(?offset=0&limit=0)**

* GET - Retrieves all tokens starting from the record at offset + 1, only taking to limit
* POST - Creates a new tokens

**/api/tokens/<tokensid>(?fields=\**kwargs)**

* GET - Retrieves the information for token with id tokenid
* PUT - Updates the token's information
* DELETE - Deletes the token


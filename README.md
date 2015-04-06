#Engagement Polling System

[![Build Status](https://travis-ci.org/xbs13/PollSystem.svg?branch=master)](https://travis-ci.org/xbs13/PollSystem)

###Objective
To create a system where users may easily create polls which engage users in deep thinking about issues and measures where priorities lie in regard to those issues.

###Stack
#####Backend Stack
- RESTful API written in Python 2.7 with Flask
- Persistence in PostgreSQL
- Deployment on [Heroku](https://poll-system.herokuapp.com/)
- Integration testing with [Travis](https://travis-ci.org/xbs13/PollSystem)

#####Installation
<pre><code>git clone https://github.com/xbs13/PollSystem
cd PollSystem
pip install -r requirements.txt</code></pre>
#####Running
<pre><code>chmod a+x run.py
./run.py
# or
python run.py</code></pre>
#####Creation of DB Management system
<pre><code>chmod a+x db_<action>
./db_<action>.py
# or
python db_<action>.py</code></pre>
#####Testing
<pre><code>nosetests<code></pre>
###Models and Relationships*

<img src="https://s3.amazonaws.com/nighnight.com/assets/LPSchemeDesignV2.png" alt="Schema Design v2" style="width: 100%;"> 

* token needs no longer has is_upperbound or is_lowerbound, and now has an int value.



###EndPoints
**/api/user(?offset=0&limit=0)**

* GET - Retrieves all users starting from the record at offset + 1, only taking to limit
* POST - Creates a new user

**/api/user/<userid>**

* GET - Retrieves the information for user with id userid
* PUT - Updates the user's information
* DELETE - Deletes the user

**/api/polls(?offset=0&limit=0)**

* GET - Retrieves all polls starting from the record at offset + 1, only taking o limit
* POST - Creates a new poll

**/api/polls/<pollid>**

* GET - Retrieve the information for poll with id pollid
* PUT - Update the poll's information
* DELETE - Deletes the Poll

**/api/polls/<pollid>/tokens**

* GET - Get all the tokens for poll of pollid
* POST - Creates a new token for poll of pollid

**/api/polls/<pollid>/questions**

* GET - Get all the questions for poll of pollid
* POST - Creates a new question for poll of pollid

**/api/questions(?offset=0&limit=0)**

* GET - Retrieves all questions starting from the record at offset + 1, only taking to limit

**/api/questions/<questionid>**

* GET - Retrieves the information for user with id questionid
* PUT - Updates the question's information
* DELETE - Deletes the question

**/api/questions/<questionid>/effects**

* GET - Get all the effects for question of questionid
* POST - Creates a new effect for question of questionid

**/api/effects(?offset=0&limit=0)**

* GET - Retrieves all effects starting from the record at offset + 1, only taking to limit

**/api/effects/<effectsid>**

* GET - Retrieves the information for effect with id effectid
* PUT - Updates the effect information
* DELETE - Deletes the effect

**/api/tokens(?offset=0&limit=0)**

* GET - Retrieves all tokens starting from the record at offset + 1, only taking to limit

**/api/tokens/<tokensid>**

* GET - Retrieves the information for token with id tokenid
* PUT - Updates the token's information
* DELETE - Deletes the token


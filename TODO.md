###Admin todo:
1. get inline effect model 'token_id' column on effect to reflect foreign key constraint
2. get polls to be populated by logged in user's polls and poll_admin
3. get foreign key on Question to default to the poll being created
4. get foreign key on Effect to default to the question being created

###API todo:
1. write and pass tests for error responses.
2. authentication with flask-login
3. enable GET/PUTs of specific resources access certain fields either by authorization to do so or choice by user.
4. better error responces refer to [Apigee's API guide page 13](https://pages.apigee.com/rs/apigee/images/api-design-ebook-2012-03.pdf)
5. listviews accept offeset and limit params that affect returned object

###Frontend todo:
1. figure out life. 
2. Research more into Ionic/Titanium
3. Research more into Processing/React + Backbone

###General todo:
1. look to see where Context Managers and Generators can make the API more Pythonic
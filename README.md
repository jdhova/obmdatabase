
Develop a backend API application where you can list members based on their name, company
name and office address. You should also be able to get, patch, update or delete members by id.
When a member is returned from the API, the following information should be returned: first
name, infix, last name, photo, company name, job title, company photo, company address.
Technical Requirements
The API should accept requests using the REST methodology and naming convention. The API
methods should accept GET or POST parameters, depending on the type of request. The
backend API application validates all incoming parameters and gives appropriate error messages
in case the API is accessed incorrectly.
The assignment should be delivered with source files and instructions for running the backend API
application. It should also make use of the following technologies:

Extras
Expand the API with the following functionality:
Programming Language Python
Programming Frameworks Django, Django Rest Framework
Database PostgreSQL

Authentication Use OAuth 2.0 to get access tokens and refresh
tokens. The list method should be public, but all
other methods should be protected.

Authorization Use permission based system for more control over
access to protected resources. A user should only
be able to get, update or delete members from their
own company. An admin user should get full
access.

Companies Create a foreign key relationship between users and
companies. The company API should get it's own
list, get, patch, update and delete methods. It
should also be possible to filter the member list
method based on a company id.


API Documentation
The description of the REST APIs in the project are given below
Get Members List:
Get a list of members matching the additional filters provided. If no filter is provided, returns all available members.
URL: http://127.0.0.1:8000/memberslist/
Method Type: GET
Required Parameters: None
Optional Parameters: 
	•	firstName
	•	lastName
	•	companyName
	•	companyAddress
Response:
The response object consists of the following attributes.
	•	Status
	•	List of members matching the criteria.
Get Member by Id:
Returns a single member matching the id provided. If no member exists returns an error message.
URL: http://127.0.0.1:8000/getmemberbyid/
Method Type: GET
Required Parameters: 
	•	id
Optional Parameters: None
Response:
The response object consists of the following attributes.
	•	Status
	•	Member matching the id parameter.

Patch Member by Id:
Patched certain fields of the member matching the given id. The fields to patch are provided by the user as optional parameters.
URL: http://127.0.0.1:8000/patchmember/
Method Type: PATCH
Required Parameters: 
	•	Id
	•	fieldsToPatch
Optional Parameters: 
	•	firstName
	•	infix
	•	lastName
	•	photo
	•	companyName
	•	jobTitle
	•	companyPhoto
	•	companyAddress
Response:
The response object consists of the following attributes.
	•	Status
	•	Patched Member.

Update Member by Id:
Updates all the fields of the members matching the id.
URL: http://127.0.0.1:8000/updatemember/
Method Type: POST
Required Parameters: 
	•	Id
	•	fieldsToPatch
	•	firstName
	•	infix
	•	lastName
	•	photo
	•	companyName
	•	jobTitle
	•	companyPhoto
	•	companyAddress
	•	
Optional Parameters: None
Response:
The response object consists of the following attributes.
	•	Status
	•	Updated Member.

Delete Member by Id:
Deletes a member matching the id
URL: http://127.0.0.1:8000/deletemember/
Method Type: POST
Required Parameters: 
	•	Id
Optional Parameters: None
Response:
The response object consists of the following attributes.
	•	Status



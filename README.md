# fusus_exercise
## Django REST API Exercise

## Models
- Organization
  - id
  - name
  - phone
  - address
  
- User
  - id
  - name
  - phone
  - email
  - organization
  - birthdate
  
 
## API Endpoints
## API's support JWT authentication

- POST /api/auth/login/ using email address
- GET /api/auth/groups/ Should return Authentication Groups
 - Administrator: Full access to CRUD Any User in his org and RU Organization
 - Viewer: List and Retrieve and User in his org.
 - User: CRU his own user
 

## User Endpoints:
- GET /api/users/ List all the users for the user organization
- GET /api/users/{id}/ Retrieve user information, and the organization id and name
- POST /api/users/ Create an user for the organization, must set password as well
- PATCH /api/users/{id} Update user information
- DELETE /api/users/{id}

## Organization Endpoints:
- GET /api/organizations/{id}/ Retrieve organization information
- PATCH /api/organizations /{id} Update organization if request user is `Administrator`.
- GET /api/organization/{id}/users List all the users for the user organization if user is
  `Administrator` or `Viewer`. Must return just id and name of the user
- GET /api/organization/{id}/users/{id}/ Retrieve user id and name if if user is `Administrator`
or `Viewer`


## Other Endpoints:
- GET /api/info/ Should return {`user_name`, `id`, `organization_name`, `public_ip`} Public Ip must be the internet public IP of the server where code is running

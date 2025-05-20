Django Notes API with JWT Authentication

  1  A simple Django REST API that supports:

  2  User registration & login

  3  JWT-based authentication (access & refresh tokens)

  4  Logout using token blacklisting

  5  Notes CRUD operations scoped to the authenticated user

Tech Stack

    Backend: Django, Django REST Framework

    Authentication: JWT (via djangorestframework-simplejwt)

    Database: Msql

Setup Instructions
 
    1 Clone the repository
        
        git clone : https://github.com/it-rohit/notes_taking_app.git

    2 Create a virtual environment & install dependencies

        python -m venv env
        source env/bin/activate  
        pip install -r requirements.txt

3. Run migration

    python manage.py makemigrations
    
    python manage.py migrate

4. Run the server
    python manage.py runserver

Authentication

    >> This project uses JWT tokens. After logging in or registering, you’ll receive:

    >> access token (used for accessing protected endpoints)

    >> refresh token (used to obtain a new access token)


API Endpoints
    
    
    User Api end
    
    1. Register -- Method --post (Auth Not Required)
      
        url : http://127.0.0.1:8000/api/users/register/
        payload            :{
                "firstname":"dev",
                "lastname":"five",
                "username":"devfive",
                "email":"dev5@gmail.com",
                "password":"dev5"
            }
        
        response : {
               "message": "User registered successfully",
            "tokens": {
                        "refresh": "ascchs...",
                        "access": "ascchs..."
                        }
                    }


    2. Login -- MEthod -Post  (Auth Not Required)

        Url : http://127.0.0.1:8000/api/users/login/
         
        payload : {
                        "email":"dev5@gmail.com",
                        "password":"dev5"
                    }

        response : {
               "message": "Login successful",
            "tokens": {
                        "refresh": "ascchs...",
                        "access": "ascchs..."
                        }
                    }

    3 logout -- method- post (Auth Required)

        url :  http://127.0.0.1:8000/api/users/logout/
        payload:
            body>>{
                    "refresh": "gcvcvcjcjdcscdsc....."
                    }
                        "access": "ascchs..."
            header >>Authorization: Bearer <access_token>
            
            response : {
                            "message": "Logout successfully"
                        }

    Notes API (Auth Required) Authorization: Bearer <access_token>


        1. List Notes
            
            url :http://127.0.0.1:8000/api/users/notes/
            
            response : [
                            {
                                "note_id": "89cf62be-84dd-4af1-910e-99b8ec783be0",
                                "note_title": "dev_5a",
                                "note_content": "sample22",
                                "last_update": "2025-05-20T07:56:02.768140Z",
                                "created_on": "2025-05-20T07:20:21.192502Z",
                                "user": "1a9dd4b5-7b6b-4bd8-99ae-110b2ff41f9c"
                            },
                            {
                                "note_id": "c1862406-f9eb-442c-b32b-b2ff0ca47c22",
                                "note_title": "dev_5",
                                "note_content": "siample notes",
                                "last_update": "2025-05-20T07:07:13.450584Z",
                                "created_on": "2025-05-20T07:07:13.450584Z",
                                "user": "1a9dd4b5-7b6b-4bd8-99ae-110b2ff41f9c"
                            }
                        ]

        2. Create Note method --Post

            url : http://127.0.0.1:8000/api/users/notes/

            payload 
                Body:{
                            "note_title":"dev_5a",
                            "note_content":"sample2",
                            "user":"1a9dd4b57b6b4bd899ae110b2ff41f9c"
                        }
                

            response :
                                {
                    "note_id": "89cf62be-84dd-4af1-910e-99b8ec783be0",
                    "note_title": "dev_5a",
                    "note_content": "sample2",
                    "last_update": "2025-05-20T07:20:21.192502Z",
                    "created_on": "2025-05-20T07:20:21.192502Z",
                    "user": "1a9dd4b5-7b6b-4bd8-99ae-110b2ff41f9c"
                }
        3. Retrieve Note by ID method -- get

            url :http://127.0.0.1:8000/api/users/notes/89cf62be-84dd-4af1-910e-99b8ec783be0/
            response : {
                            "note_id": "89cf62be-84dd-4af1-910e-99b8ec783be0",
                            "note_title": "dev_5a",
                            "note_content": "sample22",
                            "last_update": "2025-05-20T07:56:02.768140Z",
                            "created_on": "2025-05-20T07:20:21.192502Z",
                            "user": "1a9dd4b5-7b6b-4bd8-99ae-110b2ff41f9c"
                        }

        4. Update Note -- method --Put
            url : http://127.0.0.1:8000/api/users/notes/89cf62be-84dd-4af1-910e-99b8ec783be0/

            payload:

                body : {
                        "note_title":"dev_5a",
                        "note_content":"sample22"
                        "user":"1a9dd4b57b6b4bd899ae110b2ff41f9c"
                    }

            RESPONSE : {
                            "note_id": "89cf62be-84dd-4af1-910e-99b8ec783be0",
                            "note_title": "dev_5a",
                            "note_content": "sample22",
                            "last_update": "2025-05-20T07:56:02.768140Z",
                            "created_on": "2025-05-20T07:20:21.192502Z",
                            "user": "1a9dd4b5-7b6b-4bd8-99ae-110b2ff41f9c"
                        }


        5. . Delete Note
            url : http://127.0.0.1:8000/api/users/notes/89cf62be-84dd-4af1-910e-99b8ec783be0/
            
            RESPONSE : {"message": "Note deleted successfully."}


# Robot on Mission (Python Django Backend)

## While using below link you may get warning for ssl certificate but you can accept it as I have used openssl for demonstration purpose

[Live Link](https://ec2-13-127-133-231.ap-south-1.compute.amazonaws.com)

- Python-Django backend project.
- Django-Rest-Framework for APIs.
- Django-Channels for Web Socket.
- Redis for Channels as backend.
- Postgres SQL as the database.
- Dockerfile, Docker-Compose for containerization.
- Coverage and Test-cases for code coverage.
- Host on AWS ec2, by config Postgres, Docker, Nginx.

## Before starting further please create a python environment first, then install /requirements.txt and add a /.env with required envs as shown in /.env.example

```
(Add python env)
python -m venv <envname>

(Activate python env)
./env/bin/activate  (linux)
.\env\Scripts\activate   (windows)

(Deactivate)
deactivate

(Install all required packages in python env)
pip install -r requirements.txt

(Add /.env with required envs from /.env.example file)

(To run project by uvicorn)
uvicorn config.asgi:application --reload

(To run project by docker)
docker compose up (Windows)
docker-compose up (Linux)

(Run test cases with coverage report)
coverage run manage.py test

(View coverage report)
coverage report/html/xml
```

## APIs Implemented

### Robot

- /api/robot/ (GET) : To fetch List of Robots.

  ```
  Response (200) :
  [
      {
          "id": 2,
          "name": "M11",
          "model_name": "Mv1.1",
          "pose_x": 914.0,
          "pose_y": 487.0
      },
  ]
  ```

- /api/robot/ (POST) : To create a Robot.

  ```
  Payload :
    {
        "name": "Name",
        "model_name": "Model Name",
        "pose_x": 20,
        "pose_y": 30
    }
  Response (201) :
    {
        "id": 123
        "name": "Name",
        "model_name": "Model Name",
        "pose_x": 20,
        "pose_y": 30
    }
  ```

- /api/robot/:robotID/ (GET / PUT / DELETE) : To get, update, delete a robot by id.

  ```
  (GET) Response (200) :
  {
      "id": 123
      "name": "Name",
      "model_name": "Model Name",
      "pose_x": 20,
      "pose_y": 30
  }

  (PUT) Payload :
  {
      "name": "Name",
      "model_name": "Model Name",
      "pose_x": 20,
      "pose_y": 30
  }
  Response (200) :
  {
      "id": 123
      "name": "Name",
      "model_name": "Model Name",
      "pose_x": 20,
      "pose_y": 30
  }

  (DELETE) Response (204)
  ```

### Mission

- /api/mission/ (GET) : To fetch List of Missions.

  ```
  Response (200) :
  [
      {
        "id": 2,
        "name": "Mission Name",
        "description": "Mission description",
        "robot": 15
      },
  ]
  ```

- /api/mission/ (POST) : To create a Mission.

  ```
  Payload :
    {
        "name": "Name",
        "description": "Description",
        "robot": 3
    }
  Response (201) :
    {
        "id": 29,
        "name": "Name",
        "description": "Description",
        "robot": 3
    }
  ```

- /api/mission/:missionID/ (GET / PUT / DELETE) : To get, update, delete a mission by id.

  ```
  (GET) Response (200) :
  {
    "id": 3,
    "robot": {
        "id": 2,
        "name": "Robot name",
        "model_name": "Robot model",
        "pose_x": 914.0,
        "pose_y": 487.0
    },
    "name": "Mission Name",
    "description": "Mission description"
  }

  (PUT) Payload :
  {
        "name": "Name",
        "description": "Description",
        "robot": 3
  }
  Response (200) :
  {
        "id": 29,
        "name": "Name",
        "description": "Description",
        "robot": 3
  }

  (DELETE) Response (204)
  ```

### Web Socket

- /api/ws/movement/:robotID/ : To save the movement of robot on screen by recording x and y axis coordinates.

  ```
  On connection success we will get robot current details.
  {
  "name": "Robot name",
  "model_name": "model name",
  "pose_x": 914.0,
  "pose_y": 487.0
  }

  We will send as json of x and y coordinates during robot movement to save them for robot in db.

  Payload:
  {
  "pose_x": 23,
  "pose_y": 65
  }

  Response :
  {
  "status": true / false,
  "message": "coordinates_saved / invalid_data"
  }

  ```

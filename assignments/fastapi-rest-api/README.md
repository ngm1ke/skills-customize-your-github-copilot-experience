# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small task-tracker REST API with FastAPI. Practice defining HTTP endpoints, handling path and request-body data, and returning appropriate status codes.

## 📝 Tasks

### 🛠️ Create GET Endpoints

#### Description
Use the provided starter code to let clients retrieve all tasks or retrieve one task by its ID. Install the dependencies with `python -m pip install fastapi uvicorn`, then run the app with `uvicorn starter-code:app --reload`. Open `http://127.0.0.1:8000/docs` to try your endpoints.

#### Requirements
Completed program should:

- Return the full task list from `GET /tasks` as JSON.
- Return the matching task from `GET /tasks/{task_id}` as JSON.
- Return an HTTP 404 response when the requested task ID does not exist.

### 🛠️ Add a Task-Creation Endpoint

#### Description
Add an endpoint that accepts a new task in the request body and adds it to the in-memory task list.

#### Requirements
Completed program should:

- Define a request model that requires a task title.
- Create a task through `POST /tasks`, assigning it a unique ID and setting `completed` to `false`.
- Return the created task with HTTP status code 201.
- Make the new task available in subsequent requests to `GET /tasks`.

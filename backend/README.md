# API Documentation

## Chatroom Endpoints

### `POST /api/chatroom/create/<str:room_name>/`

- **Description**: Creates a new chat room with the specified name.
- **Request Body**
    - None
- **Response**
  - **200 OK**: Room created successfully.
  - **400 Bad Request**: Room name is required.
  - **Example**
    ```json
    {
        "status": "Room created"
    }
    ```

### `POST /api/chatroom/newuser/<str:user_name>/`

- **Description**: Registers a new user with the specified name.
- **Request Body**
    - None
- **Response**
  - **200 OK**: User created successfully.
  - **400 Bad Request**: User already exists.
  - **Example**
    ```json
    {
        "status": "User created", 
        "uuid": "UUID"
    }
    ```


### `POST /api/chatroom/send/<str:room_name>/`

- **Description**: Sends a message to the specified chat room.
- **Request Body**:
  - **name**: The name of the sender.
  - **message**: The content of the message.
  - **Example**
    ```json
    {
        "name": "chueat",
        "message": "Hello, world!"
    }
    ```
- **Response**:
  - **200 OK**: Message sent successfully.
  - **400 Bad Request**: Invalid user or room.
  - **Example**
    ```json
    {
        "status": "Message sent"
    }
    ```

### `GET /api/chatroom/messages/<str:room_name>/`

- **Description**: Retrieves all messages from the specified chat room.
- **Request Body**:
  - None
- **Response**:
  - **200 OK**: Returns a list of messages.
  - **404 Not Found**: Room not found.
  - **Example**
    ```json
    {
    "messages": [
            {
                "sender_name": "test_user2",
                "content": "Hello, world!",
                "time": "2024-10-14T04:51:38.883Z"
            },
            {
                "sender_name": "test_user2",
                "content": "hihihhii!",
                "time": "2024-10-14T04:54:51.691Z"
            },
            {
                "sender_name": "chueat",
                "content": "hihihhii!",
                "time": "2024-10-14T04:59:14.040Z"
            },
            {
                "sender_name": "chueat",
                "content": "Hello!",
                "time": "2024-10-14T04:59:22.769Z"
            }
        ]
    }
    ```

### `GET /api/chatroom/messages/<str:room_name>/<str:user_name>/`

- **Description**: Retrieves messages sent by a specific user in the specified chat room.
- **Request Body**:
  - None
- **Response**
  - **200 OK**: Returns a list of messages.
  - **404 Not Found**: Room not found.
  - **Example**
    ```json
    {
    "messages": [
            {
                "content": "hihihhii!",
                "time": "2024-10-14T04:59:14.040Z"
            },
            {
                "content": "Hello!",
                "time": "2024-10-14T04:59:22.769Z"
            }
        ]
    }
    ```

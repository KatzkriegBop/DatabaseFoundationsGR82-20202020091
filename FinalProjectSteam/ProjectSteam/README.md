# Project SteamApp - A RESTFUL API using MySQL databases 

## Overview  
This project implements a **Steam-like digital game distribution platform** with a structured relational database and a RESTful API. The system efficiently manages users, games, friendships, and game libraries.  

## Technologies Used  
- **FastAPI** – High-performance web framework for building APIs  
- **MySQL** – Relational database management system  
- **Docker & Docker Compose** – Containerized deployment  

## Features  
- **User Management** – Create, update, and delete users  
- **Game Library** – Manage game collections per user  
- **Friend System** – Add and remove friends  
- **RESTful API** – CRUD operations for all entities  

## Setup & Installation  
### 1. Clone the repository  
```sh
git clone https://github.com/KatzkriegBop/DatabaseFoundationsGR82-20202020091.git
cd FinalProjectSteam/ProjectSteam
```
### Run with Docker
```sh
docker-compose up --build
```

## API Endpoints  

### User Management  
| Method  | Endpoint | Description |
|---------|---------|-------------|
| `POST`  | `/user/create` | Create a new user |
| `PUT`   | `/user/update/{id_}` | Update user details |
| `DELETE`| `/user/delete/{id_}` | Remove a user |
| `GET`   | `/user/get_by_id/{id_}` | Retrieve user info by ID |
| `GET`   | `/user/get_all` | Get all users |
| `GET`   | `/user/get_by_name/{name}` | Get user by name |
| `GET`   | `/user/get_by_email/{email}` | Get user by email |
| `GET`   | `/user/get_by_country/{country}` | Get user by country |
| `GET`   | `/user/get_by_phone/{phone}` | Get user by phone |

### Game Management  
| Method  | Endpoint | Description |
|---------|---------|-------------|
| `POST`  | `/game/create` | Create a new game |
| `PUT`   | `/game/update/{id_}` | Update game details |
| `DELETE`| `/game/delete/{id_}` | Remove a game |
| `GET`   | `/game/get_by_id/{id_}` | Fetch game details by ID |
| `GET`   | `/game/get_all` | Get all games |
| `GET`   | `/game/get_by_genre` | Get games by genre |
| `GET`   | `/game/get_by_developer` | Get games by developer |
| `GET`   | `/game/get_by_name` | Get games by name |
| `GET`   | `/game/get_genres` | Get all available genres |

### Friend System  
| Method  | Endpoint | Description |
|---------|---------|-------------|
| `POST`  | `/friend/create` | Add a friend |
| `DELETE`| `/friend/delete/{user_id}/{friend_id}` | Remove a friend |
| `GET`   | `/friend/get_all` | Get all friendships |
| `GET`   | `/friend/get_by_user_id/{user_id}` | Get friends by user ID |
| `GET`   | `/friend/is_friend/{user_id}/{friend_id}` | Check if users are friends |

### Library Management  
| Method  | Endpoint | Description |
|---------|---------|-------------|
| `POST`  | `/library/create` | Add a game to a user's library |
| `DELETE`| `/library/delete/{user_id}/{game_id}` | Remove a game from a user's library |
| `GET`   | `/library/get_all` | Get all game libraries |
| `GET`   | `/library/get_games_by_user_id/{user_id}` | Get games by user ID |
| `GET`   | `/library/has_game/{game_id}` | Check if a game exists in any library |
| `GET`   | `/library/get_user_by_games_id/{game_id}` | Get users who own a specific game |

## Authors  
Developed by **Juan Pablo Borja Espitia**.  
For inquiries or contributions, contact: **jpborjae1337@gmail.com**  
---


---




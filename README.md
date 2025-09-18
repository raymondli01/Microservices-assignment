# Flask Microservices Assignment

Two minimal Flask services demonstrating a microservices architecture:

- **User Service** (`user_service.py`) on port **5001**
- **Order Service** (`order_service.py`) on port **5002** which calls the User Service

**Screenshots:**
  ![API call success](screenshots/Screenshot%202025-09-18%20125946.png)
  ![API call success](screenshots/Screenshot%202025-09-18%20130157.png)
  ![API call success](screenshots/Screenshot%202025-09-18%20130344.png)
  
## Quickstart (Windows, PowerShell)

```powershell
# 1) Ensure Python 3.10+ and Git are installed
python --version
git --version

# 2) Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Run the services in two terminals
# Terminal A
python user_service.py

# Terminal B
python order_service.py
```

## Test Requests

> These work in PowerShell (Windows 10+ has `curl`).

```powershell
# Get default users
curl http://localhost:5001/users/1
curl http://localhost:5001/users/2

# Create a user
curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"Carol\", \"email\": \"carol@example.com\"}" http://localhost:5001/users

# Get an order (includes embedded user details)
curl http://localhost:5002/orders/1

# Create an order
curl -X POST -H "Content-Type: application/json" -d "{\"user_id\": 1, \"product\": \"Tablet\"}" http://localhost:5002/orders
```

## Repo Setup & Push to GitHub

```powershell
# Initialize a new repo
git init
git add .
git commit -m "Initial commit: Flask microservices assignment"

# Create a GitHub repo named: flask-microservices-assignment
# Then set the remote and push (replace YOUR-USERNAME)
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/flask-microservices-assignment.git
git push -u origin main
```


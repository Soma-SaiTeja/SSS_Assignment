# SSS_Assignment
create a simple RESTful API using Node.js and Express.

Step-by-Step Guide to Create the Flask API
This guide walks through setting up your Flask API from scratch, including: ✅ Virtual Environment Setup
✅ Installing Dependencies
✅ Creating MySQL Database
✅ Implementing Asynchronous File Handling
✅ Rate Limiting (100 requests per 15 min)
✅ JWT Authentication & Protection
✅ Robust Error Handling
✅ CRUD Operations
✅ Finalizing README.md for Submission

📌 Step 1: Create Project Directory & Virtual Environment
1️⃣ Open CMD & Navigate to Your Preferred Directory
bash
Copy
Edit
cd C:\Users\somas
mkdir sss_assignment
cd sss_assignment
2️⃣ Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
✅ Your CMD should now show (venv), meaning the virtual environment is activated.

📌 Step 2: Install Dependencies
Run the following command inside the virtual environment:

bash
Copy
Edit
pip install flask pymysql flask-cors flask-jwt-extended flask-limiter jsonschema
✅ Now Flask and all required dependencies are installed!

📌 Step 3: Setup MySQL Database
1️⃣ Log into MySQL
cmd
mysql -u root -p
2️⃣ Create Database & Table
sql
cmd
CREATE DATABASE sss_db;
USE sss_db;

CREATE TABLE items (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
✅ Now MySQL is ready!

📌 Step 4: Create app.py (Flask API)
📜 Create a new file in the project directory:

cmd
notepad app.py

And now run the attached app.py

Step 5: Start the Flask Server
bash
Copy
Edit
python app.py
✅ Expected Output:
cmd

Running on http://127.0.0.1:5000/
📌 Step 6: Create README.md
📜 Create README.md

cmd
notepad README.md  # Windows
# nano README.md  # Mac/Linux
📌 Paste This:

cmd
# 🏆 Flask REST API with MySQL

## 🚀 Features
✅ Asynchronous File Handling (`logs.json`)  
✅ Rate Limiting (100 Requests/15 min)  
✅ JWT Authentication & Protection  
✅ Robust Error Handling  
✅ CRUD Operations  
✅ MySQL Database Connected  

## 📌 Installation & Setup
```bash
git clone <repo_url>
cd sss_assignment
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python app.py
📝 API Endpoints
Method	Endpoint	Description
POST	/login	Get JWT Token
POST	/api/items	Create an Item
GET	/api/items	Get All Items
GET	/api/items/<id>	Get One Item
PUT	/api/items/<id>	Update Item
DELETE	/api/items/<id>	Delete Item

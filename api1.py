
import requests
import mysql.connector

# Configuration constants
API_URL = "https://jsonplaceholder.typicode.com/users"
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "api_demo"
}
conn = None
cursor = None
print("Fetching Data From API...\n")
try:
    response = requests.get(API_URL, timeout=5)
    response.raise_for_status()  
    data = response.json()
    print("API Request Successful\n")
    
except requests.exceptions.RequestException as e:
    print(f"API Error occurred: {e}")
    data = None
if data is not None:
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        print("Connected To MySQL\n")
        
        inserted_count = 0
        
        for user in data:
            user_id = user['id']
            name = user['name']
            username = user['username']
            email = user['email']
            check_query = "select id from users where id = %s"
            cursor.execute(check_query, (user_id,))
            result = cursor.fetchone()
            
            if result:
                print(f"User ID {user_id} Already Exists. Skipping...")
            else:
                insert_query = "insert into users (id, name, username, email) VALUES (%s, %s, %s, %s)"
                print(f"Inserting User:\n{user_id} {name}\n")
                
                cursor.execute(insert_query, (user_id, name, username, email))
                inserted_count += 1
        conn.commit()
        print(f"{inserted_count} Users Inserted Successfully\n")
        
    except mysql.connector.Error as e: 
        print(f"Database Error occurred: {e}")
        
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
            print("Database Connection Closed")
else:
    print("Process halted due to an API connectivity failure.")
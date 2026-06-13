# api-to-mysql-data-migration
# API to MySQL Data Migration System (PDBC)

A robust, enterprise-ready Python data migration application that orchestrates data extraction from a public REST API and reliably maps it into a relational MySQL database server using Python Database Connectivity (PDBC).

---

## 🛠️ Tools & Technologies Used

* **VS Code** – The development environment used for writing, executing, and debugging the script.
* **Python 3** – The primary runtime engine executing network requests, data isolation, and database connection pools.
* **MySQL Server & Workbench** – Relational database backend used to maintain persistent data arrays.
* **JSONPlaceholder API** – The external testing endpoint used to simulate an upstream JSON stream extraction source.

---

## Installed Packages & Modules

To manage internet-to-database communication loops, the system relies on these external packages:

```bash
pip install requests mysql-connector-python

Script Architecture Modules:
import requests – Used to dispatch synchronous REST endpoint queries with network safe thresholds (timeout=5).

import mysql.connector – Provides the driver communication link required to log into the MySQL server and commit operations safely.

 Key Functional Architectures
1. Robust Fault-Tolerant Exception Handling
API Shielding: Implements an explicit try-except block watching for requests.exceptions.RequestException. This gracefully intercepts network failures, timeouts, bad URLs, or connection dropping without crashing the system host.

Database Protection: Wrapped heavily inside a mysql.connector.Error handler block to catch downstream server crashes, invalid authentication schemes, or execution syntax slipups.

Guaranteed Resource Cleanup: Built using strict finally: block routing, ensuring that no matter if transactions succeed or fail, the database cursor and open engine connections are automatically closed (cursor.close(), conn.close()) preventing socket exhaustion.

2. Parameterized Queries (Anti-SQL Injection)
The system avoids vulnerable string formatting and instead uses modern parameterized SQL arrays:

SQL
INSERT INTO users (id, name, username, email) VALUES (%s, %s, %s, %s)

3. Production-Ready Duplication Prevention 
Before blindly running insertions, the tool queries the database table indexes for existing user IDs. If a key crash is imminent, it skips safely with a log flag, ensuring total transaction safety and id isolation.

How the Application Operates
Plaintext
Start ➔ Call API ➔ Parse JSON ➔ Connect to DB ➔ Duplicate ID Check ➔ Insert ➔ Commit ➔ Cleanup
Extraction: A network connection is built to harvest the https://jsonplaceholder.typicode.com/users entity profile array.

Parsing: The engine transforms raw response blocks using Python objects via response.json().

Loop Verification: The software iterates down the object stack isolating individual values for id, name, username, and email.

Validation & Storage: The backend verifies key uniqueness, securely routes variables into standard parameters, saves data permanently using conn.commit(), and safely unlinks server channels.

Repository Map
migration_app.py – Core backend script containing execution modules, network targets, and full error handlers.

api_demo.sql – Structure schema file detailing the database rules and properties setup for the users table.

Project Engineered By: Sidra Jabeen

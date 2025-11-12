✅ Cricket Player Management System — Python + MySQL

A console-based application to manage cricket player data using Python, OOP design, and MySQL database connectivity.

✅ Features

✔ Add new players with details (name, role, batting/bowling style, matches, runs, wickets)
✔ View all stored players from the database
✔ Update player statistics (runs & wickets)
✔ Delete a player by ID
✔ Clean layered architecture (Controller → Service → DAO → DB)

✅ Tech Stack

Language: Python

Database: MySQL

Library: PyMySQL

Concepts Used: OOP, Modules, CRUD operations, SQL queries, database connection handling

✅ Folder Structure

main.py
model/
  player.py
service/
  playerservice.py
  playerservice_impl.py
dao/
  playerdao.py
  playerdao_impl.py
util/
  db_connection.py

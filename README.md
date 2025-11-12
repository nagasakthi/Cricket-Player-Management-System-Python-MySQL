🏏 Cricket Player Management System — Python + MySQL

A console-based application for managing cricket players, using Python OOP and MySQL database connectivity.

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

✅ How to Run

1.Install dependencies:

pip install pymysql

2.Create MySQL database & table:

CREATE DATABASE cricket;
USE cricket;

CREATE TABLE cricketplayers (
    playerid INT AUTO_INCREMENT PRIMARY KEY,
    PlayerName VARCHAR(100),
    Country VARCHAR(50),
    Roles VARCHAR(50),
    BattingStyle VARCHAR(50),
    BowlingStyle VARCHAR(50),
    MatchesPlayed INT,
    Runs INT,
    Wickets INT
);

3.Run the program:

python main.py

✅ Skills Demonstrated

✔ Python + SQL integration
✔ OOP & Modular Design
✔ Exception Handling & CRUD operations

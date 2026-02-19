# CodeAlpha_task

# Python Programming Tasks - Common  Projects

## 📌 Overview

This collection includes several simple Python programs created to improve basic programming skills.
Each task focuses on understanding how logic works in real programs using user interaction and decision-making.

All programs are terminal-based and do not require any external modules (except the built-in random module for one task).

## The tasks included are:

Task 1: Hangman Game

Task 2: Stock Portfolio Calculator

Task 4: Simple Chatbot

## 📁 Folder Structure

CodeAlpha_task/
│
├── CodeAlpha_hangman.py
├── CodeAlpha_stock_tracker.py
├── CodeAlpha_chatbot.py
└── README.md

## 🛠 Requirements

To run this project, you need:

   Python 3 installed

   Any text editor (VS Code / Notepad / IDLE)

   Command Prompt or Terminal

No additional libraries are required.

## ▶ How to Run the Programs

1. Open Command Prompt or Terminal.

2. Go to the project folder using cd command.

3. Run any task file using:

CodeAlpha__hangman.py

CodeAlpha_stock_tracker.py

CodeAlpha_chatbot.py

Each program will start in the terminal window.

# 🧩 Task Details

# ✅ Task 1: Hangman Game

## Description:

This is a word guessing game where the computer randomly selects a word and the player tries to guess it one letter at a time.

The player has limited wrong attempts. If they guess all letters correctly, they win. Otherwise, they lose.

## Features:

Word is selected randomly from a small list

Shows hidden word using underscores

Tracks guessed letters

Limits incorrect guesses

Displays win or lose result

## Concepts Used:

random.choice() to select a word

for loop to update hidden letters

in keyword for checking letters

continue statement to skip repeated guesses

List operations (storing guessed letters)

String comparison

# ✅ Task 2: Stock Portfolio Tracker

## Description:

This program helps users calculate their total stock investment.
Stock prices are already stored inside the program. The user enters the stock name and quantity, and the program calculates the total amount invested.

## Features:

Uses fixed stock prices

Accepts multiple stock entries

Calculates total value

Displays summary at the end

Prevents invalid stock entries

## Concepts Used:

Dictionary methods (.items())

while True loop for continuous input

Type conversion (int())

Accumulator variable for total calculation

Basic validation using if stock in dictionary

Simple formatted printing

# ✅ Task 4: Basic Chatbot

## Description:

This chatbot responds to specific messages typed by the user.
It checks the input and replies with a fixed answer.
The chat continues until the user types an exit command.

## Features:

Responds to greetings

Gives simple conversational replies

Stops when user types "bye"

Works continuously inside a loop

Example Inputs:

hello

how are you

bye

## Concepts Used:

Function definition for response handling

Boolean condition checking

break keyword to stop program

String normalization using .strip()

Infinite loop pattern

Console-based interaction

## 🎯 Purpose of This Project

This project helps students:

Strengthen understanding of Python basics

Improve problem-solving skills

Learn how different concepts work together

Practice writing structured and readable code

Prepare for internship assignments

Gain confidence in building small real-world programs

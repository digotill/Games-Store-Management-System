# Coursework: Games Store Management System

**Module:** 25COA122 - Introduction to Programming and Databases

**Assessment Weight:** 50% of the module assessment

**Submission Deadline:** 11am on Wednesday 14th January 2026

---

## Project Overview

Develop a **Board/Video Games Management System** for a new Gaming Store. This system will manage game rentals and bookings for face-to-face group sessions, all based on customer subscription status.

The system will enable a store manager to:
* Maintain a database of all games (board and video).
* Check game availability and manage rentals.
* Manage a booking system for in-store game sessions (2pm-6pm or 6pm-10pm).
* Collect and process customer feedback upon game return.
* Identify and suggest unpopular games for inventory pruning.

---

## Key Features and Functionality

| Feature | Description | Technical Requirement |
| :--- | :--- | :--- |
| **Game Inventory** | Store and manage details for a minimum of 10 board games and 10 video games. | **Files 1 & 2** (`Board_Game_Info.txt`, `Video_Game_Info.txt`) |
| **Search Function** | Search for games by type, title, and genre, returning full game records and availability. | **Python Cell:** `gameSearch` |
| **Game Rental** | Rent a game to a subscribed customer after validating their 4-letter ID using `subscriptionManager.pyc`. | **Python Cell:** `gameRent`, **File 3** (`Rental.txt`) |
| **Session Booking** | Allow subscribers to book slots for up to 50 persons. Subscribers can bring up to 3 guests. | **Python Cell:** `menu`, **File 4** (`Booking.txt`) |
| **Game Return & Feedback** | Update records upon return and collect star rating/comments using `feedbackManager.pyc`. | **Python Cell:** `gameReturn` |
| **Inventory Pruning** | Suggest unpopular games for removal based on rental frequency. Must include **visualisations**. | **Python Cell:** `inventoryPruning` |
| **User Interface** | Main application menu built using **IPyWidgets** in a single-window GUI. | **Python Cell:** `menu` |

---

## Program Structure and Submission

The project **must** be developed in **Google Colab** and submitted as an `.ipynb` notebook.

### Required Python Cells (Modules)

You MUST label the menu cells as follows:
* `database`: Common functions for data file interaction.
* `gameSearch`: Handles searching games.
* `gameRent`: Handles the rental process.
* `gameReturn`: Handles game return and feedback collection.
* `inventoryPruning`: Suggests unpopular games for removal (with visualisations).
* `menu`: The main cell providing the user interface using **IPyWidgets**.

### Required Files

The submission requires a zip file containing the `.ipynb` notebook and all files below in the same folder:

| File Name | Type | Minimum Records | Notes |
| :--- | :--- | :--- | :--- |
| `Board_Game_Info.txt` | Data File | 10 | Stores board game details. |
| `Video_Game_Info.txt` | Data File | 10 | Stores video game details. |
| `Rental.txt` | Data File | 50 | Rental history and current rented status. |
| `Booking.txt` | Data File | 50 | Session booking history. |
| `Game_Feedback.txt` | Data File | 0 | Populated by the program (`gameReturn`). |
| `subscriptionManager.pyc` | Provided Module | N/A | Must be included. |
| `feedbackManager.pyc` | Provided Module | N/A | Must be included. |

---

## Coding Restrictions

* Your code must **NOT** include any **Class type definition**.
* Your code must **NOT** have any **SQL statements**.
* Your code must **NOT** have any **nested function declaration**.
* You must use **ONLY** standard Python libraries and **MatPlotLib**.
* You must use **ONLY iPyWidgets** for your GUI.

---

## GenAI Tool Usage Statement

GenAI tools are permitted in an **assistive role** only for:
1.  Finding literature sources.
2.  Help writing code.
3.  Text proofreading.

**Inappropriate usage** includes: Text/code generation, or interpretation/discussion of results. You are responsible for fact checking any AI generated material.
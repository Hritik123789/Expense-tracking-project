## Expense Management System

A web-based application to track daily expenses, analyze spending patterns, and manage expense records using FastAPI (backend), MySQL (database), and Streamlit (frontend).

---

## Project Structure

```
expense tracking project 2/
│
├── backend/
│   ├── db_helper.py         # Database CRUD operations
│   ├── server.py            # FastAPI server with API endpoints
│   └── __pycache__/
│
├── frontend/
│   ├── app.py               # Streamlit main app
│   ├── add_update_ui.py     # UI for adding/updating expenses
│   ├── analytics_ui.py      # UI for analytics tab
│   └── __pycache__/
│
├── tests/
│   ├── conftest.py          # Test configuration
│   ├── backend/
│   │   └── test_db_helper.py # Backend unit tests
│   └── frontend/
│
└── README.md                # Project documentation
```

---

## Setup Instructions

1. **Install Dependencies**
   - Create a virtual environment and activate it.
   - Install required Python packages:
     ```
     pip install fastapi uvicorn mysql-connector-python streamlit
     ```

2. **Setup MySQL Database**
   - Mysql database is provided use in it in MySqlWorkBench
     ```

4. **Run Backend (FastAPI)**
   - Navigate to the `backend` folder and start the server:
     ```
     (Run this in Gitbash)
     uvicorn server:app --reload --port 8000
     ```

5. **Run Frontend (Streamlit)**
   - Navigate to the `frontend` folder and start the app:
     ```
     (Run this in terminal VSCode)
     streamlit run app.py
     ```

6. **Run Tests**
   - From the project root, run:
     ```
     pytest
     ```

7. **Usage**
   - Open your browser and go to `http://localhost:8501` to use the Expense



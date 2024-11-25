# Expense Management System

This project is an **Expense Management System** that consists of a **Streamlit frontend application** and a **FastAPI backend server**. The system allows users to track, add, update, delete, and analyze their expenses.

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.

## Backend (FastAPI)

### Installation & Setup

1. **Install Backend Dependencies**:
   - Create a virtual environment and activate it.
   - Install required libraries by running:
     ```bash
     pip install -r backend/requirements.txt
     ```

2. **Run the Backend**:
   - Navigate to the `backend/` directory.
   - Run the FastAPI server using the following command:
     ```bash
     uvicorn main:app --reload
     ```
   - The backend API will be running at `http://localhost:8000`.

### API Endpoints

- **GET `/expenses/{expense_date}`**: Fetches all expenses for a specific date.
  - Example: `GET /expenses/2024-08-01`
  - Response: List of expenses for the provided date.

- **POST `/expenses/{expense_date}`**: Adds or updates expenses for a specific date.
  - Payload: A list of expenses to be added or updated.
  - Example Payload:
    ```json
    [
      {
        "amount": 100,
        "category": "Food",
        "notes": "Lunch"
      }
    ]
    ```

- **POST `/analytics/`**: Fetches analytics for expenses within a specific date range.
  - Payload:
    ```json
    {
      "start_date": "2024-08-01",
      "end_date": "2024-08-15"
    }
    ```
  - Response: Breakdown of expenses by category along with their totals and percentages.

## Frontend (Streamlit)

### Installation & Setup

1. **Install Frontend Dependencies**:
   - Create a virtual environment and activate it.
   - Install required libraries by running:
     ```bash
     pip install -r frontend/requirements.txt
     ```

2. **Run the Frontend**:
   - Navigate to the `frontend/` directory.
   - Run the Streamlit application with:
     ```bash
     streamlit run main.py
     ```
   - The frontend will be accessible at `http://localhost:8501`.

### Features

- **Analytics Tab**: Allows the user to fetch an expense summary and visualizes the data in a bar chart with categories sorted by their percentage of total expenses.
- **Add/Update Expenses Tab**: Provides a form to add or update expenses for a given date. The user can input the amount, category, and notes for each expense.

## Testing

### Backend Tests

The backend includes tests to verify the functionality of the database operations and API endpoints.

To run the backend tests, navigate to the `tests/` directory and use `pytest`:
```bash
pytest backend/tests/
.
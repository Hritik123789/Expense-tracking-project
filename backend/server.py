from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from datetime import date, datetime
import db_helper
from typing import List
from pydantic import BaseModel

app = FastAPI()


class Expense(BaseModel):
    amount: float
    category: str
    notes: str


class DateRange(BaseModel):
    start_date: date
    end_date: date

@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: str):
    # Parse string to date
    try:
        expense_date_obj = datetime.strptime(expense_date, "%Y-%m-%d").date()
    except ValueError:
        # Return empty list as JSON
        return JSONResponse(content=[])
    expenses = db_helper.fetch_expenses_for_date(str(expense_date_obj))
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expenses(expense_date: str, expenses: List[Expense]):
    try:
        expense_date_obj = datetime.strptime(expense_date, "%Y-%m-%d").date()
    except ValueError:
        return {"message": "Invalid date format"}
    db_helper.delete_expenses_for_date(str(expense_date_obj))
    for expense in expenses:
        db_helper.insert_expense(str(expense_date_obj), expense.amount, expense.category, expense.notes)
    return {"message": "Expenses Updated successfully"}

@app.post("/analytics/")
def get_analytics(date_range:DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="No data found for the given date range")
    
    total=sum([row['total']for row in data])
    breakdown={}
    for row in data:
        percentage=(row['total']/total)*100 if total !=0 else 0
        breakdown[row['category']]={
            "total": row['total'],
            "percentage": percentage
        }
    return breakdown


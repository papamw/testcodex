# testcodex

This project now includes a minimal [FastAPI](https://fastapi.tiangolo.com/) application that can be used as the foundation for future features.

## Getting started

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Open <http://127.0.0.1:8000/> in your browser to see the "Hello, World!" response.

You can now extend the `app/main.py` module with additional routes, models, and business logic as needed.

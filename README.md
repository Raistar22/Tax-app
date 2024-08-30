# Income Tax Calculator Application

## Overview

This project is a full-stack Income Tax Calculator application. It allows users to create and manage tax plans based on their income, applicable deductions, and Indian tax slabs for a selected year. The application is built using Django REST Framework for the backend and React for the frontend.

## Features

- Create and manage multiple tax plans.
- Fetch tax slabs for different years.
- Calculate tax based on user inputs and selected year's slabs.
- View and delete saved tax plans.
- User authentication (optional for a more complete setup).
- Responsive UI with Material-UI.

## Technologies

- Frontend: React, Material-UI
- Backend:Django REST Framework
- Database: PostgreSQL

## Setup

### Prerequisites

- Python 3.x
- Node.js and npm (or yarn)
- PostgreSQL

### Backend Setup

1. Navigate to the Backend Directory:

    ```bash
    cd backend
    ```

2. Create a Virtual Environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. Install Backend Dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure the Database:

    Update the `DATABASES` setting in `backend/settings.py` to match your PostgreSQL configuration.

5. Apply Migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a Superuser (optional):

    ```bash
    python manage.py createsuperuser
    ```

7. Start the Backend Server:

    ```bash
    python manage.py runserver
    ```

   The backend server will be running at `http://localhost:3000`.

### Frontend Setup

1. Navigate to the Frontend Directory:

    ```bash
    cd frontend
    ```

2. Install Frontend Dependencies:

    ```bash
    npm install
    ```

   or, if you are using yarn:

    ```bash
    yarn install
    ```

3. Start the Frontend Server:

    ```bash
    npm start
    ```

   or, if you are using yarn:

    ```bash
    yarn start
    ```

   The frontend server will be running at `http://localhost:3000`.

## API Endpoints

- GET /api/taxslabs/: List all tax slabs.
- GET /api/taxslabs/{id}/: Retrieve a specific tax slab.
- GET /api/deductions/**: List all deductions.
- GET /api/deductions/{id}/**: Retrieve a specific deduction.
- GET /api/taxplans/: List all tax plans.
- POST /api/taxplans/: Create a new tax plan.
- GET /api/taxplans/{id}/: Retrieve a specific tax plan.
- PUT /api/taxplans/{id}/: Update a specific tax plan.
- PATCH /api/taxplans/{id}/: Partially update a specific tax plan.
- DELETE /api/taxplans/{id}/: Delete a specific tax plan.

## Testing

You can test the API endpoints using tools like Postman or cURL.

Example Postman Requests:

- GET /api/taxslabs/?year=2024: Fetch tax slabs for the year 2024.
- POST /api/taxplans/: Create a new tax plan (requires authentication).
- GET /api/taxplans/: List all tax plans for the authenticated user.
- DELETE /api/taxplans/{id}/: Delete a specific tax plan (requires authentication).

## Contributing

Feel free to open issues or submit pull requests to improve the project. Please ensure that you follow the coding standards and include tests for any new features or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This `README.md` provides a comprehensive guide for setting up and running both the backend and frontend servers. Adjust the instructions as needed to fit your specific project setup and requirements.

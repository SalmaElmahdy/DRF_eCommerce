# DRF_eCommerce

Django REST API with Authentication, CRUD Operations, and Swagger Documentation

## Project Description

This project is a Django REST Framework-based API that provides authentication functionality, CRUD operations for expenses, and comprehensive Swagger documentation. It is designed to serve as a robust backend, allowing users to register, sign in, verify their accounts, manage expenses, and access detailed API documentation.

The project utilizes Django REST Framework's GenericAPIView to handle user registration, sign-in, and account verification. It also employs generics such as RetrieveUpdateDestroyAPIView and ListCreateAPIView to facilitate CRUD operations for expenses. Authentication is implemented using `rest_framework_simplejwt` tokens, providing secure access to API endpoints.

Swagger documentation is integrated into the project, offering a user-friendly interface to explore and test API endpoints. The settings file is configured to use bearer token authentication in Swagger for seamless testing and interaction.

Additionally, a custom permission named `IsOwner` is implemented to ensure that only the user who owns an expense object can modify it. This permission provides an added layer of security and control over expense management.

To enhance the user experience, pagination is implemented using `PageNumberPagination`. This allows the expenses to be displayed in a paginated manner, improving performance and usability.

## Technologies Used

- Django REST Framework
- Django
- Python
- SQL lite
- `rest_framework_simplejwt` for token-based authentication
- Swagger for API documentation

## Installation and Usage

To run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Navigate to the project directory: `cd your-repo`
3. Create a virtual environment: `python -m venv env`
4. Activate the virtual environment:
   - On Windows: `.\env\Scripts\activate`
   - On macOS/Linux: `source env/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Set up the database:
   - Update the database configuration in `settings.py`
   - Run migrations: `python manage.py migrate`
7. Start the development server: `python manage.py runserver`

You can now access the API at `http://localhost:8000/` and explore the available endpoints using the Swagger documentation.

## API Documentation

The API documentation is available through the Swagger interface. To access it, start the development server and navigate to `http://localhost:8000/swagger/`. You can authenticate using the provided registration and sign-in endpoints to obtain a token for testing other authenticated endpoints.

The documentation provides detailed information about each API endpoint, including request/response formats, authentication requirements, and examples of API requests and responses.

## Project Status

This project is actively maintained and open to contributions. It provides a solid foundation for building Django REST API applications with authentication, CRUD operations, and comprehensive Swagger documentation.

Feel free to explore the code, try out the API, and provide feedback or suggestions for improvement. Contributions, bug reports, and feature requests are highly appreciated.

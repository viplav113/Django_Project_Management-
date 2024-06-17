# Django Project with Clients and Projects Management

This project is a Django-based application that manages clients and projects. It allows users to create clients and assign projects to them, and users can see the projects assigned to them.

## Setup Instructions

### Prerequisites

- Python 3.x
- PostgreSQL
- pgAdmin4

### Installation Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/viplav113/Django_Project_Management-.git
    cd your-repo-name
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up PostgreSQL:**

    - Install PostgreSQL and PgAdmin 4.
    - Create a database and user with the required permissions.

4. **Update `settings.py` with your database information:**

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

6. **Run database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

### API Endpoints

- **Clients**
  - List of all clients: `/api/clients/`
  - Create a new client: `/api/clients/`
  - Retrieve client info: `/api/clients/:id`
  - Update client info: `/api/clients/:id`
  - Delete client info: `/api/clients/:id`

- **Projects**
  - Create a new project: `/api/projects/`
  - Delete a project: `/api/projects/:id`

### Example Usage

1. **Create a Client:**

    - Send a `POST` request to `/api/clients/` with the client name.
      
      ![Screenshot 2024-06-16 222230](https://github.com/viplav113/Django_Project_Management-/assets/83233060/59273438-bee6-46e1-96a6-39197c51dcca)

    - After sending post request 
      ![Screenshot 2024-06-16 222419](https://github.com/viplav113/Django_Project_Management-/assets/83233060/c9a5778c-a957-48b4-8914-7217a28d37d9)


2. **Create a Project and Assign Users:**

    - Send a `POST` request to `/api/projects/` with the project name, client ID, and list of user IDs.
      ![Screenshot 2024-06-16 222756](https://github.com/viplav113/Django_Project_Management-/assets/83233060/5739019a-3ce4-4f73-a948-f9ddbae6db5f)

    - After creating and assigning the project
    1.  ![Screenshot 2024-06-16 222846](https://github.com/viplav113/Django_Project_Management-/assets/83233060/d7841797-0537-4c1e-840f-23b1e380e15e)

    2. ![Screenshot 2024-06-16 223048](https://github.com/viplav113/Django_Project_Management-/assets/83233060/d3292fd1-48dd-4ffc-9c57-9601f0add850)




3. **Update information of Client:**

    - Send a `GET` request to `/api/clients/`id`.
      ![Screenshot 2024-06-16 222508](https://github.com/viplav113/Django_Project_Management-/assets/83233060/450a8a56-f1c5-422f-bde0-ec4468d99748)

    - Here I have updated client name Nimap to Nimap Soft
      ![Screenshot 2024-06-16 222547](https://github.com/viplav113/Django_Project_Management-/assets/83233060/86a7952d-a345-4d24-a0ff-7b0a66945042)


4. **Delete a Project:**

    - Send a `DELETE` request to `/api/projects/:id`.
      ![Screenshot 2024-06-16 223114](https://github.com/viplav113/Django_Project_Management-/assets/83233060/113c4002-61f7-4a68-a311-c2c07bdc7990)

    - After deleting
      ![Screenshot 2024-06-16 223142](https://github.com/viplav113/Django_Project_Management-/assets/83233060/de79a88d-9cf1-40c0-9f6f-35dac65bd96f)

## Notes

- Ensure you have PostgreSQL running and properly configured in your `settings.py`.
- Use the Django admin panel to manage users.

##

# StudyBud

StudyBud is a collaborative web application designed to help students find and create study groups. Users can create study rooms based on different topics, join existing rooms, and engage in discussions with other participants.

## Features

* **User Authentication:** Users can register for an account, log in, and log out.
* **User Profiles:** Each user has a profile page displaying their created rooms and recent activity. Profiles can be updated.
* **Create & Manage Study Rooms:** Authenticated users can create new study rooms, providing a topic, name, and description. They can also update or delete the rooms they host.
* **Browse & Search:** Users can browse rooms by topic or search for specific rooms, topics, or hosts.
* **Real-time Conversations:** Inside a room, users can post messages and participate in discussions.
* **Recent Activity Feed:** The homepage displays recent messages from all study rooms, keeping users updated on the latest conversations.

## Project Structure

The project is a standard Django application with the following structure:

```
studybud/
├── base/             # Main application
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── studybud/         # Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
├── templates/
├── db.sqlite3
└── manage.py
```

## Setup and Installation

To get the project up and running on your local machine, follow these steps:

**1. Clone the Repository:**

```bash
git clone <repository-url>
cd studybud
```

**2. Create and Activate a Virtual Environment:**

* **For macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
* **For Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

**3. Install Dependencies:**

Install all the required packages using pip:

```bash
pip install -r requirements.txt
```
*(Note: If `requirements.txt` is not present, you will need to install Django manually: `pip install Django`)*

**4. Apply Database Migrations:**

Apply the database migrations to create the necessary tables:

```bash
python manage.py migrate
```

**5. Create a Superuser (Optional):**

To access the Django admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```
You will be prompted to enter a username, email, and password.

**6. Run the Development Server:**

Start the Django development server:

```bash
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`.

## Usage

* Navigate to the homepage to see all available study rooms.
* Use the "Browse Topics" section to filter rooms by a specific topic.
* Use the search bar to find rooms or topics.
* Register for an account or log in to create your own rooms and participate in conversations.
* Click on a room to view the discussion and add your own messages.


# Celestial Explore Blog 🌌



Celestial Explore Blog is a dynamic space-themed blog platform that provides users with the latest space news, engaging articles, and interactive 3D visualizations of our solar system. This project combines educational content with advanced visual technology to help users explore and understand the universe from their own devices.

### 🚀 Key Features

 -  Live Space News  & Updates: Stay informed with the latest discoveries, missions, and celestial events.
- Informative Space Blogs: Access articles covering astrophysics, space technology, planetary science, and more.
- 3D Solar System Visualization: An interactive model showcasing planets, allowing users to explore:
- Relative Distances: See accurate spatial relationships between celestial bodies.
- Sizes: Understand the scale of planets and moons within the solar system.
- Orbital Speeds: Observe how celestial bodies move in real time.
- Inspired by NASA’s “Eyes on the Solar System”: This 3D explorer was built to mimic the immersive experience provided by NASA, offering users a navigable view of the solar system.
##### Optimized Performance:
- Lazy Loading for Assets: Ensures faster load times by loading images and assets only when needed.
- Optimized 3D Rendering: Enhances interactivity with minimal lag, providing a smooth user experience.
- Educational & Engaging: Combines astronomical accuracy with an accessible, interactive visual interface, making it a valuable tool for space enthusiasts and learners alike.


### 💻 Tech Stack

#### Frontend:

HTML5, CSS3, JavaScript for building a responsive and interactive user interface.
Three.js for rendering 3D models of the solar system.
Bootstrap 5 and Sass for styling and creating responsive layouts.
Lazy Loading on images to ensure faster page loads.

#### Backend:

Django (Python) for server-side management, handling requests, and serving content dynamically.
Django REST Framework for building APIs to fetch live news and blog content.
#### Database:

mysql for development and small-scale usage (optionally PostgreSQL for production).
#### Hosting:


### 🛠 Setup Instructions

#### 1. Install Python and Virtual Environment
 - Ensure Python (preferably version 3.8+) is installed:
```bash
python --version 
```
- Install virtualenv to manage a virtual environment for your project:
```bash
pip install virtualenv
```
#### 2. Create and Activate Virtual Environment
- Create a virtual environment:
```bash
python -m venv myenv
```
- Activate the virtual environment:
On macOS/Linux:
```bash
source myenv/bin/activate
```
- On Windows:
```bash
myenv\Scripts\activate
```
#### 3. Install Django and Other Dependencies:

- Install Django and any other dependencies (if known):
```bash
pip install django
```

#### 4.Clone the repository:

```bash
 git clone https://github.com/Mohamedashmar432/celestial-explore-blog
```
- Install requirements:

```bash
pip install requirements.txt
```
#### 5. Set Up Initial Django Project Settings
 - Setting up your database crendentials in .env file in root discovery:

```bash
SECRET_KEY='your-secret-key'
DEBUG=True
DATABASE = 'your-database-host'
DATABASE_NAME='your-database-name'
DATABASE_USER='your-database-user'
DATABASE_PASSWORD='your-database-password'
DATABASE_HOST = 'your-databse-host' 
DATABASE_PORT ='your-databse-port'
DATABASE_ENGINE ='your-database-engine'
```

- Apply migrations to set up the database:
```bash
python manage.py migrate
```

- Create a superuser for the Django admin:
```bash
python manage.py createsuperuser
```
- run this commands :
``` bash
python manage.py populate_data
python manage.py populate_category
python manage.py space_agency
```
Run the development server to verify:
```bash
python manage.py runserver
```
Open http://127.0.0.1:8000 to check if your project is working.
### 🌠 Future Enhancements
User Authentication: Allow users to log in and save favorite articles or views.
Real-Time API Integration: Display live data on astronomical events, satellite tracking, and more.
Explore, learn, and be inspired by the wonders of space with the Celestial Explore Blog!

## Screenshots

#### Home page:
![App Screenshot](sreenshots/home.png)

#### Blog page:

![App Screenshot](sreenshots/blog.png)

#### solar explore(3d-view):

![App Screenshot](sreenshots/3d-view-speed.png)

#### solar explore(2d-view):

![App Screenshot](sreenshots/2d-view-speed.png)

#### solar explore size view:

![App Screenshot](sreenshots/order.png)

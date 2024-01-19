# EMR - Electronic Medical Record System

## Overview
The EMR (Electronic Medical Record) system is designed with a microservice architecture to securely collect, store, and manage comprehensive patient health information. This system integrates with other healthcare services and is built for scalability with core functionalities that encompass personal information management, emergency contacts, past doctor details, medical data, and patient history.

## Features
- Create, view, and manage patient records using a streamlined Streamlit interface.
- Upload and store medical images like X-rays without additional processing features.
- Interact with a system adhering to health data privacy and security regulations.

## User Stories
- Healthcare providers can manage various aspects of patient information through the system.
- Backend services ensure secure and efficient handling of patient data.

## Technologies
- Backend development is focused on using Node.js, Express, and Sequelize.
- Frontend interaction is facilitated by Streamlit hosted on Streamlit sharing.
- Data is stored in PostgreSQL, utilizing elephantSQL as the database service.
- The system's design incorporates Python, Peewee, and Flask for additional functionality.
- Secure authentication using JSON Web Tokens and bcrypt.
- Aesthetic design with Bootstrap, along with HTML and CSS3.
- Data fetching performed with axios.

## Project Structure
- The `package.json` contains the list of dependencies necessary for the project.
- `src/app.js` is the entry point to our Express application.
- Routes are defined in `src/routes/patientRoutes.js` and handled by `src/controllers/patientsController.js`.
- Patient model is encapsulated in `models/patient.js`.
- Database configuration is specified in `config/config.json`.
- `migrations/create-patient.js` handles the creation of the patient's table.
- The Flask app in `medical_image_service.py` is responsible for handling image uploads. Database model in `models.py`.

## Configuration
Place environment variables in the `.env` file, ensuring database connection strings and any other sensitive information are properly set.

## Installation
After cloning the repository, install node modules:

```bash
npm install
```

Start the backend service:

```bash
npm start
```

Start the Streamlit frontend in a separate terminal:

```bash
streamlit run your_streamlit_app.py
```

Execute the Flask service for medical image upload:

```bash
flask run --port=3001
```

## Testing
Execute a comprehensive suite of tests to validate the system's functions and integration points regularly.

Ensure accurate and up-to-date documentation to assist in a flawless execution of tests.

## Licensing
This project is licensed under the ISC license.

## Contributing
Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## Authors
- Your Name (add more contributors as needed)

## Acknowledgments
A tip of the hat to everyone who contributed to this project, offered support, and provided feedback.
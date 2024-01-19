# EMR - Electronic Medical Record System

## Overview

The EMR (Electronic Medical Record) system is a robust solution designed to manage patient health information through a microservice architecture. It enables healthcare providers to collect, store, and access extensive patient data, integrating seamlessly with other healthcare systems and built with scalability in mind.

### Core Functionalities
- Manage personal details, emergency contacts, and past doctor information
- Record and manage comprehensive medical data and history
- Upload and store medical images

### User-Friendly Interface
- Streamlit-based frontend for simple and intuitive data input and retrieval

### Security and Compliance
- Adheres to health data privacy and security best practices

## User Stories
- Healthcare providers enter and manage patient data
- Secure upload and storage of medical imagery
- Easy access to patient records and medical histories

## Technologies
- Backend powered by Node.js, Express, Sequelize, PostgreSQL
- Frontend developed with Streamlit, Bootstrap, HTML, and CSS3
- Security via JSON Web Tokens and bcrypt
- Efficient data fetching with axios
- Data storage on elephantSQL

## Current Project Files
**Important paths and files detailed within the project include:*** `package.json` - Project metadata and dependencies
* `src/app.js` - Main Express server application
* `config/config.json` - Database configurations for different environments
* `models/` - Sequelize models for representing database entities
* `migrations/` - Database migration files for creating tables
* `src/controllers/` and `src/routes/` - Express routes and controllers for API endpoints
* `medical_image_service.py` - Flask service for image upload functionality
* `.env` - Environment variable definitions

## Getting Started

### Prerequisites
- Node.js
- Python
- PostgreSQL

### Initial Setup
- Clone the repository
- Install dependencies with `npm install`
- Set up environment variables according to the `.env` schema

### Run the Application
- Start the backend server with `npm start`
- Launch the Streamlit frontend using `streamlit run streamlit_app.py`
- Run the Flask service for medical image uploads with `flask run --port=3001`

## Testing
Regular testing is crucial to ensure the integrity and reliability of the EMR system. See `TESTING.md` (to be created) for guidelines on how to conduct tests.

## Contribution
We welcome contributions! For details on contributing, please see `CONTRIBUTING.md` (to be created).

## License
This project is licensed under the ISC license - see the `LICENSE` file for details.

## Acknowledgments
Our gratitude extends to all contributors and testers of this project.
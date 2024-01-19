# EMR System Architecture

## Overview
This document describes the architecture and data flow of the Electronic Medical Record (EMR) system, which is developed with a microservice architecture pattern.

## Components
The EMR system consists of several key components:

- **Streamlit Interface**: Serves as the frontend through which healthcare providers interact with the system. Users can add new patient records, view, update, and delete existing records.

- **Patient Information Service**: A microservice in Node.js/Express that manages CRUD operations for patient records. It communicates with the elephantSQL database to store and retrieve patient information.

- **Medical Image Upload Service**: Implemented in Python with Flask, this service manages the upload and storage of medical images, such as X-rays.

- **elephantSQL Database**: PostgreSQL database-as-a-service to store patient data and metadata for uploaded images.

## Data Flow Overview
- When a healthcare provider uses the Streamlit interface to input or access patient data, HTTP requests are issued to the backend microservices.

- **Auth Middleware** validates the JWT before allowing access to patient data.
- The **Patient Information Service** processes the requests to create, read, update, or delete patient data and communicates with the elephantSQL database.
- The **Medical Image Upload Service** saves the binary data of the images and stores the metadata in the elephantSQL database.

## Authentication
- While no end-user authentication functionality is required, the system simulates token-based authentication using JWT tokens for API routes.

- The `authMiddleware` on Node.js Backend checks for tokens in incoming requests to secure routes.

## Secure Data Management
- All communication with the database and between microservices use encrypted connections to comply with health data privacy regulations.

- Appropriate security standards are applied to patient data and medical images to ensure confidentiality and integrity.

## Conclusion
The EMR system's architecture is designed to ensure a user-friendly experience, secure data management, and efficient data flow between various components. The system also has scalability in mind, allowing for future expansion and integrations.

// INPUT_REQUIRED {Please review this system architecture summary for accuracy and completeness. Adjust details as necessary to match the system you are working on.}
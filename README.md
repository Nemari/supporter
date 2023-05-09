# Supporter

This is a Django web application that allows users to ask questions and get answers based on a pre-trained model. The application is Dockerized for easy deployment and portability.

## Requirements

- Docker 
- Docker Compose 
- OpenAI API key.

## Getting Started

Follow the steps below to get the Django project up and running:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   
2. Create in root directory .env.bat file with next context:
    ```bash
    OPENAI_KEY=<OpenAI API key>
    ```
3. Build and start the Docker containers:
  ```bash
   docker-compose up --build
  ```
4. Open your web browser and visit http://localhost:8000/chat to access the Django application.
    

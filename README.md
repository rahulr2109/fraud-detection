# Fraud Detection System

## Overview

The Fraud Detection System is a real-time, distributed application designed to detect fraudulent transactions. The system streams transaction data via Apache Kafka, processes data with a machine learning model (IsolationForest) using a FastAPI backend, and notifies users immediately via WebSockets. Historical transaction data and fraud alerts are stored in MongoDB Atlas and cached in Redis. A user-friendly Angular dashboard displays detailed transaction analytics along with real-time fraud alerts.

## Architecture

The system is composed of several key components:

- **Apache Kafka:**  
  Streams transaction data between producers and consumers.
- **FastAPI Backend:**  
  Provides RESTful endpoints for retrieving transaction data and fraud alerts, and also hosts a WebSocket endpoint for real-time notifications.
- **Fraud Detection Service:**  
  Implements fraud detection using the IsolationForest algorithm (from scikit-learn).
- **MongoDB Atlas:**  
  Stores historical transaction and fraud alert data.
- **Redis:**  
  Caches fraud alerts for quick retrieval.
- **WebSockets:**  
  Enables real-time communication from the server to the frontend.
- **Angular Frontend:**  
  A responsive dashboard built with Angular and Angular Material that displays historical data (with pagination) and real-time fraud alerts.

## Technologies Used

- **Backend:**
  - Python, FastAPI, Uvicorn
  - Apache Kafka (using `kafka-python`)
  - scikit-learn (IsolationForest)
  - Pandas
  - MongoDB Atlas
  - Redis
  - WebSockets
- **Frontend:**
  - Angular (using standalone components)
  - Angular Material (tables, paginator, sort, etc.)
  - SCSS for styling
- **Deployment & Monitoring (Optional):**
  - Docker & Docker Compose
  - Grafana & Prometheus

## Project Structure

```
fraud-detection/
├── api/
│   ├── main.py              # Main FastAPI application
│   ├── websocket_routes.py  # WebSocket endpoints for real-time updates
├── services/
│   ├── mongodb_service.py   # MongoDB interactions
│   ├── redis_service.py     # Redis caching for fraud alerts
│   ├── kafka_service.py     # Kafka producer/consumer logic
│   ├── fraud_detection.py   # Fraud detection logic (IsolationForest)
│   └── ws_manager.py        # WebSocket connection manager
├── consumer.py              # Kafka consumer for processing transactions
├── test_kafka_producer.py   # Test script for Kafka production
├── .env                     # Environment variables
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation (this file)
└── frontend/                # Angular frontend application
    ├── src/
    │   ├── app/
    │   │   ├── app.component.ts
    │   │   ├── dashboard/
    │   │   │   ├── dashboard.component.ts
    │   │   │   ├── dashboard.component.html
    │   │   │   └── dashboard.component.scss
    │   │   └── fraud-alerts/
    │   │       ├── fraud-alerts.component.ts
    │   │       ├── fraud-alerts.component.html
    │   │       └── fraud-alerts.component.scss
    ├── package.json
    └── angular.json
```

## Installation and Setup

### Prerequisites

- **Python 3.8+**
- **Node.js & npm**
- **Angular CLI:** Install with `npm install -g @angular/cli`
- Access to a Kafka cluster (e.g., Aiven Kafka), a MongoDB Atlas cluster, and a Redis instance.

### Backend Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/rahulr2109/fraud-detection
   cd fraud-detection
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   # For WebSocket support, install Uvicorn with extras:
   pip install "uvicorn[standard]"
   ```

4. **Configure Environment Variables:**

   Create a `.env` file in the project root with entries similar to:

   ```ini
   # Kafka configuration
   KAFKA_BROKER_URL=kafka_url
   KAFKA_SSL_CAFILE=./certs/ca.pem
   KAFKA_SSL_CERTFILE=./certs/access.cert
   KAFKA_SSL_KEYFILE=./certs/access.key

   # MongoDB configuration
   MONGO_URI=mongodb+srv://<username>:<password>@your-cluster.mongodb.net/fraud_detection?retryWrites=true&w=majority

   # Redis configuration
   REDIS_HOST=host_name
   REDIS_PORT=18025
   REDIS_PASSWORD=your_redis_password
   ```

5. **Run the FastAPI Server:**

   ```bash
   uvicorn api.main:app --reload
   ```

6. **Start the Kafka Consumer (if needed):**

   ```bash
   python consumer.py
   ```

### Frontend Setup

1. **Navigate to the Frontend Directory:**

   ```bash
   cd frontend
   ```

2. **Install Dependencies:**

   ```bash
   npm install
   ```

3. **Serve the Angular Application:**

   ```bash
   ng serve --open
   ```

   The Angular dashboard should open at `http://localhost:4200`.

## Real-Time Functionality

The system uses WebSockets for real-time fraud alert notifications. The FastAPI backend exposes a WebSocket endpoint (e.g., `/ws/fraud`) which pushes fraud alerts to connected clients immediately when a fraudulent transaction is detected. On the Angular side, the `FraudAlertsService` manages the WebSocket connection and streams live updates to the UI.

## WebSocket Integration

### Backend (FastAPI)

- **WebSocket Connection Manager:**  
  See `services/ws_manager.py` for managing active WebSocket connections.
  
- **WebSocket Routes:**  
  The `api/websocket_routes.py` file defines a WebSocket endpoint (`/ws/fraud`) to handle real-time communications.

- **Usage:**  
  When fraud is detected, your backend can call `await manager.broadcast(fraud_event)` to notify all connected clients.

### Frontend (Angular)

- **FraudAlertsService:**  
  The Angular service (`src/app/services/fraud-alerts.service.ts`) establishes a WebSocket connection to the FastAPI endpoint and exposes an Observable to stream fraud alert messages.

- **FraudAlertsComponent:**  
  The component subscribes to the service to display live fraud alerts.

### Contributing
---

## How to Contribute

Contributions are welcome! If you’d like to contribute to the project, please follow these steps:

### 1. Fork the Repository
- Navigate to the [project's GitHub repository](https://github.com/rahulr2109/fraud-detection).
- Click the **Fork** button in the upper-right corner. This creates a copy of the repository in your GitHub account.

### 2. Clone Your Fork Locally
Open your terminal (or Git Bash on Windows) and clone your forked repository:

```bash
git clone https://github.com/rahulr2109/fraud-detection.git
```
This command creates a local copy of your fork.

### 3. Create a New Branch
Before making any changes, create a new branch to work on your feature or bug fix. This helps keep your work organized and makes it easier to submit a pull request later.

```bash
cd fraud-detection
git checkout -b feature/my-new-feature
```

Replace `feature/my-new-feature` with a descriptive branch name.

### 4. Make Your Changes
- Open the project in your favorite code editor.
- Make the necessary changes, improvements, or bug fixes.
- Test your changes to ensure everything works as expected.

### 5. Commit Your Changes
Once you're satisfied with your changes, commit them with a clear and concise commit message:

```bash
git add .
git commit -m "Add a detailed explanation for feature X" 
```

Be sure to explain what changes you made and why they were necessary.

### 6. Push Your Branch to Your Fork
Push your branch to your GitHub fork:

```bash
git push origin feature/my-new-feature
```

### 7. Create a Pull Request (PR)
- Go to your fork on GitHub.
- Click on the **Compare & pull request** button next to your new branch.
- Provide a clear title and a detailed description of your changes.
- Click **Create pull request**.

### 8. Respond to Feedback
Your pull request will be reviewed by the project maintainers. They may suggest changes or improvements:
- If changes are requested, make those changes in your branch, commit, and push them. The PR will update automatically.
- Once the PR is approved, it will be merged into the main repository.

### 9. Stay Updated
- To keep your fork up-to-date with the original repository, you can set the original repository as an upstream remote:

```bash
git remote add upstream https://github.com/yourusername/fraud-detection.git
```

- Then, periodically fetch the latest changes and merge them into your branch:

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

---

By following these steps, you can contribute effectively to the project. If you have any questions or need help, please feel free to open an issue on the repository or contact the maintainers directly.

Happy coding!



## Contact

For any questions or suggestions, please contact rahul0921r@gmail.com

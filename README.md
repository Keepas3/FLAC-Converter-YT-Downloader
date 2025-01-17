# Music-Converter


## Overview
VCRTS is a distributed cloud computing system that leverages parked vehicles' computational resources to create a static cloud computing environment. The system enables vehicle owners to monetize their parked vehicles' computing power while providing clients with computational resources for their jobs.

## Key Components

### Client Side (TheClientGUI)
* User registration and authentication
* Job submission interface
* Real-time job status monitoring
* Resource usage tracking

### Server Side (TheServerGUI)
* Cloud controller administration
* Resource allocation management
* Job scheduling and monitoring
* System status dashboard

## Core Features

### User Management
* Vehicle Owner registration/login
* Job Submitter (Client) registration/login
* Cloud Controller administration

### Vehicle Resource Management
* Vehicle registration with specs (VIN, computational power, storage)
* Residency time tracking
* Resource availability monitoring

### Job Processing
* FIFO job scheduling
* Automated completion time calculation
* Job status tracking
* Priority-based job management

## Technical Stack
* Backend: Java
* Frontend: Java Swing
* Database: MySQL
* Authentication: Custom implementation with database integration

## Database Schema
* Users (Vehicle Owners, Job Submitters, Cloud Controllers)
* Vehicles (Resources)
* Jobs
* Vehicle Assignments

## Getting Started

### Prerequisites
* Java JDK 11+
* MySQL 8.0+
* Environment variables configured:
  ```
  url: Database URL
  sqlusername: Database username
  password: Database password
  ```

### Installation
1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/VCRTS.git
   ```
2. Import SQL schema
   ```bash
   mysql -u root -p < VCRTS-TablesV1.sql
   ```
3. Compile Java files
   ```bash
   javac *.java
   ```

### Running the Application
1. Start the server
   ```bash
   java TheServerGUI
   ```
2. Start the client
   ```bash
   java TheClientGUI
   ```

## Project Structure
VCRTS/
├── *.java               # Source files
├── *.class              # Compiled classes
├── jobs/                # Job submission records
├── resources/           # Resource configuration


## Classes Overview
* `User`: Base class for system users
* `VehicleOwner`: Manages vehicle registration and ownership
* `JobSubmitter`: Handles job submission and tracking
* `Vehicle`: Represents computational resources
* `CloudController`: Manages resource allocation
* `Authentication`: Handles user authentication
* `TheClientGUI/TheServerGUI`: User interfaces

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Submit Pull Request

## Authors
* Bryan Fung
* Tomas Santos Yciano
* Albert Legacki
* Allan Ilyasov
* Mathew Martinez

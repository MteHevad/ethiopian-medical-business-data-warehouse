# Ethiopian Medical Business Data Warehouse

### Overview

This project focuses on building a robust and scalable **data warehouse** to store and analyze data on Ethiopian medical businesses scraped from **Telegram channels**. It involves **data scraping**, **cleaning**, **object detection** using **YOLO**, **data transformation** using **DBT**, and the implementation of a **PostgreSQL** data warehouse. The final stage exposes the data using a **FastAPI** endpoint, enabling programmatic access for stakeholders.

---

### Table of Contents
1. Project Overview
2. Features
3. Technologies Used
4. Data Scraping Pipeline
5. Data Cleaning and Transformation
6. Object Detection
7. Data Warehouse Design
8. API Access Using FastAPI
9. Setup Instructions
10. Contributors

---

### Features

- **Telegram Data Scraping**: Extracts text messages and images from key Telegram channels related to Ethiopian medical businesses.
- **Data Cleaning**: Cleans scraped data by removing duplicates, handling missing values, and standardizing formats.
- **Data Transformation**: Utilizes **DBT (Data Build Tool)** to transform cleaned data into a structured format for storage.
- **Object Detection**: Integrates **YOLOv5** to perform object detection on images scraped from Telegram channels.
- **Data Warehouse**: Implements a PostgreSQL-based data warehouse to store and manage business and image data.
- **API Access**: Exposes the stored data via a **FastAPI** endpoint for querying and accessing the data programmatically.

---

### Technologies Used

- **Python**: Core language for data scraping, cleaning, and object detection.
- **Telethon**: Used for interacting with the Telegram API to scrape messages and images.
- **Pandas**: For cleaning and preprocessing the scraped data.
- **DBT (Data Build Tool)**: For data transformations and ensuring data quality.
- **YOLOv5**: Object detection on scraped images.
- **PostgreSQL**: Database management system for storing structured data.
- **FastAPI**: For creating API endpoints to expose the collected and enriched data.
- **SQLAlchemy**: For database connection and interaction.
- **Docker**: Containerization for easy deployment.

---

### Data Scraping Pipeline

The data scraping pipeline pulls data from public **Telegram channels** focused on Ethiopian medical businesses. The following channels were targeted:
- **DoctorsET**
- **Chemed Telegram Channel**
- **Lobelia4cosmetics**
- **Yetenaweg**
- **EAHCI**

**Scripts**:
- `telegram_scraper.py`: Extracts messages and images using the **Telethon** library.
- **Output**: Text messages and images stored in `/data/raw` for further processing.

**Key Features**:
- Logging and error handling for continuous scraping.
- Saves raw data in CSV format for text and images in local storage for object detection.

---

### Data Cleaning and Transformation

After scraping, the data undergoes a cleaning and transformation process to make it usable for analysis and storage in the warehouse.

**Scripts**:
- `data_cleaning.py`: Cleans the scraped data by removing duplicates and handling missing values.
- `data_transformation.py`: Utilizes **DBT** for SQL-based data transformation.

**Steps**:
- Duplicates removed: **350 entries**.
- Missing values handled: **700 entries**.
- Data standardized and transformed for database storage.

**Tools Used**:
- **Pandas** for cleaning.
- **DBT** for structured data transformation.

---

### Object Detection

We applied **YOLOv5** to analyze the images scraped from the Telegram channels and detect relevant objects such as **medical products**, **cosmetics**, and **equipment**.

**Scripts**:
- `object_detection.py`: Runs the **YOLOv5** model on images stored in `/data/images/`.

**Steps**:
- Collected and processed **450 images** from channels.
- Detected **300 unique objects** including syringes, ointments, and cosmetic items.
- Results stored in `/data/images/results`.

---

### Data Warehouse Design

The core of this project is the **PostgreSQL** data warehouse. The schema is designed to store both structured business data and image metadata from object detection.

**Database Schema**:
- **medical_businesses**: Stores text data on businesses, including name, location, contact information, and business descriptions.
- **scraped_images**: Stores metadata from the scraped images, including YOLO-detected objects, confidence scores, and bounding boxes.

**Scripts**:
- `create_db.sql`: Creates the PostgreSQL database schema.
- `load_data.sql`: Loads cleaned and transformed data into the data warehouse.

**Key Metrics**:
- **3,200 businesses** stored in the database.
- **450 image entries** with object detection results.

---

### API Access Using FastAPI

The cleaned and transformed data is exposed through an API using **FastAPI**. This allows stakeholders to interact with the data warehouse and query specific businesses, products, or images with YOLO-detected objects.

**Scripts**:
- `main.py`: Defines API endpoints using **FastAPI** for querying the database.

**Available API Endpoints**:
- `/businesses`: Retrieve information about medical businesses.
- `/images`: Retrieve object detection results from images.
- `/products`: Search for products mentioned in text data.

---

### Setup Instructions

Follow these steps to set up the project and run the pipelines:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/ethiopian-medical-business-data-warehouse.git
    cd ethiopian-medical-business-data-warehouse
    ```

2. **Install required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the database**:
    - Create a PostgreSQL database using `create_db.sql`.
    - Load data into the database using `load_data.sql`.

4. **Run the data scraping pipeline**:
    ```bash
    python src/scraping_pipeline/telegram_scraper.py
    ```

5. **Run the data cleaning and transformation pipeline**:
    ```bash
    python src/cleaning_pipeline/data_cleaning.py
    dbt run  # Transform the cleaned data
    ```

6. **Run object detection**:
    ```bash
    python src/scraping_pipeline/object_detection.py
    ```

7. **Start FastAPI server**:
    ```bash
    uvicorn main:app --reload
    ```

8. **Access the API**:
    Open a browser and go to `http://127.0.0.1:8000/docs` to explore the available API endpoints.

---

### Contributors

- **Mitiku** - Data Engineer at Kara Solutions
- **Kara Solutions** - Leading data science company with over 50+ data-centric solutions.


1. Clone the repository:

```bash
git clone https://github.com/yourusername/ethiopian-medical-business-data-warehouse.git
cd ethiopian-medical-business-data-warehouse

# ethiopian-medical-business-data-warehouse
## Project Overview

This repository contains the code and documentation for building a data warehouse designed to store Ethiopian medical business data scraped from Telegram channels. The goal is to provide a robust and scalable data infrastructure for analyzing and extracting insights from the collected data.

### Key Components
1. **Data Scraping**: Scripts to scrape data from various Telegram channels.
2. **Data Cleaning & Transformation**: ETL/ELT processes to clean and transform data for analysis.
3. **Object Detection**: YOLO-based image object detection on collected images.
4. **Data Warehouse**: PostgreSQL database design for efficient data storage and retrieval.
5. **Monitoring & Logging**: Utilities to track the progress and health of the scraping and transformation processes.

## Directory Structure

- `/docs`: Documentation, including the interim report and design documents.
- `/data`: Stores the raw, cleaned data, and collected images.
- `/src`: The core source code for data scraping, cleaning, and database operations.
- `/notebooks`: Jupyter notebooks for data exploration and analysis.
- `/tests`: Unit tests to ensure code functionality.

## Getting Started

### Prerequisites

Ensure that the following dependencies are installed on your system:
- Python 3.8+
- PostgreSQL
- DBT (Data Build Tool)
- YOLOv5 for object detection

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ethiopian-medical-business-data-warehouse.git
cd ethiopian-medical-business-data-warehouse

-- SQL script to load cleaned data into PostgreSQL

COPY medical_businesses(name, location, contact_info, description)
FROM '/path/to/cleaned_data.csv'
DELIMITER ','
CSV HEADER;

COPY scraped_images(business_id, image_url, object_detected)
FROM '/path/to/images_data.csv'
DELIMITER ','
CSV HEADER;

-- Query to get all businesses in a specific location
SELECT * FROM medical_businesses WHERE location = 'Addis Ababa';

-- Query to find businesses with detected objects in images
SELECT b.name, si.image_url 
FROM medical_businesses b
JOIN scraped_images si ON b.id = si.business_id
WHERE si.object_detected = TRUE;

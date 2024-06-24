from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Navigate to the page with reviews
url = 'https://www.google.com/maps/place/Brook+Restoration+Ltd/@43.6894916,-79.5787702,17z/data=!4m8!3m7!1s0x4cce0f89676bfef1:0x22d7b5dc07bb0c7e!8m2!3d43.6894877!4d-79.5762006!9m1!1b1!16s%2Fg%2F1tgkhxyv?entry=ttu'  # Replace with the actual URL
driver.get(url)

# Find all review elements
reviews = driver.find_elements(By.CLASS_NAME, 'GHT2ce')

# Extract reviews with 5 stars
five_star_reviews = []
for review in reviews:
    try:
        star_element = review.find_element(By.CLASS_NAME, 'kvMYJc')
        star_label = star_element.get_attribute('aria-label')
        if '5 stars' in star_label:
            review_text_element = review.find_element(By.CLASS_NAME, 'wiI7pd')
            review_text = review_text_element.text
            five_star_reviews.append(review_text)
    except Exception as e:
        print(f"An error occurred: {e}")

# Print out the 5-star reviews
for review in five_star_reviews:
    print(review)

# Close the WebDriver
driver.quit()

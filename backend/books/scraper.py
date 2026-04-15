from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_books():
    driver = webdriver.Chrome()
    driver.get("https://books.toscrape.com/")

    time.sleep(3)

    books = driver.find_elements(By.CLASS_NAME, "product_pod")

    data = []

    for book in books[:5]:
        title = book.find_element(By.TAG_NAME, "h3").text
        
        data.append({
            "title": title,
            "author": "Unknown",
            "description": "Sample scraped book",
            "rating": 4.0,
            "url": "https://books.toscrape.com/"
        })

    driver.quit()
    return data
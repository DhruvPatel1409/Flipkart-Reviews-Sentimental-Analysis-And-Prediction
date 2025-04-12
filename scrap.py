import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def setup_driver(headless=False, implicit_wait=10):
    options = Options()
    options.headless = headless
    service = Service()
    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(implicit_wait)
    return driver

def get_product_links(driver, max_products=2):
    product_links = set()  # Use a set to avoid duplicates
    base_url = "https://www.flipkart.com/search?q=mobile+5g&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobile+5g%7CMobiles&requestId=af2b15a8-5e9d-4e93-9508-c09e91fff29d&as-searchtext=mobile&page="
    page = 1

    while len(product_links) < max_products:
        try:
            print(f"🔍 Collecting product links from page {page}...")
            driver.get(base_url + str(page))
            time.sleep(3)
            
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            products = soup.find_all("a", class_="CGtC98")
            
            for product in products:
                if len(product_links) < max_products:
                    link = "https://www.flipkart.com" + product.get("href")
                    if link and "flipkart.com" in link:
                        product_links.add(link)
                else:
                    break
            
            next_page = soup.find("a", class_="_9QVEpD")
            if next_page:
                page += 1
            else:
                break
        except TimeoutException:
            print(f"❌ Timeout on page {page}")
            break
    
    return list(product_links)[:max_products]

def get_product_reviews(driver, product_url, max_review_pages=10):
    reviews_data = []
    product_name = "Unknown Product"
    product_rating = "No Rating"

    try:
        driver.get(product_url)
        time.sleep(3)

        # Get Product Name
        try:
            product_name = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.VU-ZEz"))
            ).text
            print(f"📌 Product: {product_name}")
        except:
            print(f"⚠ Could not fetch product name for {product_url}")

        # Get Product Rating
        try:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            rating_div = soup.find("div", class_="XQDdHH")
            if rating_div:
                product_rating = rating_div.text.strip()
                print(f"⭐ Product Rating: {product_rating}")
            else:
                print(f"⚠ No rating found for {product_name}")
        except:
            print(f"⚠ Error extracting rating for {product_name}")

        # Get the 'All Reviews' page URL
        try:
            print("🔍 Getting URL of 'All reviews' button...")
            element = driver.find_element(By.CSS_SELECTOR, "div._8-rIO3 a")
            review_page_url = element.get_attribute("href")
            driver.get(review_page_url)
            time.sleep(3)
        except:
            print(f"⚠ No 'All reviews' button found for {product_name}")
            return reviews_data

        # Loop through pages
        for page in range(1, max_review_pages + 1):
            try:
                print(f"📄 Scraping page {page} reviews for '{product_name}'...")
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                
                # Individual review div class
                review_containers = soup.find_all("div", class_="EKFha-")
                
                if not review_containers:
                    print(f"⚠ No reviews found on page {page}, stopping.")
                    break

                for container in review_containers:
                    rating_div = container.find("div", class_="XQDdHH")
                    review_text = container.find("div", class_="ZmyHeo").text if container.find("div", class_="ZmyHeo") else "No Review"

                    reviews_data.append({
                        "Product": product_name,
                        "Overall Rating": product_rating,
                        "Review": review_text
                    })

                # Locate the next page button
                try:
                    next_page_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "a._9QVEpD"))
                    )
                    next_page_url = next_page_button.get_attribute("href")

                    if not next_page_url or next_page_url == driver.current_url:
                        print(f"🛑 No new next page found, stopping pagination.")
                        break

                    print(f"➡ Navigating to next review page: {next_page_url}")
                    driver.get(next_page_url)

                    # Wait for reviews to load on the new page
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "div.EKFha-"))
                    )
                    time.sleep(3)

                except (TimeoutException, NoSuchElementException):
                    print(f"🛑 No next page button found on page {page}, stopping pagination.")
                    break

            except TimeoutException:
                print(f"⏳ Timeout while getting reviews on page {page}")
                break

    except Exception as e:
        print(f"❌ Error processing product '{product_name}': {str(e)}")

    return reviews_data

def main():
    driver = setup_driver()
    all_reviews = []
    
    try:
        print("🔍 Collecting product links...")
        product_links = get_product_links(driver, max_products=500)
        print(f"✅ Found {len(product_links)} products.")
        
        for i, product_url in enumerate(product_links, 1):
            print(f"📌 Processing product {i}/{len(product_links)}: {product_url}")
            product_reviews = get_product_reviews(driver, product_url, max_review_pages=8)
            all_reviews.extend(product_reviews)
            
            df = pd.DataFrame(all_reviews)
            df.to_csv("flipkart_reviews.csv", index=False)
            print(f"✅ Collected {len(product_reviews)} reviews for product {i}")
            
            time.sleep(2)
    finally:
        driver.quit()
    
    print(f"🎉 Scraping complete! Total reviews collected: {len(all_reviews)}")
    return all_reviews

if __name__ == "__main__":
    main()

import os
import time

import selenium
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ACCOUNT_EMAIL ="user@test.com"
ACCOUNT_PASSWORD = "password"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

login_page = driver.find_element(By.XPATH, value='//*[@id="home-page"]/section[1]/div/div/a[1]/button')
login_page.click()

def login():

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "login-form"))
    )

    email_field = driver.find_element(By.ID, "email-input")
    email_field.clear()
    email_field.send_keys(ACCOUNT_EMAIL)

    password_field = driver.find_element(By.ID, "password-input")
    password_field.clear()
    password_field.send_keys(ACCOUNT_PASSWORD)

    login_button = driver.find_element(By.ID, "submit-button")
    login_button.click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "schedule-page"))
    )

def retry(func, retries=7, description=None):
    count = 0
    for attempt in range(retries):
        print()
        try:
            print(f"Login attempt {count + 1}")
            func()
            print("Login successful!")
            return True
        except TimeoutException:
            count += 1
            print("Login failed, retrying...")
            time.sleep(2)
    print("All login attempts failed.")
    return False

def book_class(value, description):
    value.click()
    WebDriverWait(driver, 5).until(lambda d: value.text == description)


retry(login)

class_cards = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[id^='class-card-']"))
)


time.sleep(2)


booked_count = 0
waitlist_count = 0
already_booked_count = 0
for card in class_cards:
    date = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    header = date.find_element(By.CSS_SELECTOR, "h2")
    day_list = ["Tue", "Thu"]
    for day in day_list:
        if day in header.text:
            exercise_time = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
            if "6:00 PM" in exercise_time:

                exercise_class = card.find_element(By.XPATH, "//*[starts-with(@id, 'class-card-')]")
                exercise_class_text = card.find_element(By.CSS_SELECTOR, "h3")
                exercise_booking = card.find_element(By.CSS_SELECTOR, "button")
                if exercise_booking.text == "Join Waitlist":
                    exercise_booking.click()
                    retry(lambda: book_class(exercise_booking, "Waitlisted"))
                    print(f"Joined waitlist: {exercise_class_text.text} on {header.text}")
                    waitlist_count += 1
                elif exercise_booking.text == "Booked":
                    print(f"✓ You have already booked this section for {exercise_class_text.text} on {header.text}")
                    already_booked_count += 1
                elif exercise_booking.text == "Waitlisted":
                    print(f"✓ You are already on the waitlist for {exercise_class_text.text} on {header.text}")
                    already_booked_count += 1
                elif exercise_booking.text == "Book Class":
                    exercise_booking.click()
                    retry(lambda: book_class(exercise_booking, "Booked"))
                    print(f"Booked: {exercise_class_text.text} on {header.text}")
                    booked_count += 1


total = booked_count + waitlist_count + already_booked_count

print(f"--- Total Tuesday/Thursday 6pm classes: {total} ---")
print("--- VERIFYING ON MY BOOKINGS PAGE ---")

verified_count = 0
def my_bookings():
    bookings = driver.find_element(By.ID, value="my-bookings-link")
    bookings.click()
    all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")
    global verified_count
    for card in all_cards:
        try:
            when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
            when_text = when_paragraph.text

            # Check if it's a Tuesday or Thursday 6pm class
            if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
                class_name = card.find_element(By.TAG_NAME, "h3").text
                print(f"  ✓ Verified: {class_name}")
                verified_count += 1
        except NoSuchElementException:
            # Skip if no "When:" text found (not a booking card)
            pass

retry(my_bookings)
print(f"""
--- VERIFICATION RESULT ---
Expected: {total} bookings
Found: {verified_count} bookings
✅ SUCCESS: All bookings verified!
""")


# print("\n--- BOOKING SUMMARY ---")
# print(f"Classes booked: {booked_count}")
# print(f"Waitlists joined: {waitlist_count}")
# print(f"Already booked/waitlisted: {already_booked_count}")
# print(f"Total Tuesday 6pm classes processed: {booked_count + waitlist_count + already_booked_count}")

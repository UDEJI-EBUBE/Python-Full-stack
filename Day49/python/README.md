# Day 49
Today i creadted a automated bot that check a demo gym website for aailable bookings and waitlists
- extra knowledge gained was the use of slenium to get that match starting letters of a  string e.g
```
driver.find_elements(By.XPATH, "//*[starts-with(@id, 'class-card-')]")
driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
```
## Lambda Functions for Retry

- Learned to use `lambda` to wrap functions that require arguments, so they can be passed to a retry system without being executed immediately.
  
- Example:

```python
retry(lambda: book_class(button), description="Booking")

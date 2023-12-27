# Scatping the top box office movie from rotten tomatoes

from selenium import webdriver

def access_page(web_url):
    # 1. Open "Rotten Tomatoes" website
    browser = webdriver.Chrome()
    browser.get(web_url)

    browser.close()

# 2. Find the "movie" tab
# 3. Hover(not press) to the "movie" button 
# 4. Find "Top box office" button
# 5. Press "Top box office" button
# 6. Find "TOMATOMETER" tab
# 7. Press "TOMATOMETER" button
# 8. Find the first button "CERTIFIED FRESH"
# 9. Choose "CERTIFIED FRESH"
# 10. Find "APPLY" button
# 11. Press "APPLY" button
# 12. Get the first movie element
# 13. Get the name of the movie
# 14. Save the name into Database
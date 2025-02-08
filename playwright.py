from playwright.sync_api import sync_playwright

def scrape_profile_info(url: str):

    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        context = browser.new_context(viewport={"width":1920,"height":1080})
        page = context.new_page()

        page.on("response", intercept_response)

        page.goto(url)
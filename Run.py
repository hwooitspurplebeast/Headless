from playwright.sync_api import sync_playwright

def automate_without_head():
    # Launch the browser in headless mode
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        # Perform automation tasks
        page = context.new_page()
        page.goto('https://example.com')
        print(page.title())

        # Close the browser
        browser.close()

if __name__ == "__main__":
    automate_without_head()

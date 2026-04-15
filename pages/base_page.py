from playwright.sync_api import sync_playwright


class BasePage:
    def __init__(self, url):
        self.url = url
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start_browser(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=False,
            channel="msedge"  # или "chrome" или в оригинале SberBrowser и путь к нему
        )
        self.context = self.browser.new_context(
            client_certificates=[{
                "origin": self.url,
                "pfxPath": r"C:\Downloads\cert.pfx",
                "passphrase": "password"
            }]
        )
        self.page = self.context.new_page()
        return self.page

    def goto(self):
        self.page.goto(self.url)

    def close(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
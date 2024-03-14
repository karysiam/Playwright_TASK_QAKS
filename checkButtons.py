# 14-03-2024
# QAKS - CASO DE PRUEBA No. 7: VALIDACION DE LINKS, AL DAR CLICK SOBRE CADA UNO DEBE FUNCIONAR Y SER COHERENTE

import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()

        await page.goto("https://nozzmo.com/recruiting")
  
        await page.locator("section").filter(has_text="We assess candidates for both").get_by_role("link").click()
        await page.wait_for_timeout(5000)
        await page.screenshot(path="screenshots/chkButtons/ScheduleBtn1.png")

        await page.goto("https://nozzmo.com/recruiting")
        await page.wait_for_timeout(5000)
        await page.locator("section").filter(has_text="Discover how we helped a").get_by_role("link").click()
        await page.wait_for_timeout(5000)
        await page.screenshot(path="screenshots/chkButtons/ScheduleBtn2.png")

        await page.goto("https://nozzmo.com/recruiting")
        await page.wait_for_timeout(5000)
        await page.locator("section").filter(has_text="Start by scheduling a free").get_by_role("link").click()
        await page.wait_for_timeout(5000)
        await page.screenshot(path="screenshots/chkButtons/ScheduleBtn3.png")

        await page.goto("https://nozzmo.com/recruiting")
        await page.wait_for_timeout(5000)
        await page.locator("section").filter(has_text="Ready to take your hiring").get_by_role("link").click()
        await page.wait_for_timeout(5000)
        await page.screenshot(path="screenshots/chkButtons/ScheduleBtn4.png")

        #-Stoping Tracing
        await context.tracing.stop(path = "logs/traceCheckButtons.zip")
        #-Closing browser
        await browser.close()



asyncio.run(main())
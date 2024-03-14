# 14-03-2024
# QAKS - CASO DE PRUEBA No. 8: VALIDACION DEL ACORDEON DE LOS PROCESOS, AL DAR CLICK SOBRE CADA UNO DEBE MOSTRAR
# EL DETALLE DEL MISMO

import asyncio
from playwright.async_api import async_playwright, expect
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()

      
        await page.goto("https://nozzmo.com/recruiting")
        
        await page.get_by_text("Understanding your needs").click()
        await page.wait_for_timeout(10000)
        await page.screenshot(path="screenshots/chkAcordeon/UnderstandingOp1.png")
        await page.get_by_text("Sourcing candidates").click()
        await page.wait_for_timeout(10000)
        await page.screenshot(path="screenshots/chkAcordeon/SourcingOp2.png")
        await page.get_by_text("Technical evaluation").click()
        await page.wait_for_timeout(10000)
        await page.screenshot(path="screenshots/chkAcordeon/TechnicalOp3.png")
        await page.get_by_text("Cultural fit evaluation").click()
        await page.wait_for_timeout(10000)
        await page.screenshot(path="screenshots/chkAcordeon/CulturalOp4.png")
        await page.get_by_text("Data-driven insights").click()
        await page.wait_for_timeout(10000)
        await page.screenshot(path="screenshots/chkAcordeon/DataOp5.png")
        await page.get_by_text("Final selection and onboarding").click()
        await page.wait_for_timeout(10000)
        await page.screenshot(path="screenshots/chkAcordeon/FinalSelectionOp6.png")

        #-Stoping Tracing
        await context.tracing.stop(path = "logs/traceCheckAcordeon.zip")

        #-Closing browser
        await browser.close()

asyncio.run(main())
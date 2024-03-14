# 14-03-2024
# QAKS - CASO DE PRUEBA No. 1: VALIDACIÓN DE DESPLIEGUE DEL SITIO WEB EN ESCRITORIO,
# AL INGRESAR AL SITIO SE DEBE DESPLEGAR TODO EL CONTIDO DEL MISMO.

import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.goto("https://nozzmo.com/recruiting")
        await page.wait_for_timeout(5000)
        await page.screenshot(path="screenshots/loadWebSite.png")
        await browser.close()
asyncio.run(main())

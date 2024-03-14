# 14-03-2024
# QAKS - CASO DE PRUEBA No. 2: VALIDACIÓN DE DESPLIEGUE DEL SITIO WEB EN TELEFONO iPhone14,
# AL INGRESAR AL SITIO SE DEBE DESPLEGAR TODO EL CONTIDO DEL MISMO.

import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.webkit.launch(headless=False)
    context = await browser.new_context(**playwright.devices["iPhone 14"])
    page = await context.new_page()
    await page.goto("https://nozzmo.com/recruiting")
    await page.screenshot(path="screenshots/loadAppIphone14Inicio.png")
    await page.wait_for_timeout(10000)
    await page.screenshot(path="screenshots/loadAppIphone14Fin.png")

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())

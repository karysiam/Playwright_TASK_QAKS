# 14-03-2024
# QAKS - VALIDACION DE CAMPOS EN EL FORMULARIO DE CONTACTO

import asyncio
from playwright.async_api import async_playwright,expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
         
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
      
        await page.goto("https://nozzmo.com/recruiting")

        #CASO DE PRUEBA No. 3: VALIDACION DE LOS CAMPOS EN FORMATO INCORRECTO
        await page.fill('#name',  '1111')
        await page.fill('#email', 'testtesti.com')
        await page.fill('#more', 'mi proyecto es referente a finanzas.')

        #-Actions
        await page.get_by_role("button", name="Send").click()
        await page.wait_for_timeout(1000)
        await page.screenshot(path="screenshots/chkContactForm/checkContactFormTC1.png")

        #CASO DE PRUEBA No. 4: VALIDACION DE LOS CAMPOS EN FORMATO CORRECTO PERO INVALIDO PARA EL CAMPO "EMAIL"
        await page.fill('#name', 'abde')
        await page.fill('#email', 't@testi.com')
        await page.fill('#more', 'mi proyecto es referente a finanzas.')
        await page.wait_for_timeout(5000)
        #-Actions
        await page.get_by_role("button", name="Send").click()
        await page.screenshot(path="screenshots/chkContactForm/checkContactFormTC2.png")
        await page.wait_for_timeout(1000)
        
         #CASO DE PRUEBA No. 5: VALIDACION DE LOS CAMPOS EN FORMATO CORRECTO Y VALIDO PARA EL CAMPO "EMAIL"
        await page.fill('#name', 'Luna Castillo del Cid Ramirez')
        await page.fill('#email', 'lcastillo@gmail.com')
        await page.fill('#more', 'mi proyecto es referente a finanzas.')
        await page.wait_for_timeout(5000)
        await page.get_by_role("button", name="Send").click()
        await page.screenshot(path="screenshots/chkContactForm/checkContactFormTC3.png")

         #CASO DE PRUEBA No. 6: VALIDACION DE LOS CAMPOS DEJANDO VACIOS"
        await page.fill('#name', '')
        await page.fill('#email', '')
        await page.fill('#more', '')
        await page.get_by_role("button", name="Send").click()
        await page.wait_for_timeout(1000)
        await page.screenshot(path="screenshots/chkContactForm/checkContactFormTC4.png")


        #-Stoping Tracing
        await context.tracing.stop(path = "logs/traceCheckForm.zip")
    
        #-Closing browser
        await browser.close()


asyncio.run(main())
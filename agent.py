from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser
from browser_use.browser.context import BrowserContextConfig, BrowserContext
from dotenv import load_dotenv
from form_controller import controller
import os
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")

async def main():
    task = (
        "Complete the challenge in the provided website by ",
        "1. Configuring the download behavior",
        "2. Downloading the Excel file, ",
        "3. Reading the data, and",
        "4. Starting the challenge and filling out the first form with the information from the Excel file",
        "5. For each form, first analyze excel data, select the corresponding row and fill out the form with the data",
        "https://www.arenarpa.com/crazy-form"
    )

    # recordings directory path
    recording_path = "./recordings/"
    config = BrowserContextConfig(
        save_recording_path=recording_path
    )

    browser = Browser()
    context = BrowserContext(browser=browser, config=config)
    
    try:
        agent = Agent(
            task=task,
            llm=llm,
            controller=controller,  # Add our custom controller
            browser_context=context
        )
        result = await agent.run()
        print(result)
    finally:
        # Ensure we properly close the browser context
        await context.close()

if __name__ == "__main__":
    asyncio.run(main())

from browser_use import Browser, Controller, ActionResult
from typing import Dict, Any
import os
import pandas as pd
from pathlib import Path
import json

# Initialize the controller
controller = Controller()

async def handle_download(download):
    await download.save_as("./downloads/form_data.xlsx")
    print(f"Downloaded file saved to ./downloads")

@controller.action('Configure download behavior')
async def configure_download_behavior(browser: Browser, download_dir: str = "./downloads") -> str:
    """
    Configures the browser's download behavior to save files to the specified directory.
    This should be called before any download action is performed.
    Returns the configured download directory path.
    """
    # Make sure the download directory exists
    os.makedirs(download_dir, exist_ok=True)
    
    # Get the current page
    page = await browser.get_current_page()

    page.on("download", handle_download)
    
    return ActionResult(extracted_content=f"Downloads Directory: {download_dir}")

@controller.action('Get downloaded Excel file')
async def get_downloaded_excel(browser: Browser, download_dir: str = "./downloads") -> str:
    """
    Retrieves the most recently downloaded Excel file from the specified directory.
    Returns the path to the downloaded file.
    """
    # Get the most recently downloaded file
    files = list(Path(download_dir).glob("*.xlsx"))
    if not files:
        files = list(Path(download_dir).glob("*.xls"))
    
    if not files:
        return "No Excel file found in download directory."
    
    # Get the most recent file
    latest_file = max(files, key=lambda x: x.stat().st_mtime)
    return ActionResult(extracted_content=f"Downloaded file: {str(latest_file)}")

@controller.action('Analyze Excel file and return data')
def analyze_excel_file(file_path: str):
    """
    Reads an Excel file using pandas and returns the data as a dictionary.
    """
    if not os.path.exists(file_path):
        return json.dumps({"error": f"File not found: {file_path}"})
    
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Convert DataFrame to dictionary
        data = df.to_dict(orient='records')

        data_string = json.dumps({
            "row_count": len(data),
            "data": data
        })

        print(data_string)
        
        # Return the stringified data and some summary info
        return ActionResult(extracted_content=data_string)
    except Exception as e:
        return json.dumps({"error": f"Error reading Excel file: {str(e)}"})
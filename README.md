# AI-Agent
An AI agent that reads through a dataset and performs a web search to retrieve specific information for each entity in a chosen column.

Summary:
The project involves creating an AI agent that reads data from a CSV file or Google Sheets, performs web searches for specific information, and extracts relevant data using a Language Model (LLM). It includes building a Flask-based dashboard where users can upload files, define dynamic search queries with placeholders, and view or download the extracted results. The agent uses the Google Sheets API for data retrieval, SerpAPI for web searches, and OpenAI's GPT-3 for parsing and extracting information from search results, providing a user-friendly interface for efficient data extraction and organization.

Setup Instruction:
To set up the AI agent project, start by installing the necessary libraries using pip install pandas flask google-auth google-auth-oauthlib gspread requests openai. Then, configure the Google Sheets API by creating a project in Google Cloud Console, enabling the Sheets API, and obtaining a service account key. Save this key as a JSON file. Next, create a Flask application (app.py) with routes for uploading files, defining queries, and displaying results. Develop HTML templates for the interface (index.html, select_column.html, results.html). Integrate the Google Sheets API for data retrieval, SerpAPI for web searches, and OpenAI's GPT-3 for parsing results. Finally, run the Flask server with python app.py and access the application via your browser at http://127.0.0.1:5000/ to start interacting with the dashboard. This will enable you to upload CSV files, define search queries, and view or download the extracted information

APIs Used:
Google Sheets API:
Purpose: To connect and retrieve data from Google Sheets.
Usage: We used the google-auth and gspread libraries to authenticate and access Google Sheets.

SerpAPI:
Purpose: To perform web searches.
Usage: We used SerpAPI for gathering web search results based on user queries.

OpenAI GPT API:
Purpose: To parse web search results and extract specific information.
Usage: We used OpenAI's GPT-3 to interpret and extract the requested information from web search results.

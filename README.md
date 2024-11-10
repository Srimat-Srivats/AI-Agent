# AI-Agent
An AI agent that reads through a dataset and performs a web search to retrieve specific information for each entity in a chosen column.

Summary:
The project involves creating an AI agent that reads data from a CSV file or Google Sheets, performs web searches for specific information, and extracts relevant data using a Language Model (LLM). It includes building a Flask-based dashboard where users can upload files, define dynamic search queries with placeholders, and view or download the extracted results. The agent uses the Google Sheets API for data retrieval, SerpAPI for web searches, and OpenAI's GPT-3 for parsing and extracting information from search results, providing a user-friendly interface for efficient data extraction and organization.

Setup Instruction:
To set up the AI agent project, start by installing the necessary libraries using pip install pandas flask google-auth google-auth-oauthlib gspread requests openai. Then, configure the Google Sheets API by creating a project in Google Cloud Console, enabling the Sheets API, and obtaining a service account key. Save this key as a JSON file. Next, create a Flask application (app.py) with routes for uploading files, defining queries, and displaying results. Develop HTML templates for the interface (index.html, select_column.html, results.html). Integrate the Google Sheets API for data retrieval, SerpAPI for web searches, and OpenAI's GPT-3 for parsing results. Finally, run the Flask server with python app.py and access the application via your browser at http://127.0.0.1:5000/ to start interacting with the dashboard. This will enable you to upload CSV files, define search queries, and view or download the extracted information

Features:
This project features a user-friendly dashboard that allows users to upload CSV files or connect to Google Sheets, facilitating seamless data input and preview. Users can define dynamic queries with placeholders to tailor information retrieval to their specific needs. The AI agent performs automated web searches for each entity using the defined queries, leveraging web search APIs like SerpAPI. Advanced language models, such as OpenAI's GPT-3, are used to parse and extract the required information from the search results. The extracted data is displayed in an organized format on the dashboard, with options to download the results as a CSV file or update a Google Sheet. The integration of the Google Sheets API enables real-time access and updates to Google Sheets, enhancing efficiency. Additionally, the system includes robust error handling and API rate limiting mechanisms to ensure smooth and reliable operation. This comprehensive tool simplifies and accelerates the process of extracting valuable information from the web, making data collection and analysis more efficient and effective

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

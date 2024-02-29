# Insta-Unfollowers

This project is a simple web application built with Streamlit and Instaloader to help Instagram users identify accounts they follow but who don't follow them back. Users can input their Instagram credentials, and the application will retrieve the list of accounts they follow but who don't follow them back. The application also provides links to visit the profiles of these accounts directly from the interface.

## Key Features

- Checks for accounts followed but not following back.
- Provides clickable links to visit user profiles.

## Instructions for Use

1. Disable two-factor authentication for the Instagram account you wish to check.
2. Input your Instagram username and password into the provided fields.
3. Click the "Check" button to retrieve the list of accounts not following you back.
4. Review the results and click on usernames to visit their profiles directly.

## Note

- This application does not store your Instagram credentials.
- Avoid using this service for the same account multiple times in a day to prevent temporary bans.
- If the web application encounters issues, consider running the code locally on your PC.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/SiddhantDembi/Insta-Unfollowers.git
```

2. Install the required dependencies:
   
```bash
pip install -r requirements.txt
```

3. Run the application:

````bash
streamlit run data.py
````
  or 
````bash
python -m streamlit run data.py
````

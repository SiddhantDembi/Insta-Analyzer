# Insta-Analyzer

This project is a web application built with Streamlit to help Instagram users analyze their follower relationships. Users can upload their Instagram data in JSON format to identify accounts they follow but who don't follow them back (unfollowers), pending follow requests, and fans (accounts following them but not followed back).

## Key Features

- Unfollowers: Identifies users you follow who don't follow you back.
- Pending Follow Requests: Lists users you've sent follow requests to but haven't accepted yet.
- Fans: Lists users who follow you but whom you don't follow back.
- Provides clickable links to visit user profiles directly from the interface.

## Instructions for Use

1. Download your Instagram data from the Instagram app or website.
2. Choose the analysis you want to perform: Unfollowers, Requests Pending, or Fans.
3. Upload the required JSON files based on the selected option.
4. Review the results and click on usernames to visit their profiles directly.

## Note

- Ensure you upload the correct JSON files as specified for each option.
- This application does not store your JSON files.
- JSON Files Required: followers_1.json, following.json and pending_follow_requests.json.

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
streamlit run app.py
````


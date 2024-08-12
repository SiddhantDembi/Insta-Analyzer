import streamlit as st
import json

# Function to extract usernames and their URLs from the JSON file content
def extract_usernames_and_urls(file_content, key):
    data = json.load(file_content)
    if isinstance(data, dict):  # For following.json or pending_follow_requests.json
        user_list = [(entry['string_list_data'][0]['value'], entry['string_list_data'][0]['href']) for entry in data[key]]
    elif isinstance(data, list):  # For followers_1.json
        user_list = [(entry['string_list_data'][0]['value'], entry['string_list_data'][0]['href']) for entry in data]
    return user_list

# Streamlit UI
st.title("Instagram Analyzer")

# Show options for the different analyses
option = st.selectbox("Choose an option:", ["Select an option", "Unfollowers", "Requests Pending", "Fans"])

if option == "Unfollowers":
    # File upload for followers_1.json
    followers_file = st.file_uploader("Upload followers_1.json", type="json")
    # File upload for following.json
    following_file = st.file_uploader("Upload following.json", type="json")
    
    if followers_file and following_file:
        if followers_file.name != "followers_1.json":
            st.error("Please upload the correct file: followers_1.json")
        elif following_file.name != "following.json":
            st.error("Please upload the correct file: following.json")
        else:
            # Extract usernames and URLs
            followers = extract_usernames_and_urls(followers_file, key=None)  # followers_1.json has no key
            following = extract_usernames_and_urls(following_file, key="relationships_following")
            
            # Convert to dictionaries for easy lookup
            followers_dict = {user: url for user, url in followers}
            following_dict = {user: url for user, url in following}
            
            # Find users that are in following but not in followers
            not_following_back = [user for user in following_dict if user not in followers_dict]
            
            # Display results
            st.write("### List of users you are following but who are not following you back:")
            for i, user in enumerate(not_following_back, start=1):
                st.markdown(f"{i}. [{user}]({following_dict[user]})")

elif option == "Requests Pending":
    # File upload for pending_follow_requests.json
    pending_requests_file = st.file_uploader("Upload pending_follow_requests.json", type="json")
    
    if pending_requests_file:
        if pending_requests_file.name != "pending_follow_requests.json":
            st.error("Please upload the correct file: pending_follow_requests.json")
        else:
            # Extract usernames and URLs
            pending_requests = extract_usernames_and_urls(pending_requests_file, key="relationships_follow_requests_sent")
            
            # Display results
            st.write("### List of pending follow requests:")
            for i, (user, url) in enumerate(pending_requests, start=1):
                st.markdown(f"{i}. [{user}]({url})")

elif option == "Fans":
    # File upload for followers_1.json
    followers_file = st.file_uploader("Upload followers_1.json", type="json")
    # File upload for following.json
    following_file = st.file_uploader("Upload following.json", type="json")
    
    if followers_file and following_file:
        if followers_file.name != "followers_1.json":
            st.error("Please upload the correct file: followers_1.json")
        elif following_file.name != "following.json":
            st.error("Please upload the correct file: following.json")
        else:
            # Extract usernames and URLs
            followers = extract_usernames_and_urls(followers_file, key=None)  # followers_1.json has no key
            following = extract_usernames_and_urls(following_file, key="relationships_following")
            
            # Convert to dictionaries for easy lookup
            followers_dict = {user: url for user, url in followers}
            following_dict = {user: url for user, url in following}
            
            # Find users that are in followers but not in following
            fans = [user for user in followers_dict if user not in following_dict]
            
            # Display results
            st.write("### List of users who are following you but whom you don't follow back:")
            for i, user in enumerate(fans, start=1):
                st.markdown(f"{i}. [{user}]({followers_dict[user]})")

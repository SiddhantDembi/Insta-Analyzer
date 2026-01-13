import streamlit as st
import json

def extract_usernames_and_urls(file_content, key=None):
    data = json.load(file_content)
    user_list = []

    if isinstance(data, list):
        for entry in data:
            username = entry["string_list_data"][0]["value"]
            url = entry["string_list_data"][0]["href"]
            user_list.append((username, url))

    elif isinstance(data, dict):
        for entry in data[key]:
            username = entry["title"]
            url = entry["string_list_data"][0]["href"]
            user_list.append((username, url))

    return user_list


st.title("Instagram Analyzer")

option = st.selectbox("Choose an option:", ["Select an option", "Unfollowers", "Requests Pending", "Fans"])

if option == "Unfollowers":
    followers_file = st.file_uploader("Upload followers_1.json", type="json")
    following_file = st.file_uploader("Upload following.json", type="json")
    
    if followers_file and following_file:
        if followers_file.name != "followers_1.json":
            st.error("Please upload the correct file: followers_1.json")
        elif following_file.name != "following.json":
            st.error("Please upload the correct file: following.json")
        else:
            followers = extract_usernames_and_urls(followers_file)
            following = extract_usernames_and_urls(following_file, key="relationships_following")
            
            followers_dict = {user: url for user, url in followers}
            following_dict = {user: url for user, url in following}
            
            not_following_back = [user for user in following_dict if user not in followers_dict]
            
            st.write("### List of users you are following but who are not following you back:")
            for i, user in enumerate(not_following_back, start=1):
                st.markdown(f"{i}. [{user}]({following_dict[user]})")

elif option == "Requests Pending":
    pending_requests_file = st.file_uploader("Upload pending_follow_requests.json", type="json")
    
    if pending_requests_file:
        if pending_requests_file.name != "pending_follow_requests.json":
            st.error("Please upload the correct file: pending_follow_requests.json")
        else:
            pending_requests = extract_usernames_and_urls(
                pending_requests_file, 
                key="relationships_follow_requests_sent"
            )
            
            st.write("### List of pending follow requests:")
            for i, (user, url) in enumerate(pending_requests, start=1):
                st.markdown(f"{i}. [{user}]({url})")

elif option == "Fans":
    followers_file = st.file_uploader("Upload followers_1.json", type="json")
    following_file = st.file_uploader("Upload following.json", type="json")
    
    if followers_file and following_file:
        if followers_file.name != "followers_1.json":
            st.error("Please upload the correct file: followers_1.json")
        elif following_file.name != "following.json":
            st.error("Please upload the correct file: following.json")
        else:
            followers = extract_usernames_and_urls(followers_file)
            following = extract_usernames_and_urls(following_file, key="relationships_following")
            
            followers_dict = {user: url for user, url in followers}
            following_dict = {user: url for user, url in following}
            
            fans = [user for user in followers_dict if user not in following_dict]
            
            st.write("### List of users who are following you but whom you don't follow back:")
            for i, user in enumerate(fans, start=1):
                st.markdown(f"{i}. [{user}]({followers_dict[user]})")

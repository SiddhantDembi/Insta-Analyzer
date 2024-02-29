import streamlit as st
import instaloader
from instaloader.exceptions import ConnectionException, TwoFactorAuthRequiredException

def get_followers_and_following(username, password):
    L = instaloader.Instaloader()

    try:
        L.login(username, password)  # Login with your Instagram credentials

        # Load profile
        profile = instaloader.Profile.from_username(L.context, username)

        # Initialize lists for followers and following
        followers = []
        following = []

        # Get followers
        for follower in profile.get_followers():
            followers.append(follower.username)

        # Get following
        for followee in profile.get_followees():
            following.append(followee.username)

        # Calculate people whom you follow but who don't follow you back
        not_followers_back = list(set(following) - set(followers))

        return not_followers_back
    except TwoFactorAuthRequiredException:
        raise ValueError("Login error: Disable two-factor authentication")
    except ConnectionException as e:
        raise ValueError("Login error: " + str(e))

def main():
    st.title("Instagram UnFollower Checker")
    st.write("1. Two-factor authentication should be disabled for this to work.")
    st.write("2. Do not use this service for the same account more than once in a day. Too many requests can result in temporary ban of your account.")
    st.write("3. Your username and password won't be stored in any database.")
    st.write("4. If the web-app does not work, run the code locally on your PC.")
    st.markdown("[GitHub](https://github.com/SiddhantDembi/Insta-Unfollowers)")
    st.write("Enter your Instagram credentials below:")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Check"):
        if not username or not password:
            st.error("Please enter your username and password.")
        else:
            try:
                not_followers_back = get_followers_and_following(username, password)
                st.write("People whom you follow but who don't follow you back:")
                st.write("Click on the username to visit their profile.")
                for user in not_followers_back:
                    # Display the username as a clickable hyperlink
                    st.markdown(f"[{user}](https://www.instagram.com/{user})")
            except ValueError as e:
                st.error(str(e))

if __name__ == "__main__":
    main()

import requests
import base64
from urllib.parse import urlparse, parse_qs
import datetime
import os
from dotenv import load_dotenv, set_key

# Define a class to hold Spotify configuration information
class SpotifyConfig:
    def __init__(self, client_id, client_secret, redirect_uri, scopes):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scopes = scopes

    # Load Spotify configuration from environment variables or user input
    def load_config(self):
        load_dotenv()

        existing_client_id = os.getenv("SPOTIFY_CLIENT_ID")
        existing_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        existing_redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

        if existing_client_id:
            update_client_id = input(f"Existing Spotify Client ID found: {existing_client_id}. Do you want to update it? (y/n): ")
            if update_client_id.lower() == 'y':
                self.client_id = input("Enter your updated Spotify Client ID: ")
            else:
                self.client_id = existing_client_id
        else:
            self.client_id = input("Enter your Spotify Client ID: ")

        if existing_client_secret:
            update_client_secret = input(f"Existing Spotify Client Secret found. Do you want to update it? (y/n): ")
            if update_client_secret.lower() == 'y':
                self.client_secret = input("Enter your updated Spotify Client Secret: ")
            else:
                self.client_secret = existing_client_secret
        else:
            self.client_secret = input("Enter your Spotify Client Secret: ")

        if existing_redirect_uri:
            update_redirect_uri = input(f"Existing Redirect URI found: {existing_redirect_uri}. Do you want to update it? (y/n): ")
            if update_redirect_uri.lower() == 'y':
                self.redirect_uri = input("Enter your updated Redirect URI: ")
            else:
                self.redirect_uri = existing_redirect_uri
        else:
            self.redirect_uri = input("Enter your Redirect URI: ")

    # Generate the Spotify authorization URL
    def generate_authorization_url(self):
        AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
        return f"{AUTHORIZE_URL}?client_id={self.client_id}&response_type=code&scope={self.scopes}&redirect_uri={self.redirect_uri}"

    # Get the authorization code from the user
    @staticmethod
    def get_authorization_code():
        authorization_url = input("Paste the entire URL from your browser's address bar: ")
        parsed_url = urlparse(authorization_url)
        query_params = parse_qs(parsed_url.query)
        return query_params.get("code", [])[0]

    # Exchange the authorization code for an access token
    def exchange_authorization_code_for_token(self, authorization_code):
        TOKEN_URL = "https://accounts.spotify.com/api/token"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {base64.b64encode((self.client_id + ':' + self.client_secret).encode()).decode()}"
        }

        data = {
            "grant_type": "authorization_code",
            "code": authorization_code,
            "redirect_uri": self.redirect_uri
        }

        response = requests.post(TOKEN_URL, headers=headers, data=data)

        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data["access_token"]
            refresh_token = token_data["refresh_token"]
            expires_in = token_data["expires_in"]
            expiration_time = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)

            self.save_tokens_to_env(access_token, refresh_token, expiration_time)
        else:
            print("Failed to obtain an access token. Status code:", response.status_code)
            return None

    # Save tokens and configuration details to .env file
    def save_tokens_to_env(self, access_token, refresh_token, expiration_time):        
        set_key(".env", "SPOTIFY_CLIENT_ID", self.client_id)
        set_key(".env", "SPOTIFY_CLIENT_SECRET", self.client_secret)
        set_key(".env", "SPOTIFY_REDIRECT_URI", self.redirect_uri)
        set_key(".env", "SPOTIFY_ACCESS_TOKEN", access_token)
        set_key(".env", "SPOTIFY_REFRESH_TOKEN", refresh_token)
        set_key(".env", "SPOTIFY_TOKEN_EXPIRATION", str(expiration_time.timestamp()))

        print("Access and Refresh Tokens generated and saved to .env file.")
        print("Token will expire at:", expiration_time.strftime("%Y-%m-%d %H:%M:%S"))

def main():
    config = SpotifyConfig(
        client_id=None,
        client_secret=None,
        redirect_uri=None,
        scopes="user-read-recently-played"  # You can parameterize this
    )

    config.load_config()
    auth_url = config.generate_authorization_url()
    print(f"Please log in to Spotify and authorize the app by visiting the following URL:\n{auth_url}")
    authorization_code = config.get_authorization_code()

    if authorization_code:
        config.exchange_authorization_code_for_token(authorization_code)

if __name__ == "__main__":
    main()
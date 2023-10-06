# 🎵 Spotify Authorization Script 🎵

**Simplify Spotify API Authentication for Your Projects**

While developing a personal project involving the Spotify's API, I struggled using Apache Airflow for an automated ETL (Extract, Transform, Load) - STAY TUNED!. One of the initial hurdles was navigating the Spotify API's complex authentication process, a flow especially challenging for beginners.

This Python script serves as a solution to streamline the authentication process, making it more accessible for novice developers. It not only simplifies authentication but also helps you manage your Spotify application's credentials and tokens.

For detailed information on the authentication flow, you can refer to the [official Spotify documentation](https://developer.spotify.com/documentation/web-api/tutorials/code-flow).

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
  - [SpotifyConfig Class](#spotifyconfig-class)
    - [Constructor](#constructor)
    - [load_config Method](#load_config-method)
    - [generate_authorization_url Method](#generate_authorization_url-method)
    - [get_authorization_code Method](#get_authorization_code-method)
    - [exchange_authorization_code_for_token Method](#exchange_authorization_code_for_token-method)
    - [save_tokens_to_env Method](#save_tokens_to_env-method)
  - [Main Function](#main-function)
- [Contributing](#contributing)

## Introduction

This script simplifies the Spotify API authorization flow by handling the following tasks:

- Loading and managing Spotify application configuration.
- Generating the Spotify authorization URL for user login.
- Extracting the authorization code from the browser's URL.
- Exchanging the authorization code for access and refresh tokens.
- Saving the obtained tokens and configuration details to a `.env` file that can be safely used for other projects.

## Prerequisites

Before using this script, ensure that you have the following prerequisites:

- Python 3 installed on your system.
- Spotify Developer Account: You need to register your application with Spotify and obtain a Client ID and Client Secret. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) to create your Spotify application. 

## Installation

1. Clone or download this repository to your local machine.

2. Install the required Python packages using pip:

   ```bash
   pip install requests base64 urllib3 datetime python-dotenv
   ```

3. (OPTIONAL) Create a `.env` file in the same directory as the script to store your Spotify application credentials and tokens.

   ```
   # .env file
   SPOTIFY_CLIENT_ID=
   SPOTIFY_CLIENT_SECRET=
   SPOTIFY_REDIRECT_URI=
   SPOTIFY_ACCESS_TOKEN=
   SPOTIFY_REFRESH_TOKEN=
   SPOTIFY_TOKEN_EXPIRATION=
   ```

## Usage

1. Run the script using the following command:

   ```bash
   python spotify_auth.py
   ```

2. The script will prompt you to enter or update your Spotify application credentials (Client ID, Client Secret, and Redirect URI) if they are not already present in the `.env` file.

3. Follow the provided URL to log in to your Spotify account and authorize the application.

4. After authorization, copy and paste the URL from your browser address bar and the script will automatically retrieve and save the access and refresh tokens to the `.env` file.

5. You can now use the obtained access token to make authenticated requests to the Spotify API.

## Documentation

### SpotifyConfig Class

#### Constructor

- `SpotifyConfig(client_id, client_secret, redirect_uri, scopes)`: Initializes a SpotifyConfig object with your Spotify application credentials and the desired scopes.

#### load_config Method

- `load_config()`: Loads the Spotify configuration from environment variables or user input, allowing you to update credentials interactively.

#### generate_authorization_url Method

- `generate_authorization_url()`: Generates the Spotify authorization URL based on your configuration.

#### get_authorization_code Method

- `get_authorization_code()`: Prompts the user to paste the authorization code from their browser's address bar and returns it.

#### exchange_authorization_code_for_token Method

- `exchange_authorization_code_for_token(authorization_code)`: Exchanges the authorization code for an access token and a refresh token.

#### save_tokens_to_env Method

- `save_tokens_to_env(access_token, refresh_token, expiration_time)`: Saves the obtained tokens and configuration details to the `.env` file.

### Main Function

- `main()`: The entry point of the script. It initializes a SpotifyConfig object, loads configuration, generates the authorization URL, and handles the authorization flow.

## Contributing

Contributions to this project are welcome! Feel free to submit issues or pull requests on the GitHub repository.

---

Enjoy using the Spotify Authorization Script! 🎶🎉

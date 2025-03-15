# Setting Up the Procore API

### 📝 Introduction 
   This guide provides step-by-step instructions for setting up and using the Procore API to access construction management data and manage projects programmatically.

### 📡 Prerequisites 
   Before you can use the Procore API, ensure you have the following:

   1. **Procore Account**: You need to create a Procore developer account if you don't already have one. Visit [Procore](https://developers.procore.com/) to sign up.

   2. **App**: Log in to the Procore Developer Portal. Navigate to My Apps and click Create New App. Provide a meaningful app name base on your usecase. Click Create App to proceed.

### 🔑 Generating an Access Token 

   To interact with the Procore API, you need to generate an access token. Follow these steps:

   1. **Add a Data Connector Component**: 
        * Click the down arrow to expand the Data Connector Components section.
        * Select Add Components.
        * On the right-hand side, select User Level Authentication.
        * Click Save Component at the bottom-right of the side panel.
        * Click Create Version in the near the top right then follow the prompts.

   2. **Update Your App’s URIs**: It's essential to note that this specific redirect URI is meant for testing purposes only.
        * In your app, select OAuth Credentials on the left-hand side.
        * Under Sandbox OAuth Credentials, click into the Redirect URI field.
        * In this field, paste the following text: urn:ietf:wg:oauth:2.0:oob
        * Click Update in the bottom right corner

> **Note**: You can omit the above step if you have access to an existing account.

   3. **Access Your Client ID and Secret**: 
      - After creating the app, go to the MyApp section and  navigate to the overview section of your app. Here, you will find your **Client ID** and **Client Secret**.

   4. **Obtain Your Access Token**: 
      - Switch to the second section of your app named settings. You will find your **Access Token** here. This token is required for making authorized requests to the Procore API.
      - Copy the access token and store it securely, as you will need it for your API calls.




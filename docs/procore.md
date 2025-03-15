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

   3. **Install Your App in the Sandbox**: Every created app comes with a Developer Sandbox intended to be your primary testing environment. To access the Developer Sandbox, check your email inbox for a message prompting you to create a password. Additionally, you can find the URL to your Sandbox by navigating to the Sandbox OAuth Credentials section of your app.

        * Log into your Developer Sandbox and select the corresponding Company
        * Select Company Tools at the top, then click on the Admin tool.
        * On the right-hand side, click App Management.
        * Click Install App and choose Install Custom App.
        * Paste the previously copied App Version Key.
        * Click Install.
        * Click Install again to confirm the installation.


   4. **Generate a Code for User Authentication**: Now that your app is installed, we need to generate a code, which will be exchanged for an access token.

        * In the following URL, replace the CLIENT_ID variable with that of your Sandbox Credentials, which can be found in your app through the Developer Portal: https://login-sandbox.procore.com/oauth/authorize?response_type=code&client_id=CLIENT_ID&redirect_uri=urn:ietf:wg:oauth:2.0:oob
        * Open the edited URL in your web browser.
        * This may prompt you to log in, if you are already not signed into Procore.
        * Additionally, you may have to select Approve if the app is accessing your information for the first time.
        * Once successfully done, copy the code value as it’s required for the next step.

  5. **Exchange the Code for an Access Token**: To retrieve an access token, you’ll exchange the code for a token using Postman or curl:

        * In Postman, create a POST request to: https://login-sandbox.procore.com/oauth/token/.
        * Add the following to the Body as x-www-form-urlencoded:
        * grant_type: authorization_code
        * code: Your authorization code (from Step 5).
        * client_id: Your app’s Client ID.
        * client_secret: Your app’s Client Secret.
        * redirect_uri: urn:ietf:wg:oauth:2.0:oob.
        * Click Send.
        * If successful, you’ll receive a response containing your access token similar to the example below:

        ```
        { "access_token": "####", "token_type": "bearer","expires_in": 5400, "refresh_token": "####","created_at": 1508271900} 
        ```





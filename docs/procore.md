# Setting Up the Procore API

### 📝 Introduction 
   This guide provides step-by-step instructions for setting up and using the Procore API to access construction management data and manage projects programmatically.

### 📡 Prerequisites 
   Before you can use the Procore API, ensure you have the following:

   1. **Procore Account**: You need to create a Procore developer account if you don't already have one. Visit [Procore](https://developers.procore.com/) to sign up.

   2. **App**: Log in to the Procore Developer Portal. Navigate to My Apps and click Create New App. Provide a meaningful app name base on your usecase. Click Create App to proceed.

### 🔑 Generating an Access Token 

   To interact with the Procore API, you need to generate an access token. Follow these steps:

   1. **Log In to the Procore Developer Portal**: Go to the [Procore Developer Portal](https://developer.surveymonkey.com/) and log in with your existing Procore account credentials.

   2. **Create a New App**: 
      - Click on the option to create a new app. You can choose to create either a **Public** or **Private** app based on your use case. 
      - Public apps are suitable for applications that will be used by multiple users, while private apps are intended for personal use or limited distribution.

> **Note**: You can omit the above step if you have access to an existing account.

   3. **Access Your Client ID and Secret**: 
      - After creating the app, go to the MyApp section and  navigate to the overview section of your app. Here, you will find your **Client ID** and **Client Secret**.

   4. **Obtain Your Access Token**: 
      - Switch to the second section of your app named settings. You will find your **Access Token** here. This token is required for making authorized requests to the Procore API.
      - Copy the access token and store it securely, as you will need it for your API calls.




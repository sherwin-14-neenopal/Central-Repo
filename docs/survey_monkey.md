# Setting Up the SurveyMonkey API

### 📝 Introduction 
   This guide provides step-by-step instructions for setting up and using the SurveyMonkey API to access survey data and manage surveys programmatically.

### 📡 Prerequisites 
   Before you can use the SurveyMonkey API, ensure you have the following:

   1. **SurveyMonkey Account**: You need to create a SurveyMonkey account if you don't already have one. Visit [SurveyMonkey](https://www.surveymonkey.com/) to sign up.

   2. **Survey with Responses**: Create at least one survey that includes responses. This survey will be used to test the API functionality. For creating surveys refer to this [link](https://www.youtube.com/watch?v=l-Vfhevy7g0). 

> **Note**: If you are given access to an existing account then you can skip the above step and move to the next section.

### 🔑 Generating an Access Token 

   To interact with the SurveyMonkey API, you need to generate an access token. Follow these steps:

   1. **Log In to the SurveyMonkey Developer Portal**: Go to the [SurveyMonkey Developer Portal](https://developer.surveymonkey.com/) and log in with your existing SurveyMonkey account credentials.

   2. **Create a New App**: 
      - Click on the option to create a new app. You can choose to create either a **Public** or **Private** app based on your use case. 
      - Public apps are suitable for applications that will be used by multiple users, while private apps are intended for personal use or limited distribution.

> **Note**: You can omit the above step if you have access to an existing account.

   3. **Access Your Client ID and Secret**: 
      - After creating the app, go to the MyApp section and  navigate to the overview section of your app. Here, you will find your **Client ID** and **Client Secret**.

   4. **Obtain Your Access Token**: 
      - Switch to the second section of your app named settings. You will find your **Access Token** here. This token is required for making authorized requests to the SurveyMonkey API.
      - Copy the access token and store it securely, as you will need it for your API calls.

### 🔍 Choosing Scopes

   When generating an access token, it's important to select the appropriate scopes that define the permissions your application will have when accessing the SurveyMonkey API. Follow these steps:

   1. **Navigate to the Scopes Section**: In the app settings, look for the section where you can define the scopes for your access token.

   2. **Select Appropriate Scopes**: Choose the scopes that align with the functionality you need for your application. Common scopes include:
      - **`surveys`**: Access to survey data.
      - **`collectors`**: Manage collectors for your surveys.
      - **`responses`**: Access to survey responses.
      - **`users`**: Access to user information.

   3. **Understand Scope Implications**: Be selective about the permissions you grant. Only choose the scopes that are relevant and useful for your purpose. This practice not only enhances the security of user data but also aligns with best practices.

   4. **Save Your Changes**: After selecting the desired scopes, make sure to click on update scopes button. Your access token will now have the permissions associated with the scopes you selected. You can now make requests to the various endpoints and retrieve data related to surveys, responses, and collectors etc.


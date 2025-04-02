# Setting Up the Youtube Analytics API

### 📝 Introduction 

This guide provides step-by-step instructions for setting up and using the YouTube Analytics API to access video performance data and manage YouTube channels programmatically.

### 📡 Prerequisites 
   
Before you can use the Youtube Analytics API, ensure you have the following:

1. **Create a Project in Google Developer Console**: You need to create a project in google developer console, if you don't already have one. You can follow this [tutorial](https://www.youtube.com/watch?v=7n9DkOzjwlA) to create a project.

2. **Enable Youtube Analytics API**: To enable the required APIs, navigate to the "APIs & Services" menu and select "Library." Use the search bar to locate the Youtube Analytics API, then select it and click the "Enable" button.

### 🔐 Setting Up OAuth

To interact with the Youtube Analytics API, you need to generate a `credentials.json` file. Follow these steps:

1. **Set Up The App**: To set up the application, click on the option `OAuth consent screen` in the "APIs & Services" section. After that choose a user type and fill relevant information about the app.

2. **Get Oauth Credentials**: After creating the app, click on `Credentials` section. Navigate to "Create credentials" and then choose `Oauth Client ID`. Choose the application type and click on create, this will prompt you to download your `CLIENT_ID` and `CLIENT_SECRET` in json format. After doing all of these, just rename the file as `credentials.json` so as to maintain brevity.
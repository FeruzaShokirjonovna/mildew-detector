# <h1 align="center">**Mildew Detector**</h1>

## Introduction

The Mildew Detector dashboard application utilizes Machine Learning technology to allow users to upload images of cherry leaves for analysis. It assesses whether the cherry leaves is healthy or afflicted with powdery mildew, providing users with a downloadable report summarizing the findings.

![Home Screen](/static/images/amIresponsive.png)

### Deployed version at [Plant Disease Classification](https://mildew-detector-app-84798b6ec62b.herokuapp.com/)

## Table of Contents

- [Dataset Content](#dataset-content)
- [Business Requirements](#business-requirements)
- [Hypotheses and how to Validate](#hypotheses-and-how-to-validate)
- [Rational to Map Business Requirements](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [User Stories](#user-stories)
- [Dashboard Design](#dashboard-design---streamlit-app-user-interface)
- [Methodology](#methodology)
- [Rationale for the Model](#rationale-for-the-model)
- [Project Features](#project-features)
- [Project Outcomes](#project-outcomes)
- [Hypothesis Outcomes](#hypothesis-outcomes)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Languages and Libraries](#languages-and-libraries)
- [Credits](#credits)

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). Then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.


## Business Requirements
- The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.

- To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project to all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


    * 1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.
    * 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.
    * 3 - The client would like to receive some treatment suggestions based on the plant disease.


## Hypothesis and how to validate?
1. The identification of cherry leaves affected by powdery mildew from healthy leaves can be achieved through visual examination of their distinct appearances.
   - This can be confirmed through the creation of an average image study and image montage, allowing for a comparative analysis of the appearance differences between healthy leaves and those affected by powdery mildew.
2. The determination of cherry leaves as healthy or afflicted with powdery mildew can be accomplished with a confidence level of 97% accuracy. 
   - This assertion can be substantiated by assessing the model's performance on the test dataset, aiming for a minimum accuracy rate of 97%.
3. The model's prediction accuracy may be compromised if the images of cherry leaves contain backgrounds different from the beige background of the Kaggle dataset. 
   - Confirm this limitation, the model should be tested with new pictures of cherry leaves featuring backgrounds distinct from those in the dataset images.
4. It is advisable to use images in RGB mode for improved prediction accuracy. Nevertheless, if images are not already in RGB mode, the trained model will automatically convert them to RGB mode for processing.
The outcome of the validation can be found on the live dashboard on the page "Project Hypotheses".


## The rationale to map the business requirements to the Data Visualizations and ML tasks
- Business Requirement 1: Data Visualization

  - The dashboard will showcase the 'mean' and 'standard deviation' images for both healthy and powdery mildew-infected cherry leaves.
  - Additionally, it will display the contrast between an average healthy leaf and an average leaf infected with powdery mildew.
  - Furthermore, an image montage featuring healthy leaves, leaves affected by powdery mildew will be presented for comparison.

- Business Requirement 2: Classification

  - Create and fit a machine learning model to predict if a given leaf is healthy or infected with powdery mildew. This will be a classification task with three classes and will require to set the image shape.
  - The model provides treatment recommendations to users based on the type of plant disease identified.
  - The predictions should have a 97% accuracy level.
  
- Business Requirement 3: Report
  - A downloadable report containing the predicted status of all uploaded images is available for users.

## ML Business Case
- To create a machine learning model for cherry leaf classification, particularly distinguishing between healthy leaves and those infected with powdery mildew, typically the following steps are followed:

1. Data Collection: Gather a dataset containing images of leaves categorized as healthy and powdery mildew-infected. Ensure each category is well-represented in the dataset.

2. Data Preprocessing: Preprocess the images to ensure uniformity in size, color space, and quality. This step may involve resizing, normalization, and augmentation techniques to enhance the dataset's diversity.

3. Feature Extraction: Use techniques like convolutional neural networks (CNNs) to extract meaningful features from the images. CNNs are particularly effective for image classification tasks due to their ability to capture spatial hierarchies.

4. Model Selection: Choose an appropriate machine learning model architecture for classification. Common choices for image classification tasks include CNN-based architectures.

5. Model Training: Split the dataset into training and validation sets. Train the selected model on the training set while validating its performance on the validation set. Fine-tune hyperparameters to optimize the model's performance.

6. Model Evaluation: Evaluate the trained model's performance using appropriate evaluation metrics on the validation set.

7. Model Testing: Once satisfied with the model's performance, test it on a separate test dataset to assess its generalization ability. This step ensures that the model can accurately classify unseen data.

8. Deployment: Deploy the trained model into production, making it available for inference on new leaf images. Integrate the model into an application or system where users can upload leaf images and receive predictions on their health status.

9. Monitoring and Maintenance: Continuously monitor the model's performance in production and update it periodically with new data to ensure its effectiveness over time.

- The training data is a [Kaggle dataset](https://www.kaggle.com/codeinstitute/cherry-leaves) with over 4k images of healthy and affected cherry leaves. 

## User Stories

- As a client I require an intuitive dashboard for easy navigation, allowing me to effortlessly access and comprehend data, models, and outcomes.
- As a client I need the capability to observe average and variable images of both healthy cherry leaves and those infected with powdery mildew. This feature will enable me to visually distinguish between the two categories.
- As a client I seek the ability to view a visual montage comprising images of healthy cherry leaves and those infected with powdery mildew. This feature will facilitate a clearer differentiation between the three classifications.
- As a client I desire the functionality to upload images of cherry leaves and receive classification predictions with an accuracy exceeding 97%. This will allow for swift assessment of cherry tree health based on the provided predictions.
- As a client I require treatment suggestions based on identified plant diseases to effectively address any issues affecting my plants' health.
- As a client I require the facility to download a report containing the provided predictions, ensuring that I have a record of the outcomes for future reference.


## Dashboard Design
### Page 1: Quick Project Summary

- Provide an overview of powdery mildew, accompanied by sample images for illustration.
- Outline the specifics of the dataset utilized in the project.
- Define the business requirements.
- Include a hyperlink to access this Readme file.

### Page 2: Plant leaves Visualizer

- This page is designed to meet Business Requirement 1 by showcasing the following:
  - Illustrating the disparity between the average and variability image.
  - Displaying the contrast between average healthy leaves and leaves infected with powdery mildew.
  - Presenting an image montage featuring for healthy leaves and leaves infected with powdery mildew.

### Page 3: Plant Diseases Detector

- This page is designed to meet Business Requirements 2 and 3, offering the following features:
  - Prediction of whether a leaf is infected with powdery mildew.
  - Provision of a link to download a set of images displaying healthy leaves and leaves infected with powdery mildew for live prediction.
  - User Interface featuring a file uploader widget for multiple leaf image uploads. It displays each uploaded image along with a prediction statement indicating if the leaf is infected with powdery mildew, along with the associated probability.
  - In addition to uploading images directly from their device, users can also copy and paste image URL(s) from external sources for live prediction.
  - Generation of a report containing image names and prediction results.
  - Offering treatment recommendations tailored to plant disease.
  - Download button provided to download the generated report.

### Page 4: Project Hypothesis and Validation

- Detail each [hypotheses](#hypotheses-and-how-to-validate), how it was validated and the conclusion.

### Page 5: Machine Learning Performance Metrics

- Providing comprehensive details on the model performance, including:
  - Label frequencies for the training, validation, and test sets.
  - Model history depicting accuracy and losses during training.
  - Evaluation results of the model's performance.
  - Offering metrics that demonstrate the performance of the model.



## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people that provided support through this project.


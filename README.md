# AlzheimersAI
### [![Build Status](https://travis-ci.com/safinsingh/AlzheimersAI.svg?token=3fbJg9w6ZsQzZoBT4nKJ&branch=master)](https://travis-ci.com/safinsingh/AlzheimersAI) [![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)


A website for early detection and tracking of Alzheimer's disease. The live link is [https://alzheimersai.tk/](https://alzheimersai.tk/)

To run locally, clone the repository and run `npm install -g firebase-tools` and then `firebase serve` in your terminal.

<p>AlzheimersAI is a Firebase-hosted Flask app running inside a Google Cloud Run Docker container. It combines quiz results with a FastAI Convolution Neural Network analysis of the users' brain scan to produce a value for the user's Alzheimers Index. It enables family members to keep track of the user's condition through the use of charts and diagrams produced by Chart.JS. Caregives can also fill out a user profile for the patient to refer to in case they forget something. The site stores this data by interacting with the Firestore database service and can successfully authenticate users and save data. The languages used to create this site include <code>HTML</code>, <code>CSS</code>, <code>JavaScript</code>, <code>jQuery</code>, <code>YAML</code>, <code>Batch</code>, <code>Shell (zsh)</code>, <code>Jupyter Notebook</code>, and <code>Python</code>. It takes advantage of the <code>Flask</code>, <code>FastAI</code>, <code>Pandas</code>, <code>NumPy</code>, <code>PyTorch</code>, <code>Node.JS</code>, <code>Chart.JS</code>, <code>Visual Studio Code Live Share</code>, <code>Travis-CI</code>, and <code>Bootstrap</code> libraries. The data use to train the model can found on <a href="https://www.kaggle.com/tourist55/alzheimers-dataset-4-class-of-images">Kaggle</a>. Travis-CI is integrated with Google Cloud Run, Docker, and Node.JS to automatically build the Docker image and deploy to Firebase Hosting whenever a new change is committed. Bootstrap streamlines responsiveness on the page, allowing it to work seamlessly on mobile devices. The code itself was written in the Visual Studio Code IDE with Live Share integration for increased productivity and collaboration.</p>

A diagram of how our content is served can be found below: 
![alt text](/static/assets/nt_diagram.png)

For more information on our AI and our AI library, please check out the AI folder and our [Wiki](https://github.com/safinsingh/AlzheimersAI/wiki)

Video Demo: [https://youtu.be/DBsy2l8raws](https://youtu.be/DBsy2l8raws)<br>
DevPost: [https://devpost.com/software/alzheimersai](https://devpost.com/software/alzheimersai)<br>
Presentation: [https://bit.ly/2yLpoEC](https://bit.ly/2yLpoEC)<br>

Creators: Aadit Gupta, Raadwan Masum, Safin Singh, and Rohan Juneja
# Sign-Language-Detection-using-Python-and-OpenCV

## steps to run the flask  application :

1. go to the folder named Flask_application.
2. open the terminal in that folder location.
3. run the command "python App.py". If this command doesn't work try running "python3 App.py".
4. you can see a link in the terminal, open that link in chrome.
5. This opens the url in the browser, which contains an option to open the webcam
6. Give the sign laguage gestures using hand to see the intant results displayed on the screen. Below attached is the reference for signs.
![image](https://user-images.githubusercontent.com/65344410/235353907-235522cc-1919-4ac6-9f8b-5869617bccc7.png)

## Steps to include new signs and intents :
Althouh above model is trained to detect 24 Alphabets, you can also include the symbols of your choice snd train the model - Example : Numbers, symbols of Objects, etc
Follow these steps to give your custom input:

Overview: First, we give the input using openCV. We move our hands in front of the camera, and the camera captures the frames from different angles through the motion of our hands(Using mediapipe). This creates its own database for our model. In this process, the model segregates our hands and gestures from the whole picture.  Using the created dataset, the ML model gets trained; here, I used a Random Forest Classifier for simplicity. Also, this model gave almost 100% accuracy. After training using our custom dataset, we can give real-time inputs and convert them into corresponding texts.

Step-by-step process:
For step by step process follow this documents : https://docs.google.com/document/d/1-dPvvIr6b0jqolnhQ6e-tdkN0kEAzLJOD4aN49egt5k/edit?usp=sharing

         




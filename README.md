<p align="left">
  <img src="https://user-images.githubusercontent.com/125717930/225975240-24b9a8ad-8cc6-4d5f-9a91-1435951b0bd7.png" width="120" alt="Nest Logo" />
</p>

👏  We have published the Face Liveness Detection, Face Recognition SDK and ID Card Recognition SDK for the server.

  - [FaceLivenessDetection-Docker](https://github.com/kby-ai/FaceLivenessDetection-Docker)

  - [FaceLivenessDetection-Windows](https://github.com/kby-ai/FaceLivenessDetection-Windows)

  - [FaceRecognition-Docker](https://github.com/kby-ai/FaceRecognition-Docker)

  - [FaceRecognition-Windows](https://github.com/kby-ai/FaceRecognition-Windows)

  - [IDCardRecognition-Docker](https://github.com/kby-ai/IDCardRecognition-Docker)

# FaceLivenessDetection-Windows
## Introduction
This is the face liveness detection demo project for windows.

> The demo is integrated with KBY-AI's Face Liveness Detection Server SDK.

> We can customize the SDK to align with your specific requirements.

  | Features      |
  |------------------|
  | Face Detection        |
  | Face Liveness Detection        |
  | Pose Estimation        |
  | 68 points Face Landmark Detection        |
  | Face Quality Calculation        |
  | Face Occlusion Detection        |
  | Eye Closure Detection        |
  | Mouth Opening Check        |
 
> For other solutions, please explore the following:
> - [Face Liveness Detection - Android(Basic SDK)](https://github.com/kby-ai/FaceLivenessDetection-Android)
> - [Face Liveness Detection - iOS(Basic SDK)](https://github.com/kby-ai/FaceLivenessDetection-iOS)
> - [Face Recognition - Android(Standard SDK)](https://github.com/kby-ai/FaceRecognition-Android)
> - [Face Recognition - iOS(Standard SDK)](https://github.com/kby-ai/FaceRecognition-iOS)
> - [Face Recognition - Flutter(Standard SDK)](https://github.com/kby-ai/FaceRecognition-Flutter)
> - [Face Attribute - Android(Premium SDK)](https://github.com/kby-ai/FaceAttribute-Android)
> - [Face Attribute - iOS(Premium SDK)](https://github.com/kby-ai/FaceAttribute-iOS)

## Try the API
### Online Demo
  You can test the SDK using images from the following URL:
  https://web.kby-ai.com
  
  ![image](https://github.com/kby-ai/FaceLivenessDetection-Docker/assets/125717930/4fd2c1ca-3552-4c6e-b8c2-4a12d7c92ca6)

### Postman
  To test the API, you can use Postman. Here are the endpoints for testing:
  - Test with an image file: Send a POST request to http://18.221.33.238:8080/check_liveness.
  - Test with a base64-encoded image: Send a POST request to http://18.221.33.238:8080/check_liveness_base64.

    You can download the Postman collection to easily access and use these endpoints. [click here](https://github.com/kby-ai/FaceLivenessDetection-Docker/blob/main/postman/kby-ai-live.postman_collection.json)
    
    ![image](https://github.com/kby-ai/FaceLivenessDetection-Docker/assets/125717930/b24b1145-08af-46ca-8ffa-65aa020749b4)


## SDK License

This project uses KBY-AI's Face Liveness Detection Server SDK, which requires a license per machine.

- The code below shows how to use the license: https://github.com/kby-ai/FaceLivenessDetection-Windows/blob/e7ffeecc21f6053828a744e127ddef2e8a34c4a2/test.py#L32-L44

- In order to request the license, please provide us with the machine code obtained from the "getMachineCode" function.

  Please contact us:
  ```
  Email: contact@kby-ai.com

  Telegram: @kbyai

  WhatsApp: +19092802609

  Skype: live:.cid.66e2522354b1049b
  
## How to run

> We have not published facesdk1.dll. If you need the SDK DLL, please get in touch with us.

### 1. System Requirements
  - CPU: 2 cores or more (Recommended: 8 cores)
  - RAM: 4 GB or more (Recommended: 8 GB)
  - HDD: 4 GB or more (Recommended: 8 GB)
  - OS: Windows 7 or later
  - Dependency: OpenVINO™ Runtime (Version: 2022.3)

### 2. Setup and Test
  - Clone the project:
    ```
    git clone https://github.com/kby-ai/FaceLivenessDetection-Windows.git
    ```
  - Download the model from Google Drive and unzip: [click here](https://drive.google.com/file/d/1bYl0p5uHXuTQoETdbRwYLpd3huOqA3wY/view?usp=share_link)

  - Run the python code:
    ```
    python test.py
    ```
  - Send us the machine code and replace the license.txt file you received. Then, run python code again.
    
    ![image](https://github.com/kby-ai/FaceLivenessDetection-Windows/assets/125717930/345cb742-cef3-43b4-b46a-c84c94087826)
    
    ![image](https://github.com/kby-ai/FaceLivenessDetection-Windows/assets/125717930/0069fcd9-c35b-4020-ade9-7dced03918d2)

## About SDK

### 1. Initializing the SDK

- Step One

  First, obtain the machine code for activation and request a license based on the machine code.
  ```
  machineCode = getMachineCode()
  print("machineCode: ", machineCode.decode('utf-8'))
  ```
  
- Step Two

  Next, activate the SDK using the received license.
  ```
  setActivation(license.encode('utf-8'))
  ```  
  If activation is successful, the return value will be SDK_SUCCESS. Otherwise, an error value will be returned.

- Step Three

  After activation, call the initialization function of the SDK.
  ```
  initSDK("data".encode('utf-8'))
  ```
  The first parameter is the path to the model.

  If initialization is successful, the return value will be SDK_SUCCESS. Otherwise, an error value will be returned.

### 2. Enum and Structure
  - SDK_ERROR
  
    This enumeration represents the return value of the 'initSDK' and 'setActivation' functions.

    | Feature| Value | Name |
    |------------------|------------------|------------------|
    | Successful activation or initialization        | 0    | SDK_SUCCESS |
    | License key error        | -1    | SDK_LICENSE_KEY_ERROR |
    | AppID error (Not used in Server SDK)       | -2    | SDK_LICENSE_APPID_ERROR |
    | License expiration        | -3    | SDK_LICENSE_EXPIRED |
    | Not activated      | -4    | SDK_NO_ACTIVATED |
    | Failed to initialize SDK       | -5    | SDK_INIT_ERROR |

- FaceBox
  
    This structure represents the output of the face detection function.

    | Feature| Type | Name |
    |------------------|------------------|------------------|
    | Face rectangle        | int    | x1, y1, x2, y2 |
    | Liveness score (0 ~ 1)        | float    | liveness |
    | Face angles (-45 ~ 45)        | float    | yaw, roll, pitch |
    | Face quality (0 ~ 1)        | float    | face_quality |
    | Face luminance (0 ~ 255)       | float    | face_luminance |
    | Eye distance (pixels)       | float    | eye_dist |
    | Eye closure (0 ~ 1)       | float    | left_eye_closed, right_eye_closed |
    | Face occlusion (0 ~ 1)       | float    | face_occlusion |
    | Mouth opening (0 ~ 1)       | float    | mouth_opened |
    | 68 points facial landmark        | float[]    | landmarks_68 |
  
    > 68 points facial landmark
    
    <img src="https://user-images.githubusercontent.com/125717930/235560305-ee1b6a39-5dab-4832-a214-732c379cabfd.png" width=500/>

### 3. APIs
  - Face Detection
  
    The Face SDK provides a single API for detecting faces, performing liveness detection, determining face orientation (yaw, roll, pitch), assessing face quality, detecting facial occlusion, eye closure, mouth opening, and identifying facial landmarks.
    
    The function can be used as follows:

    ```
    faceBoxes = (FaceBox * maxFaceCount)()
    faceCount = faceDetection(image_np, image_np.shape[1], image_np.shape[0], faceBoxes, maxFaceCount)
    ```
    
    This function requires 5 parameters.
    * The first parameter: the byte array of the RGB image buffer.
    * The second parameter: the width of the image.
    * The third parameter: the height of the image.
    * The fourth parameter: the 'FaceBox' array allocated with 'maxFaceCount' for storing the detected faces.
    * The fifth parameter: the count allocated for the maximum 'FaceBox' objects.

    The function returns the count of the detected face.

### 4. Thresholds
  The default thresholds are as the following below:
  https://github.com/kby-ai/FaceLivenessDetection-Windows/blob/e7ffeecc21f6053828a744e127ddef2e8a34c4a2/test.py#L13-L25

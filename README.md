<p align="center">
  <a href="https://play.google.com/store/apps/dev?id=7086930298279250852" target="_blank">
    <img alt="" src="https://github-production-user-asset-6210df.s3.amazonaws.com/125717930/246971879-8ce757c3-90dc-438d-807f-3f3d29ddc064.png" width=500/>
  </a>  
</p>

#### 📚 Product & Resources - [Here](https://github.com/kby-ai/Product)
#### 🛟 Help Center - [Here](https://docs.kby-ai.com)
#### 💼 KYC Verification Demo - [Here](https://github.com/kby-ai/KYC-Verification-Demo-Android)
#### 🙋‍♀️ Docker Hub - [Here](https://hub.docker.com/u/kbyai)

# FaceLivenessDetection-Windows
## Overview
This repo is the `Face Liveness Detection` Python project for `Windows`.

> In this repo, we integrated `KBY-AI`'s `Face Liveness Detection` solution into `Windows Server SDK`.<br/>
> We can customize the SDK to align with your specific requirements.

### ◾FaceSDK(Server) Details
  | 🔽 Face Liveness Detection      | Face Recognition |
  |------------------|------------------|
  | <b>Face Detection</b>        | Face Detection    |
  | <b>Face Liveness Detection</b>        | Face Recognition(Face Matching or Face Comparison)    |
  | <b>Pose Estimation</b>        | Pose Estimation    |
  | <b>68 points Face Landmark Detection</b>        | 68 points Face Landmark Detection    |
  | <b>Face Quality Calculation</b>        | Face Occlusion Detection        |
  | <b>Face Occlusion Detection</b>        | Face Occlusion Detection        |
  | <b>Eye Closure Detection</b>        | Eye Closure Detection       |
  | <b>Mouth Opening Check</b>        | Mouth Opening Check        |

### ◾FaceSDK(Server) Product List
  | No.      | Repository | SDK Details |
  |------------------|------------------|------------------|
  | 1        | [Face Liveness Detection - Linux](https://github.com/kby-ai/FaceLivenessDetection-Docker)    | Face Livness Detection |
  | ➡️        | <b>[Face Liveness Detection - Windows](https://github.com/kby-ai/FaceLivenessDetection-Windows)</b>    | <b>Face Livness Detection</b> |
  | 3        | [Face Recognition - Linux](https://github.com/kby-ai/FaceRecognition-Docker)    | Face Recognition |
  | 4        | [Face Recognition - Windows](https://github.com/kby-ai/FaceRecognition-Windows)    | Face Recognition |

> To get `Face SDK(mobile)`, please visit products [here](https://github.com/kby-ai/Product):<br/>

## Try the API
### Online Demo
  You can test the SDK using images from the following URL:
  `https://web.kby-ai.com`
  
  ![image](https://github.com/kby-ai/FaceLivenessDetection-Docker/assets/125717930/4fd2c1ca-3552-4c6e-b8c2-4a12d7c92ca6)

### Postman
  To test the API, you can use `Postman`. Here are the endpoints for testing:
  - Test with an image file: Send a `POST` request to `http://18.221.33.238:8080/check_liveness`.
  - Test with a `base64-encoded` image: Send a `POST` request to `http://18.221.33.238:8080/check_liveness_base64`.

    You can download the `Postman` collection to easily access and use these endpoints. [click here](https://github.com/kby-ai/FaceLivenessDetection-Docker/blob/main/postman/kby-ai-live.postman_collection.json)
    
    ![image](https://github.com/kby-ai/FaceLivenessDetection-Docker/assets/125717930/b24b1145-08af-46ca-8ffa-65aa020749b4)


## SDK License

This project uses `KBY-AI`'s `Face Liveness Detection Server SD`, which requires a license per machine.

- The code below shows how to use the license: https://github.com/kby-ai/FaceLivenessDetection-Windows/blob/e7ffeecc21f6053828a744e127ddef2e8a34c4a2/test.py#L32-L44

- To request the license, please provide us with the `machine code` obtained from the `getMachineCode` function.

#### Please contact us:</br>
🧙`Email:` contact@kby-ai.com</br>
🧙`Telegram:` [@kbyai](https://t.me/kbyai)</br>
🧙`WhatsApp:` [+19092802609](https://wa.me/+19092802609)</br>
🧙`Skype:` [live:.cid.66e2522354b1049b](https://join.skype.com/invite/OffY2r1NUFev)</br>
🧙`Facebook:` https://www.facebook.com/KBYAI</br>
  
## How to run

> We have not published `facesdk1.dll`. If you need the `SDK dynamic library file(*.dll)`, please get in touch with us.

### 1. System Requirements
  - CPU: 2 cores or more (Recommended: 8 cores)
  - RAM: 4 GB or more (Recommended: 8 GB)
  - HDD: 4 GB or more (Recommended: 8 GB)
  - OS: Windows 7 or later
  - Dependency: OpenVINO™ Runtime (Version: 2022.3), ncnn Runtime(20220721) or later, Vulkan SDK Runtime(1.3.250)

### 2. Setup and Test
  - Clone the project:
    ```bash
    git clone https://github.com/kby-ai/FaceLivenessDetection-Windows.git
    ```
  - Download the model from `Google Drive` and unzip: [click here](https://drive.google.com/file/d/1bYl0p5uHXuTQoETdbRwYLpd3huOqA3wY/view?usp=share_link)

  - Run the python code:
    ```bash
    python test.py
    ```
  - Send us the `machine code` and then we will give you a license key.
  
    After that, update the `license.txt` file by overwriting the license key that you received. Then, run python code again.
    
    ![image](https://github.com/kby-ai/FaceLivenessDetection-Windows/assets/125717930/345cb742-cef3-43b4-b46a-c84c94087826)
    
    ![image](https://github.com/kby-ai/FaceLivenessDetection-Windows/assets/125717930/0069fcd9-c35b-4020-ade9-7dced03918d2)

## About SDK

### 1. Initializing the SDK

- Step One

  First, obtain the `machine code` for activation and request a license based on the `machine code`.
  ```python
  machineCode = getMachineCode()
  print("machineCode: ", machineCode.decode('utf-8'))
  ```
  
- Step Two

  Next, activate the SDK using the received license.
  ```python
  setActivation(license.encode('utf-8'))
  ```  
  If activation is successful, the return value will be `SDK_SUCCESS`. Otherwise, an error value will be returned.

- Step Three

  After activation, call the initialization function of the SDK.
  ```python
  initSDK("data".encode('utf-8'))
  ```
  The first parameter is the path to the model.

  If initialization is successful, the return value will be `SDK_SUCCESS`. Otherwise, an error value will be returned.

### 2. Enum and Structure
  - SDK_ERROR
  
    This enumeration represents the return value of the `initSDK` and `setActivation` functions.

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
  
    The `Face SDK` provides a single API for detecting faces, performing `liveness detection`, determining `face orientation` (yaw, roll, pitch), assessing `face quality`, detecting `facial occlusion`, `eye closure`, `mouth opening`, and identifying `facial landmarks`.
    
    The function can be used as follows:

    ```python
    faceBoxes = (FaceBox * maxFaceCount)()
    faceCount = faceDetection(image_np, image_np.shape[1], image_np.shape[0], faceBoxes, maxFaceCount)
    ```
    
    This function requires 5 parameters.
    * The first parameter: the byte array of the RGB image buffer.
    * The second parameter: the width of the image.
    * The third parameter: the height of the image.
    * The fourth parameter: the `FaceBox` array allocated with `maxFaceCount` for storing the detected faces.
    * The fifth parameter: the count allocated for the maximum `FaceBox` objects.

    The function returns the count of the detected face.

### 4. Thresholds
  The default thresholds are as the following below:
  https://github.com/kby-ai/FaceLivenessDetection-Windows/blob/e7ffeecc21f6053828a744e127ddef2e8a34c4a2/test.py#L13-L25


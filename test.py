import sys
sys.path.append('.')

from PIL import Image
import numpy as np

from facesdk import getMachineCode
from facesdk import setActivation
from facesdk import faceDetection
from facesdk import initSDK
from facebox import FaceBox

livenessThreshold = 0.7
yawThreshold = 10
pitchThreshold = 10
rollThreshold = 10
occlusionThreshold = 0.9
eyeClosureThreshold = 0.8
mouthOpeningThreshold = 0.5
borderRate = 0.05
smallFaceThreshold = 100
lowQualityThreshold = 0.3
hightQualityThreshold = 0.7
luminanceDarkThreshold = 50
luminanceLightThreshold = 200

maxFaceCount = 10

licensePath = "license.txt"
license = ""

machineCode = getMachineCode()
print("machineCode: ", machineCode.decode('utf-8'))

try:
    with open(licensePath, 'r') as file:
        license = file.read()
except IOError as exc:
    print("failed to open license.txt: ", exc.errno)
print("license: ", license)


ret = setActivation(license.encode('utf-8'))
print("activation: ", ret)

ret = initSDK("D:/Temp/kby_face/github/FaceLivenessDetection-Windows/data".encode('utf-8'))
print("init: ", ret)

def process_file(filePath):
    image = Image.open(filePath)
    image_np = np.asarray(image)

    faceBoxes = (FaceBox * maxFaceCount)()
    faceCount = faceDetection(image_np, image_np.shape[1], image_np.shape[0], faceBoxes, maxFaceCount)

    faces = []
    for i in range(faceCount):
        # landmark_68 = []
        # for j in range(68):
        #     landmark_68.append({"x": faceBoxes[i].landmark_68[j * 2], "y": faceBoxes[i].landmark_68[j * 2 + 1]})
        faces.append({"x1": faceBoxes[i].x1, "y1": faceBoxes[i].y1, "x2": faceBoxes[i].x2, "y2": faceBoxes[i].y2, 
                        "liveness": faceBoxes[i].liveness, 
                        "yaw": faceBoxes[i].yaw, "roll": faceBoxes[i].roll, "pitch": faceBoxes[i].pitch,
                        "face_quality": faceBoxes[i].face_quality, "face_luminance": faceBoxes[i].face_luminance, "eye_dist": faceBoxes[i].eye_dist,
                        "left_eye_closed": faceBoxes[i].left_eye_closed, "right_eye_closed": faceBoxes[i].right_eye_closed,
                        "face_occlusion": faceBoxes[i].face_occlusion, "mouth_opened": faceBoxes[i].mouth_opened})
                        # "landmark_68": landmark_68})

    result = ""
    if faceCount == 0:
        result = "No face"
    elif faceCount > 1:
        result = "Multiple face"
    else:
        livenessScore = faceBoxes[0].liveness
        if livenessScore > livenessThreshold:
            result = "Real"
        else:
            result = "Spoof"
        
        isNotFront = True
        isOcclusion = False
        isEyeClosure = False
        isMouthOpening = False
        isBoundary = False
        isSmall = False
        quality = "Low"
        luminance = "Dark"
        if abs(faceBoxes[0].yaw) < yawThreshold and abs(faceBoxes[0].roll) < rollThreshold and abs(faceBoxes[0].pitch) < pitchThreshold:
            isNotFront = False
        
        if faceBoxes[0].face_occlusion > occlusionThreshold:
            isOcclusion = True

        if faceBoxes[0].left_eye_closed > eyeClosureThreshold or faceBoxes[0].right_eye_closed > eyeClosureThreshold:
            isEyeClosure = True

        if faceBoxes[0].mouth_opened > mouthOpeningThreshold:
            isMouthOpening = True
        
        if (faceBoxes[0].x1 < image_np.shape[1] * borderRate or 
            faceBoxes[0].y1 < image_np.shape[0] * borderRate or 
                faceBoxes[0].x1 > image_np.shape[1] - image_np.shape[1] * borderRate or 
                faceBoxes[0].x1 > image_np.shape[0] - image_np.shape[0] * borderRate):
            isBoundary = True

        if faceBoxes[0].eye_dist < smallFaceThreshold:
            isSmall = True
        
        if faceBoxes[0].face_quality < lowQualityThreshold:
            quality = "Low"
        elif faceBoxes[0].face_quality < hightQualityThreshold:
            quality = "Medium"
        else:
            quality = "High"
        
        if faceBoxes[0].face_luminance < luminanceDarkThreshold:
            luminance = "Dark"
        elif faceBoxes[0].face_luminance < luminanceLightThreshold:
            luminance = "Normal"
        else:
            luminance = "Light"

    faceState = {"result": result, "liveness_score": livenessScore, "is_not_front": isNotFront, "is_occluded": isOcclusion, "eye_closed": isEyeClosure,
                  "mouth_opened": isMouthOpening, "is_boundary_face": isBoundary, "is_small": isSmall, "quality": quality, "luminance": luminance}
    result = {"face_state": faceState, "faces": faces}

    return result

if __name__ == "__main__":
    ret = process_file('D:/Temp/kby_face/github/FaceLivenessDetection-Windows/live_examples/1.jpg')
    print(ret)
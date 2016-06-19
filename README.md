# TorpedoDetection
## Problem Statement
This is a data analysis problem. 
Your country is being attacked by aliens aboard Spaceship Ravager. Their weapon of choice is a proton torpedo. 
You could counter attack or avoid the torpedos if you knew where they were, but unfortunately, both Spaceship Ravager and the torpedos are invisible to the naked eye! They are hidden by cloaks made of a material called kromon.
You know that more spaceships identical to Ravager are converging and preparing for an attack…
Your only hope is the ‘Detector’, an imaging kromon detection system that provides the only information you have about the locations of enemy spaceships and torpedos. However, the information isn’t perfect.
First, the Detector outputs data that is equivalent of a black and white image. Each pixel where kromon material is detected is ‘on’ and marked with a ‘+’. The Detector only detects kromon at any particular point on an image, not what its intensity is. 
Second, the data is very noisy – even if there are no spaceships or torpedos in a particular area, some pixels will be “on”, and even if there is a spaceship or torpedo, some of its pixels will be “off”. For example, here's a sample of raw data from the Detector (each “+” is a pixel that is ‘on’):
[Click here](https://github.com/yardstick17/TorpedoDetection/blob/master/DetectorOutput.blf)


Sample image of a proton torpedo:[Click here]
(https://github.com/yardstick17/TorpedoDetection/blob/master/Ravager.blf)

On the Detector data, the pixels that should be “on” for a proton torpedo have been highlighted. You can see that more of the highlighted pixels are “on” in the highlighted area than in other areas of the image. You can use this difference to locate spaceships and torpedos in the Detector data.

There are given 3 files - 
1. DetectorOutput.blf: a 100 x 100 swath of raw data 
2. ProtonTorpedo.blf: perfect image of a proton torpedo 
3. Ravager.blf: perfect image of spaceship Ravager

The program analyzes arbitrary-sized Detector images, returning a list of targets (spaceships and proton torpedos) found. 
For each target, it includes the following –
Target type
Co-ordinates of target on Detector data
Degree of confidence in the detection
## Run Command
```
python test.py percent_cut_off  # python test.py 60

```
## Output
```
Target Name :  Ravager  , Co-ordinates :  ((26, 54), (35, 69))  , Degree of Confidence :  62.9629629698
Target Name :  Ravager  , Co-ordinates :  ((68, 43), (77, 58))  , Degree of Confidence :  61.1111111183
Target Name :  Ravager  , Co-ordinates :  ((34, 64), (43, 79))  , Degree of Confidence :  70.3703703759
Target Name :  Ravager  , Co-ordinates :  ((26, 56), (35, 71))  , Degree of Confidence :  64.8148148213
Target Name :  Ravager  , Co-ordinates :  ((26, 55), (35, 70))  , Degree of Confidence :  72.2222222274
Target Name :  ProtonTorpedo  , Co-ordinates :  ((1, 0), (12, 12))  , Degree of Confidence :  70.2127659638
Target Name :  ProtonTorpedo  , Co-ordinates :  ((79, 25), (90, 37))  , Degree of Confidence :  70.2127659638
Target Name :  ProtonTorpedo  , Co-ordinates :  ((15, 29), (26, 41))  , Degree of Confidence :  63.8297872417
```


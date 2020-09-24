# Pose_Coach 🤸‍♀️
The project gives instructions to perform exercises/yoga poses with the correct form.


## Smart coach using deep learning for body keypoint detection and geometry/ML for giving guidance.

Dash app for style transfer using neural network

![image](https://github.com/niharika412/pose_coach/blob/master/home.PNG?raw=true)
### Prerequisites

* Computer Vision
* Pandas
* Numpy
* Tensorflow 
* Plotly Dash

### Installing

Install the prerequisties

To run it locally, first clone the directory,
Install the requirements


Then run `python index.py` in cmd

Go to localhost:8050 in your web browser


A home page with three exercise poses will be displayed. Pick one and click on it.

The next page will allow you to upload an image from your system and after clicking submit, the keypoints detected by OPENPOSE algorithm will be displayed along with some instructions on how to perform the pose better.


## Built With

* [Dash](https://plotly.com/dash/) -  Machine learning library
* [Openpose]https://github.com/CMU-Perceptual-Computing-Lab/openpose/) - web framework

## Results
![success](https://github.com/niharika412/pose_coach/blob/master/final.PNG?raw=true)

## future work

* Improving accuracy of the algorithm. The algorithm fails when the background blends into the picture. 
* Algorithm used here is openpose mobilenet thin architecture, however larger more precise models can be used.
* With high power GPUs, the keypoint detection can be done in real-time and instructions can be provided on the go.

## Inspiration

Most exercises only work if they are done correctly, i.e in good form. This is why people insist on having personal trainers. However, during the pandemic most gyms were closed and exercises were done at home. This project is a very practical solution to analyse how a person exercises and is he/she doing it right.


## References

* ![Mobile Net arch. code]https://github.com/quanhua92/human-pose-estimation-opencv
* ![Similar work]https://github.com/stevenzchen/pose-trainer

# pose-coach

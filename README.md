# Motion-Detection-with-Python-and-OpenCV

A motion detector built using Python and OpenCV documentation.Through the program, we can access our webcam and detect any motion in front of it and we can record the intervals 
where motion was observed in the webcam in a CSV file via pandas. The motion is detected using OpenCV where we calculate the absolute difference between frames captured by webcam at each instance(delta_frame) and build a binary threshold_frame to better classify our moving objects.
Using the  Bokeh plotting library, we can plot the csv file containing the start and end intervals of motion for better visualization.

![Screenshot (74)](https://user-images.githubusercontent.com/72685315/152538286-88b1534c-ae2e-4f53-8734-85a7602b823d.png)

![Screenshot (78)](https://user-images.githubusercontent.com/72685315/152828097-6123bba9-feec-4fe3-a5da-a4b595b40126.png)



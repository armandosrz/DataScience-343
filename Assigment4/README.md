# Difference Image

For this project 310 images were capture over a span of an hour with a difference of
12 seconds between capture (revise [capture script](capture_image.py)). After a careful
analysis a [hypothesis](Hypothesis.pdf) was made towards the areas that are most
affected by change over time.

All the images were then processed in order to obtain the average difference image
from all the input images. The program outputs a new picture which highlights
the area of change in red based on the passed threshold.
[example 20% threshold](figure_20.png)


## Usage

Version: `Python 2.7`

`python main.py <threshold>`

Where the threshold is a value in between [0...0.99].

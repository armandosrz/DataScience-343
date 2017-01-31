# K-Nearest Neighbors

K nearest Neighbors approximation using the mean values. Determine a US color
map based on how Americans call their soda/soft drinks in different parts of
America.


For this project we take the [data points](data.png) by obtaining the pixels
that are not green. Then we generate a new color in the [us_outline](us_outline.png)
based on the Euclidean distance from K-Neighbor and obtain the new pixel
color by averaging those.  


##Usage:
- _Language:_ Python 2.7
- _Execution:_ ´python main.py {K-Neighbor(int)} {FileName}´

###Detailed Instructions
  For more information open the pdf called (_Challenge_5.pdf_)[Challenge_5.pdf].
  Results are stored in the files that end in ´{number}-neigboors.png´

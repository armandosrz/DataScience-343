import urllib, time


for x in range(310):
    urllib.urlretrieve("http://livecam-static.olemiss.edu/quadrangle.jpg?0.008437760880358525","local{}.jpg".format(x))
    time.sleep(12)
    print x

#!/usr/bin/python
#
# example.py - An example of using the neuro.py package
# for the CSCI 343 Final Project
#
# This example creates a nueral network that can simulate
# the behavior of an AND gate.
#

from __future__ import division
import numpy as np
import neuro #This is MUST be included

#training inputs
inputs=[[0,0], [0,1], [1,0], [1,1]]
#training targets placed in the same order as their
#corresponding inputs (listed above)
targets=[[0], [0], [0], [1]]

#initializes the neural network
network=neuro.setup_network(inputs)

#The number of repetitions that you will
#be training your network with
training_reps=100

#trains your neural network
neuro.train(network, inputs, targets, training_reps)

#gets the predicted value for input [0,0]
pred = neuro.predict(network, [0,0])
#rounds the predicted value to either 0 or 1
pred = int( np.round(pred) )

print "0 & 0 =",pred

#the following lines are the same as the lines
#documented above except they are for inputs [0,1], [1,0], and [1,1]
pred = neuro.predict(network, [0,1])
pred = int( np.round(pred) )

print "0 & 1 =",pred

pred = neuro.predict(network, [1,0])
pred = int( np.round(pred) )

print "1 & 0 =",pred

pred = neuro.predict(network, [1,1])
pred = int( np.round(pred) )

print "1 & 1 =",pred

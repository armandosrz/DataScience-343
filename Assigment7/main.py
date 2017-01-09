from __future__ import division
import numpy as np
import neuro #This is MUST be included
import random

random.seed(0)


def neuro_start(inputs, targets, training):
    #initializes the neural network
    network=neuro.setup_network(inputs)

    #The number of repetitions that you will
    #be training your network with
    training_reps= training

    #trains your neural network
    neuro.train(network, inputs, targets, training_reps)

    total = 0
    correct = 0

    for i in range(1,10):
        for x in range(1,10):
            pred = neuro.predict(network, [i+x])
            #rounds the predicted value to either 0 or 1
            #print '{}  == pred {}'.format(i+x,pred)
            pred = np.round(pred)
            if (i+x)%2 == pred:
                correct+= 1
            total += 1
    percent = (correct/total) * 100
    #print 'with training: {}'.format(training_reps)
    #print 'correct: {}\n total: {} \n {:.2f}%'.format(correct, total, (correct/total) * 100)
    return training_reps, percent, correct, total

def main():

    # Get inputs from file
    inputs = []
    with open('dataset.csv', 'r') as file:
        for line in file:
            inputs.append([sum(list(map(int, line.strip().split(','))))])
    # Generate target points
    #print inputs
    targets = []
    for a in inputs:
        targets.append([(a[0]%2)])
    #print targets
    # Perform cross validation on training point and return best result.
    maxi = [1, 0]
    for t in [50 * i for i in range(1,10)]:
        temp = neuro_start(inputs, targets, t)
        if temp[1] > maxi[1]:
            maxi = temp

    print 'Training_points: {}\n Correct: {:.2f}% ({} out of {})'.format(*maxi)

if __name__ == '__main__':
    main()

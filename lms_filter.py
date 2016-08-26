"""Least mean squares filter"""
import numpy as np
import matplotlib.pyplot as plt
import pdb

def lms_filter(signal, order = 4, mu = 0.05 ):
    weight = np.zeros(order) # initial weight, the system model
    length = len(signal) #find train signal length
    estimate = [] # LSM filter output
    er = [] # error list
    for i in range(length-order):
        x_signal = list(signal[i:i+order])# slice input signal
        x_signal.reverse() #transform sliced signal to timeline
        x_signal = np.transpose(x_signal) # x_signal transpose
        y_current = signal[i] #current signal point
        y_estimate = np.dot(weight, x_signal) #use LSM estamate current signal
        estimate.append(y_estimate) # filter output
        error = y_current - y_estimate
        er.append(error)
        weight = weight + mu * error * x_signal
    return estimate, weight,er

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Feb. 14, 2023

A sample code to do "embarrassingly" parallel computation of trajectories of the simple harmonic oscillator
"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
from numpy import arange
import os
import time
import multiprocessing
from multiprocessing import Pool
import pandas as pd
from scipy.integrate import odeint


########################################################################################################################

def harmonic_oscillator(initial_point:np.ndarray, t:np.ndarray, omega) -> np.ndarray:
    """
    Simple Harmonic oscillator (mass = 1)
    """
    u = initial_point
    # print(u)
    q = u[0]
    p = u[1]
    dq_dt = p
    dp_dt = -omega**2*q
    return np.hstack((dq_dt, dp_dt))
########################################################################################################################


def generate_trajectory(t: np.ndarray,omega: float, initial_point:np.ndarray) -> np.ndarray:
    """
    input: time, frequency (omega), and initial condition
    output: trajectory
    """
    sol = odeint(harmonic_oscillator, initial_point, t, args=(omega,))
    return sol
########################################################################################################################


def compute_trajectories(ind):

    # total time to integrate
    dt = 10**(-3)
    t = arange(0, 10, dt)
    omega = 0.5
    initial = np.random.uniform(low=-1.0, high=1.0, size=(2,))  # initial condition

    trajectory = generate_trajectory(t=t, omega=omega, initial_point=initial)

    # save trajectory
    traj_data = pd.DataFrame(trajectory)

    # save as csv (the usual format)
    fname1 = 'trajectory-data-'+str(ind)+'.csv'
    traj_data.to_csv(fname1)  # as csv

    # save as HDF5 (for large data)
    fname2 = 'trajectory-data-' + str(ind) + '.h5'
    all_posotions = pd.DataFrame(trajectory[:, 0])
    all_momenta = pd.DataFrame(trajectory[:, 1])
    all_posotions.to_hdf(fname2, key="q")
    all_momenta.to_hdf(fname2, key="p")
########################################################################################################################


def read_data_files():
    """
    To be done
    """
    pass
########################################################################################################################


def all_computations(n):
    # To compute code running time
    start = time.time()
    time_fname = "time-elapsed.txt"

    # Serial computation
    print ("Computing 1000 trajectories one at a time")
    for ind in range(n):
        compute_trajectories(ind=ind)

    end = time.time()
    total_time = (end - start)
    f = open(time_fname, "a")
    f.write("\n Serial computation time: " + str(total_time) + " seconds for 1000 trajectories ")
    f.close()
    print("Computation time for 1000 trajectories:", total_time, " seconds.")

    # Parallel computation
    print("Computing 1000 trajectories in parallel")
    start = time.time()
    n_cores = multiprocessing.cpu_count()
    print("No. of cores available:", n_cores)
    print("Using 8 cores ...")
    pool = multiprocessing.Pool(8)  # using 6 cores
    ind = range(n)  # no. of trajectories
    pool.map(compute_trajectories, ind)
    end = time.time()
    total_time = (end - start)
    f = open(time_fname, "a")
    f.write("\nComputation time: " + str(total_time) + " seconds. for 1000 trajectories ")
    f.close()
    print("Parallel computation time for 1000 trajectories:", total_time, " seconds.")

    print("Total number of data files generated: 2 x 1000")
########################################################################################################################
########################################################################################################################


def main():
    n = 1000  # no. of trajectories to be computed
    all_computations(n=n)

########################################################################################################################


if __name__ == "__main__":
    main()

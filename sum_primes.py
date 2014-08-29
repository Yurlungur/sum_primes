#!/usr/bin/env python2

"""
A short Python program that computes the sum of all prime numbers less
than N.
"""

import numpy

def sum_primes(N):
    """
    Computes the sum of all prime numbers less than N using the Sieve
    of Eratosthenes.
    """
    # Create an array of numbers k such that 2 <= k <= N.
    # We exclude 0 and 1 because they are known not to be prime.
    numbers = numpy.arange(2,N)

    # We iterate through the array and set non prime numbers to
    # zero. We do this by assuming all nonzero numbers are prime. If
    # we encounter a zero we ignore it. If we encounter a nonzero
    # number, we iterate through the array and set all multiples of
    # that number to zero.
    for i in xrange(len(numbers)):
        if numbers[i] != 0:
            for j in xrange(i+numbers[i],len(numbers),numbers[i]):
                numbers[j] = 0

    # Finally we take the sum of all elements in the array. Only the
    # primes contribute because all other elements have been set to
    # zero.
    prime_sum = numpy.sum(numbers)
    return prime_sum

max_number = 200
print "Summing all prime numbers less than {}.".format(max_number)
prime_sum = sum_primes(max_number)
print "The sum is {}.".format(prime_sum)


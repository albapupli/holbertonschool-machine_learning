#!/usr/bin/env python3
"""
this function determines if you should stop gradient descent early
"""

def early_stopping(cost, opt_cost, threshold, patience, count):
    """
    check if the epoke time is here
    """
    if opt_cost - cost > threshold:
        count = 0
    else:
        count += 1
    
    if count != patience:
        return False, count
    else:
        return True, count
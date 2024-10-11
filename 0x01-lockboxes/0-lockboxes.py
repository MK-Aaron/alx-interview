#!/usr/bin/python3
"""
Lockboxes module
"""


def canUnlockAll(boxes):
    """ Check if there are boxes """
    if not boxes:
        return True

    """ Use set to track unlcoked boxes (box 0 unlocked) """
    unlocked_boxes = set([0])

    """ Queue to explore boxes starting with 0 """
    to_explore = [0]

    """ While there still boxes to explore """
    while to_explore:
        current_box = to_explore.pop()

        """ for each key inside current box """
        for key in boxes[current_box]:
            """ Check if key correspond to box which hasn't been unblocked """
            if key < len(boxes) and key not in unlocked_boxes:
                unlocked_boxes.add(key)
                to_explore.append(key)

    """ After exploring, check if all boxes are unlocked """
    return len(unlocked_boxes) == len(boxes)

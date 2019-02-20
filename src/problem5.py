#
#   This problem implements the funny_move method from the Paper Exam
#
#
#   TODO#1: Read the supplied Point class to understand its function
#
#
###############################################################################
# NOTE: For ALL of the methods that you implement, the method is allowed
# to have additional side effects as needed by it and/or other methods.
###############################################################################
class Point(object):
    """Point in 2-D space"""
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return"Point({},{})".format(self.x, self.y)
##############################################################################
#
#   TODO#4:  Write the method for funny move
#
#   What comes in:
#       An integer x
#   What goes out:
#       Nothing
#   Side effects:
#       If the integer, x, is even, the new x-coordinate of the point becomes the value of the even integer.
#       If the integer, x, is odd, the x-coordinate is moved by the value of the odd integer.
#       The y coordinate is always moved to a position equal to twice its original position.
#
#   Example 1:      point1 coordinates (2,5)
#                   point1.funny_move(4)
#                   New coordinates of point1:
#                   Since the integer x is even (4), the new x-coordinate becomes 4
#                   The new y-coordinate is 2*5 = 10
#                   After a call to funny_move  p1’s coordinates are (4, 10)
#
#   Example 2:      point2 coordinates (2,1)
#                   point2.funny_move(3)
#                   New coordinates of point2:
#                   Since the integer x is odd (3), the new x-coordinate becomes 2+3 = 5
#                   The new y-coordinate is 2*1 = 2
#                   After a call to funny_move  p2’s coordinates are (5, 2)
#
##############################################################################
    def funny_move(self,m):
        return self
##############################################################################
#
#   TODO#3:  Write the three more test cases for funny_move
#            The first one has been written for you.
#            (It will fail until you write funny_move)
##############################################################################
def run_test_funny_move():
    point1 = Point(2,5)
    expected_x = 4
    expected_y = 10
    actual_x = point1.funny_move(3).x
    actual_y = point1.funny_move(3).y
    print()
    print('Expected point is ', expected_x, expected_y)
    print('Actual point is ', actual_x, actual_y)
    print()

##############################################################################
#
#   TODO#2:  In main below, write code that will create and print
#            three additional points.  One has been written for you
#
##############################################################################

def main():
    point1 = Point(54,29)
    print(point1)
    run_test_funny_move()
    pass


# Calls main to start execution
main()

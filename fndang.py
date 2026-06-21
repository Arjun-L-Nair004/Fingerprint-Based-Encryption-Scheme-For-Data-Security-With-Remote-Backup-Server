# import math
#
#
# def distance(p1, p2):
#     return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
#
#
# def find_angle(A, B, C):
#     # Lengths of sides
#     a = distance(B, C)
#     b = distance(A, C)
#     c = distance(A, B)
#
#     # Using the cosine rule to find the angle at A
#     angle_A = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
#
#     # Convert the angle from radians to degrees
#     angle_A_degrees = math.degrees(angle_A)
#
#     return angle_A_degrees
#
#
# # Example coordinates
# A = (1, 2)
# B = (4, 6)
# C = (5, 2)
#
# angle_A = find_angle(A, B, C)
# angle_B = find_angle( B,C,A)
# angle_c = find_angle( C,A,B)
#
# print(angle_A,angle_B,angle_c)

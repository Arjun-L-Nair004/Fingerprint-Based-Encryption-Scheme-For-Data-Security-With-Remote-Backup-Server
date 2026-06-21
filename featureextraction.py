# import cv2
# import fingerprint_feature_extractor
# img = cv2.imread(r'C:\Users\noufa\PycharmProjects\FBESFDSWRBS\finger3.jpg', 0)				# read the input image --> You can enhance the fingerprint image using the "fingerprint_enhancer" library
# FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(img, spuriousMinutiaeThresh=10, invertImage=False, showResult=True, saveResult=True)
# print(FeaturesBifurcations)
# print(FeaturesTerminations)
# pp=[]
#
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
# for idx, curr_minutiae in enumerate(FeaturesTerminations):
#     # print(idx,curr_minutiae.locX,curr_minutiae.locY)
#     pp.append([curr_minutiae.locX,curr_minutiae.locY])
#
#
# for idx, curr_minutiae in enumerate(FeaturesBifurcations):
#     # print(idx,curr_minutiae.locX,curr_minutiae.locY)
#     pp.append([curr_minutiae.locX, curr_minutiae.locY])
#
# import numpy as np
# points = np.array(pp)
# from scipy.spatial import Delaunay
# tri = Delaunay(points)
# for i in tri.points:
#     print(i)
#
#
# for i in tri.simplices:
#     # print(tri.points[i[0]],tri.points[i[1]],tri.points[i[2]])
#     A=tri.points[i[0]]
#     B=tri.points[i[1]]
#     C=tri.points[i[2]]
#     angle_A = find_angle(A, B, C)
#     angle_B = find_angle(B, C, A)
#     angle_c = find_angle(C, A, B)
#     print(math.floor(angle_A), math.floor(angle_B), math.floor(angle_c))
#
#     """"√ [ (x₂ - x₁)² + (y₂ - y₁)²]."""
#     """a==b"""
#     return np.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2 + (A[2] - B[2]) ** 2)
#
#     """b==c"""
#
#
#     """c==d"""
#
#
#
#
#



#
# import cv2
# import fingerprint_feature_extractor
# import math
# import numpy as np
# from scipy.spatial import Delaunay
#
#
# img = cv2.imread(r'C:\Users\noufa\PycharmProjects\FBESFDSWRBS\finger3.jpg', 0)
#
#
# FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(
#     img, spuriousMinutiaeThresh=10, invertImage=False, showResult=True, saveResult=True
# )
#
#
# print("Bifurcations:", FeaturesBifurcations)
# print("Terminations:", FeaturesTerminations)
#
# pp = []
#
#
#
# def distance(p1, p2):
#     return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
#
#
# def find_angle(A, B, C):
#     # Lengths of sides of the triangle
#     a = distance(B, C)
#     b = distance(A, C)
#     c = distance(A, B)
#
#     angle_A = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
#
#
#     angle_A_degrees = math.degrees(angle_A)
#
#     return angle_A_degrees
#
#
# for idx, curr_minutiae in enumerate(FeaturesTerminations):
#     pp.append([curr_minutiae.locX, curr_minutiae.locY])
#
# for idx, curr_minutiae in enumerate(FeaturesBifurcations):
#     pp.append([curr_minutiae.locX, curr_minutiae.locY])
#
# points = np.array(pp)
#
#
# tri = Delaunay(points)
#
#
# print("Delaunay Triangulation Points:")
# for i in tri.points:
#     print(i)
#
#
# for i in tri.simplices:
#     A = tri.points[i[0]]
#     B = tri.points[i[1]]
#     C = tri.points[i[2]]
#
#     angle_A = find_angle(A, B, C)
#     angle_B = find_angle(B, C, A)
#     angle_C = find_angle(C, A, B)
#
#     """"√ [ (x₂ - x₁)² + (y₂ - y₁)²]."""
#     """a==b"""
#         # return np.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2 + (A[2] - B[2]) ** 2)
#
#     """b==c"""
#
#
#     """c==d"""
#
#     print(f"Angles of triangle {i}:")
#     print(f"Angle at A: {math.floor(angle_A)} degrees")
#     print(f"Angle at B: {math.floor(angle_B)} degrees")
#     print(f"Angle at C: {math.floor(angle_C)} degrees")
#
#     distance_AB = distance(A, B)
#     distance_BC = distance(B, C)
#     distance_CA = distance(C, A)
#
#     print(f"Distances between points A, B, C:")
#     print(f"Distance AB: {distance_AB}")
#     print(f"Distance BC: {distance_BC}")
#     print(f"Distance CA: {distance_CA}")
#
#
#     k= str(math.floor(angle_A))+ str(math.floor(angle_B))+str(math.floor(angle_C))
#     print(k)



###hash k

# use hash value as aes key and encrypy





# decrypt time   finger image upload --- same process again ---  decrypt using hash































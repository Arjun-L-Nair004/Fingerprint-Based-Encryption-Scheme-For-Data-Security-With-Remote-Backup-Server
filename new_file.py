import cv2
import fingerprint_feature_extractor
import math
import numpy as np
from scipy.spatial import Delaunay
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

img = cv2.imread(r'C:\Users\noufa\PycharmProjects\FBESFDSWRBS\finger3.jpg', 0)

FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(
    img, spuriousMinutiaeThresh=10, invertImage=False, showResult=True, saveResult=True
)

print("Bifurcations:", FeaturesBifurcations)
print("Terminations:", FeaturesTerminations)

pp = []


def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def find_angle(A, B, C):
    a = distance(B, C)
    b = distance(A, C)
    c = distance(A, B)

    angle_A = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    angle_A_degrees = math.degrees(angle_A)
    return angle_A_degrees


for idx, curr_minutiae in enumerate(FeaturesTerminations):
    pp.append([curr_minutiae.locX, curr_minutiae.locY])

for idx, curr_minutiae in enumerate(FeaturesBifurcations):
    pp.append([curr_minutiae.locX, curr_minutiae.locY])

points = np.array(pp)

tri = Delaunay(points)

print("Delaunay Triangulation Points:")
for i in tri.points:
    print(i)

angle_sum_list = []

secret_key = os.urandom(32)
iv = os.urandom(16)


def aes_encrypt(data, key, iv):

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return encrypted_data


for i in tri.simplices:
    A = tri.points[i[0]]
    B = tri.points[i[1]]
    C = tri.points[i[2]]

    angle_A = find_angle(A, B, C)
    angle_B = find_angle(B, C, A)
    angle_C = find_angle(C, A, B)






    print(f"Angles of triangle {i}:")
    print(f"Angle at A: {math.floor(angle_A)} degrees")
    print(f"Angle at B: {math.floor(angle_B)} degrees")
    print(f"Angle at C: {math.floor(angle_C)} degrees")

    distance_AB = distance(A, B)
    distance_BC = distance(B, C)
    distance_CA = distance(C, A)

    print(f"Distances between points A, B, C:")
    print(f"Distance AB: {distance_AB}")
    print(f"Distance BC: {distance_BC}")
    print(f"Distance CA: {distance_CA}")

    k = str(math.floor(angle_A)) + str(math.floor(angle_B)) + str(math.floor(angle_C))+str(math.floor(distance_AB))+str(math.floor(distance_BC))+str(math.floor(distance_CA))

    print(f"Concatenated angles (k): {k}")


hash_object = hashlib.sha256(k.encode())
hash_value = hash_object.hexdigest()
print(f"Hash value of k: {hash_value}\n")

encrypted_hash = aes_encrypt(hash_value, secret_key, iv)
print(f"Encrypted hash value (AES): {encrypted_hash.hex()}\n")


total_angle_sum = sum(angle_sum_list)
print(f"Total sum of all angles: {total_angle_sum}")

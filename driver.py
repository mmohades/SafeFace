#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 15:28:12 2019
@author: maksim

Libraries used
pip install boto3
pip install awscli
which aws
aws configure

Disoplay AWS info: cat ~/.aws/credentials


driver
take_pic
post_pic

Driver script, communicates with AWS
"""
import take_pic
import post_pic
import compare_faces
from servo import lock, unlock

BUCKET = "securitycamera1"      # Bucket name
KEY_SOURCE = "new_image.jpg"    # New Image
KEY_TARGET = "saved_image.jpg"  # Person's Image


'''
The main function
'''


def main():
    # Take the picture
    take_pic.main(KEY_SOURCE)

    # Send the picture to AWS
    post_pic.main(BUCKET, KEY_SOURCE)

    # Flag variable
    flag = True
    information = {}

    # Get the similarity
    try:
        source_face, matches, similarity = compare_faces.main(BUCKET, KEY_SOURCE, BUCKET, KEY_TARGET)
    except:
        flag = False
        information["status"] = "not_auth"

    if(flag):
        try:
            # if it is 80%
            if(int(similarity) > 80):
                flag = True
                print ("Face maches: " + str(similarity))
            # If the face doesn't match or the accuracy is very low
            else:
                flag = False
                information["status"] = "not_auth"
                print("Face doesn't match!")
        except:
            flag = False
            information["status"] = "not_auth"

    print("flag: " + str(flag))

    if flag:
        unlock()
        information["status"] = "unlocked"

    else:
        lock()
        information["status"] = "locked"

    return information


if __name__ == "__main__":
    main()

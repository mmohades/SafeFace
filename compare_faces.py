'''
Communicate with AWS
'''

import boto3

'''
Call AWS
'''
def main(bucket, key, bucket_target, key_target, threshold=80, region="us-east-1"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.compare_faces(
	    SourceImage={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		TargetImage={
			"S3Object": {
				"Bucket": bucket_target,
				"Name": key_target,
			}
		},
	    SimilarityThreshold=threshold,
	)

	# Check for similarity string
	try:
		#print(response)
		compare = response['FaceMatches'][0]['Similarity']
	except:
		compare = "0"
	return response['SourceImageFace'], response['FaceMatches'], compare

if __name__== "__main__":
  main()

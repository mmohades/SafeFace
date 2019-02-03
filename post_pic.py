'''
Posts the taken picture to the AWS
'''
import boto
import boto.s3
import sys
from boto.s3.connection import S3Connection, Bucket, Key

'''
Delete the below information when posting
'''
def main(bucket_name, image_name):
	AWS_ACCESS_KEY_ID = 'Public ACCESS ID'
	AWS_SECRET_ACCESS_KEY = 'SECRET KEY GOES HERE'

	bucket_name = str(bucket_name)
	conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)


	bucket = Bucket(conn, bucket_name)

	testfile = str(image_name)
	print ('Uploading %s to Amazon S3 bucket %s' % (testfile, bucket_name))

	def percent_cb(complete, total):
	    sys.stdout.write('.')
	    sys.stdout.flush()


	k = Key(bucket)
	k.key = str(image_name)
	k.set_contents_from_filename(testfile,cb=percent_cb, num_cb=10)


if __name__== "__main__":
  main()

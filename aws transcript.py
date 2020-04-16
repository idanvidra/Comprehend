from __future__ import print_function
import time
import boto3
transcribe = boto3.client('transcribe')
job_name = "job name"
job_uri = "s3://yesandidc/transcribe-sample.5fc2109bb28268d10fbc677e64b7e59256783d3c.mp3"
#"https://yesandidc.s3-eu-west-1.amazonaws.com/transcribe-sample.5fc2109bb28268d10fbc677e64b7e59256783d3c.mp3"

transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='mp3',
    LanguageCode='en-US'
)
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)
print(status)

#https://yesandidc.s3-eu-west-1.amazonaws.com/transcribe-sample.5fc2109bb28268d10fbc677e64b7e59256783d3c.mp3
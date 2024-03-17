# aws-s3-bucket-synchronisation-srr-crr

This bucket does Same Region Replication (SRR) and Cross Region Replication (CRR).
This Repo holds the policy you need to attach to the IAM Role who's arn you need to use in the code.

This code creates a replication rule and attaches it to the bucket.

Replace the following accordingly: <code>ACCOUNT_ID</code>, <code>YOUR_ROLE</code>, <code>source-bucket-name</code>, and <code>destination-bucket-name</code>

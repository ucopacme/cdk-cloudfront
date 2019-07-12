A AWS-CDK project to build out cloudtrail periferal resources
=============================================================

Quick Start
-----------

ensure your node environnment is properly set up::

  cdk-cloudtrail> nvm current
  v11.10.0

active the local python virtual environment::

  cdk-cloudtrail> . .env/bin/activate

supply spec-file location as context var::

  cdk-cloudtrail> ckd -c spec-file=./cloudtrail-spec.sample.yaml synth

or set it as context var in ``cdk.json``::

  cdk-cloudtrail> cat cdk.json 
  {
    "app": "python3 app.py",
    "context": {
      "spec-file": "./cloudtrail-spec.sample.yaml"
    }
  }
  cdk-cloudtrail> ckd synth


Environment Setup
-----------------

nvm
***


python
******

::

  rm -rf .env
  python3 -m venv .env
  pip install -r requirements.txt



Links
-----

- https://docs.aws.amazon.com/cdk/api/latest/python/index.html
- https://github.com/aws-samples/aws-cdk-examples/tree/master/python


import setuptools


with open("README.rst") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cdk_cloudtrail",
    version="0.0.1",

    description="ACDK Python app to build CloudTrail periferal resources",
    long_description=long_description,
    long_description_content_type="text/x-rst",

    author="agould@ucop.edu",

    package_dir={"": "cdk_cloudtrail"},
    packages=setuptools.find_packages(where="cdk_cloudtrail"),

    install_requires=[
        "pyyaml",
        "aws-cdk.cdk",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)

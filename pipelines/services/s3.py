from dataclasses import dataclass


class S3Client:
    @dataclass
    class Config:
        AWS_CLIENT_ID: str
        AWS_CLIENT_SECRET: str
        AWS_BUCKET_NAME: str
        AWS_PATH_PREFIX: str

    def __init__(self, config: Config) -> None:
        self.__config = config

    def upload(self, content: bytes, content_type: str) -> None:
        print(f"Uploading to S3")

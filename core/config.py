from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    watsonx_api_key: str
    watsonx_project_id: str
    watsonx_region: str
    watsonx_model_id: str
    watsonx_url: str

    pinecone_api_key: str
    pinecone_env: str
    index_name: str

    class Config:
        env_file = ".env"

settings = Settings()

import streamlit as st
from azure.storage.blob import BlobServiceClient
from azure.cosmos import CosmosClient
import uuid
import json

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# === Azure Blob Storage Config ===
blob_account_name = os.getenv("BLOB_ACCOUNT_NAME")
blob_account_key = os.getenv("BLOB_ACCOUNT_KEY")
blob_container_name = os.getenv("BLOB_CONTAINER_NAME")

blob_service = BlobServiceClient(
    account_url=f"https://{blob_account_name}.blob.core.windows.net",
    credential=blob_account_key
)
blob_container = blob_service.get_container_client(blob_container_name)

# === Cosmos DB Config ===
cosmos_endpoint = os.getenv("COSMOS_ENDPOINT")
cosmos_key = os.getenv("COSMOS_KEY")
cosmos_db_name = os.getenv("COSMOS_DB_NAME")
cosmos_container_name = os.getenv("COSMOS_CONTAINER_NAME")

cosmos_client = CosmosClient(cosmos_endpoint, cosmos_key)
cosmos_container = cosmos_client.get_database_client(cosmos_db_name).get_container_client(cosmos_container_name)

# === UI ===
st.title("Image Tagging Pipeline")

uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Upload to blob storage
    file_name = uploaded_file.name
    blob_container.upload_blob(name=file_name, data=uploaded_file, overwrite=True)
    st.success(f"✅ Image uploaded successfully with ID: {file_name}")

    # if st.button("Upload Another Image"):
    #     st.rerun()

if st.button("📄 Show All Tags in Cosmos DB"):
    st.subheader("All Tagged Images")
    items = cosmos_container.read_all_items()
    for item in items:
        st.write(f"🖼️ Image ID: `{item['id']}`")
        st.image(item['url'], width=300)
        st.markdown("**Tags (Readable):**")
        try:
            tags = json.loads(item["tags"]) if isinstance(item["tags"], str) else item["tags"]
            for tag in tags:
                st.write(f"- {tag['name']} ({round(tag['confidence']*100, 2)}%)")
            
            st.markdown("**📋 Copyable JSON Tags:**")
            st.code(json.dumps(tags, indent=4), language='json')
        except Exception as e:
            st.warning(f"⚠️ Could not parse tags for this image. Error: {e}")


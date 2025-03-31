# Image Tagging Pipeline using Azure

This project implements a serverless, scalable image tagging and metadata storage pipeline using Azure cloud services.

## 🌐 Overview

When a user uploads an image, the system:
1. Stores it in Azure Blob Storage
2. Triggers an Azure Logic App
3. Sends the image to Azure's Computer Vision API
4. Stores the tags and metadata in Cosmos DB

Frontend is built using **Streamlit** for image upload and viewing results.

---

## 🧱 Architecture

- **Azure Blob Storage** – Stores uploaded images
- **Azure Logic Apps** – Handles the trigger and workflow
- **Azure Computer Vision API (v3.2)** – Analyzes images and returns tags
- **Azure Cosmos DB** – Stores image URL, tags, and timestamp
- **Streamlit Frontend** – For uploading images and viewing tag results

![architecture](screenshots/architecture.png)

---

## 🚀 Features

- Upload images and automatically get descriptive tags
- View all uploaded images and tags from Cosmos DB
- Secure access using SAS tokens and Azure SDKs
- Fast, serverless, and scalable

---

## 📂 Project Structure

```
image-tagging-pipeline/
├── app.py                # Streamlit frontend
├── requirements.txt      # Python dependencies
├── screenshots/          # Architecture and run screenshots
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/fernandeslder/cloud_project_frontend.git
cd cloud_project_frontend
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up `.env`
Create a `.env` file:

Fill in the following values:
- BLOB_ACCOUNT_NAME
- BLOB_ACCOUNT_KEY
- BLOB_CONTAINER_NAME
- COSMOS_ENDPOINT
- COSMOS_KEY
- COSMOS_DB_NAME
- COSMOS_CONTAINER_NAME

### 4. Run the App
```bash
streamlit run app.py
```

---

## 🧪 Testing
- Upload test images using the frontend
- Confirm Logic App execution via Azure Portal
- View results in Cosmos DB (Data Explorer)

---

## 🧠 Known Issues
- Ensure images are in valid format (JPG/PNG)
- Logic App errors can occur if SAS generation or API call fails

---

## 📸 Screenshots
- Logic App Designer
- Cosmos DB Document Output
- Streamlit Interface

All screenshots are available in `/screenshots/`

---

## 📜 License
MIT License

---

## 🙋‍♂️ Authors
Akshit Kalita
Leander Fernandes
Raju Deb
Sadman Saqib



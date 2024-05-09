# Medical Chatbot Readme

## 1. Introduction

In today's fast-paced world, access to healthcare information and services is essential for ensuring timely and effective medical assistance. With the growing demand for efficient healthcare solutions, we have developed a Medical Chatbot designed to revolutionize the way individuals interact with healthcare resources. Our chatbot is a friendly helper for health concerns, providing personalized advice, understanding of possible illnesses, and connecting users with healthcare info and resources.

## 2. Problem Statement

In the healthcare domain, one of the significant challenges is the accessibility of medical information and guidance, especially in situations where individuals experience symptoms but may not have immediate access to healthcare professionals. This lack of accessibility can lead to uncertainty and anxiety about one's health status, potentially delaying necessary medical intervention and treatment. A chatbot solution is well-suited to address this challenge due to its 24/7 availability, instant response, personalized interaction, scalability, and educational capabilities.

## 3. Solution Approach

### Architecture

#### Backend
- Data Integration
- Data Extraction
- Creating Chunks (Potentially Larger Than Token Size)
- Embeddings (Any Kind of Vector)
- Build Semantic Index (By Combining All the Vectors)
- Knowledge Base (Using Pinecone for Vector Store)

#### Frontend
- Data Integration
- Data Extraction
- Creating Chunks (Potentially Larger Than Token Size)
- Embeddings (Any Kind of Vector)
- Build Semantic Index (By Combining All the Vectors)
- Knowledge Base (Using Pinecone for Vector Store)

### Data Integration
Combining data from different sources or formats to provide a unified view of the data for analysis and processing.

### Data Extraction
Extracting specific information or data points from raw datasets or sources, including relevant medical information such as symptoms, diseases, and medical guidelines.

### Creating Chunks (Potentially Larger Than Token Size)
Breaking down large input texts into smaller chunks or segments for analysis, especially if the input exceeds the token limit of the model.

### Embeddings (Any Kind of Vector)
Representing a numerical representation of words or phrases in a continuous vector space to capture semantic meaning and relationships between words.

### Build Semantic Index (By Combining All the Vectors)
Constructing a semantic index or representation of the input data by combining the embeddings of individual words or phrases to efficiently retrieve relevant information.

### Knowledge Base (Using Pinecone for Vector Store)
A repository or database of structured information and knowledge stored in Pinecone for fast and efficient retrieval of relevant information by the chatbot.

### Frontend
Development of the frontend or web application interface using Flask, a lightweight web framework for Python, allowing quick and efficient creation of web applications.

### Tech Stack Used

- **Programming Language:** Python
- **Frontend/Web App:** Flask
- **LLM - Meta Llama2:** GPT 3.5 model used for processing and generating output responses based on user queries.
- **Vector DB - Pinecone:** Vector database for storing and querying embeddings or vector representations of medical concepts and data.

## Additional Steps

### Real-Time Use Video

Watch our model demonstrating real-time usage of the Medical Chatbot ![pic 2](https://github.com/rathoreashish146/AI-Innovisionaries/assets/117078265/dcdeb267-5cb6-4387-93db-b47cd27c0ca3)
.

### Architecture Flow Chart

![image arch 2](https://github.com/rathoreashish146/AI-Innovisionaries/assets/117078265/c377d1cf-09c7-4f65-9f6a-e0f0bbae64ff)

![image arch](https://github.com/rathoreashish146/AI-Innovisionaries/assets/117078265/f42f4141-d034-4ed5-9480-96626a4ba9e0)

## How to Run

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask web application using `python app.py`.
4. Access the chatbot interface through your web browser.

## Contributors

- Ashish
- Gufran Ahmed
- Alifza Siddiqui
- Komal Varshney

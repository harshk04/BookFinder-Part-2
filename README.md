# BookFinder: Autonomous LLM-based Book Recommendation Agent

## Overview

Welcome to the BookFinder application! This app demonstrates the use of Retrieval-Augmented Generation (RAG) to provide advanced book recommendations. Using cutting-edge AI technology, BookFinder leverages models like the Open Source Model from Hugging Face and BGE-Large-EN embeddings from BAAI to provide accurate and contextually relevant book suggestions.

## DEMO

https://github.com/harshk04/BookFinder-Part-2/assets/115946158/861083bd-6500-4c51-804d-914988e6033b


## Functionalities

1. **Generate Response**: Engage in a chat with the BookFinder assistant to get personalized book recommendations.
2. **Scrap Data and Store**: Use web scraping to extract book data from specific websites and store it in a vector database for future use.
3. **Store Data to Vector Database (Qdrant)**: Ingest the scraped data and the data fetched from LLM into the vector database (Qdrant) for efficient retrieval and recommendation.
4. **LoRA-based Quantization**: Enhance the efficiency of our models using LoRA (Low-Rank Adaptation). 

## Steps Involved in LoRA-based Quantization

1. **Identify Target Layers**: Determine which layers of the model will benefit most from quantization.
2. **Apply Low-Rank Decomposition**: Decompose the weights of the target layers into lower-dimensional representations.
3. **Quantize Decomposed Weights**: Convert the decomposed weights into a lower precision format (e.g., 8-bit).
4. **Fine-tune the Model**: Fine-tune the quantized model to recover any lost performance.
5. **Validate Performance**: Ensure that the quantized model performs adequately on the intended tasks.

## Project Structure

├── 1.100scraper.py

├── 2.10scraper.py

├── 3.llm.py

├── 4.ingest.py

├── 5.main.py

├── app.py

├── README.md

└── requirements.txt


### 1. 100scraper.py
This script scrapes the "Top 100 Books to Read in a Lifetime" from AbeBooks and stores the book names in `scrap1.txt`.

### 2. 10scraper.py
This script scrapes the "Top 10 Fiction Books of All Time" from LifestyleAsia and stores the book names in `scrap2.txt`.

### 3. llm.py
This script queries a large language model (LLM) to get book recommendations and stores the results in `llm.txt`.

### 4. ingest.py
This script ingests the data from the LLM and scraped data into the vector database (Qdrant).

### 5. main.py
This script performs a semantic search with caching using Qdrant and retrieves book recommendations based on user queries.

### app.py
This is the main Streamlit app script. It provides a web interface for users to interact with the BookFinder system.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/harshk04/BookFinder.git
    cd BookFinder
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

## Usage

### Home
Provides an overview of the functionalities offered by the BookFinder application.

### Scrap Data and Store
- **Scrap Top 100 Books Data**: Scrape data from AbeBooks.
- **Scrap Top 10 Books Data**: Scrape data from LifestyleAsia.
- **Run Query on LLM**: Execute a query on the LLM hosted on Hugging Face's open-source platform.
- **Store Data to Vector Database (Qdrant)**: Ingest data into the vector database.

### Generate Response
Start a chat with the BookFinder assistant to get personalized book recommendations.

### Contact Me
Fill out the form to get in touch with the developer.

## Contributing

Feel free to open issues or submit pull requests if you find bugs or have suggestions for improvements.

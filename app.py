import os
os.environ["USE_TF"] = "0"

import streamlit as st
import subprocess
import pandas as pd
from streamlit_option_menu import option_menu

def run_script(script_name, user_input=None):
    """Run a script and return its output."""
    if user_input:
        result = subprocess.run(["python", script_name, user_input], capture_output=True, text=True)
    else:
        result = subprocess.run(["python", script_name], capture_output=True, text=True)
    return result.stdout

with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>Welcome</h1>", unsafe_allow_html=True)
    page = option_menu(
        "Navigation", 
        ["Home","Scrap Data and Store", "Generate Response" , "Contact Me"],
        icons=["house", "download", "search", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

    st.sidebar.success("This app demonstrates Retrieval-Augmented Generation (RAG) using the Hugging Face Open Source Model.")
    st.sidebar.warning("Developed by [Harsh Kumawat](https://www.linkedin.com/in/harsh-k04/)")

if page == "Home":
    st.title("BookFinder: Autonomous LLM-based Book Recommendation Agent")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("img.jpeg", width=600, caption="LLM with RAG implementation", use_column_width=True)
    
    st.subheader("Home")
    st.success("Retrieval-Augmented Generation (RAG) using the Hugging Face Open Source Model.")
    
    st.write("Welcome to the BookFinder application. This app demonstrates the use of Retrieval-Augmented Generation (RAG) to provide advanced book recommendations. Here’s an overview of the functionalities offered:")
    
    st.write("### Functionalities:")
    st.write("1. **Generate Response**: Engage in a chat with the BookFinder assistant to get personalized book recommendations. Using cutting-edge AI technology, BookFinder leverages models like the Open Source Model from Hugging Face and BGE-Large-EN embeddings from BAAI to provide accurate and contextually relevant book suggestions.")
    st.write("2. **Scrap Data and Store**: Use web scraping to extract book data from specific websites and store it in a vector database for future use. The scraping scripts pull data from the following sources:")
    st.write("    - [Top 100 Books](https://www.abebooks.com/books/100-books-to-read-in-lifetime/)")
    st.write("    - [Top 10 Fiction Books](https://www.lifestyleasia.com/ind/shop/more/best-fiction-books-of-all-time/)")
    st.write("3. **Store Data to Vector Database (Qdrant)**: Ingest the scraped data and the data fetched from LLM into the vector database (Qdrant) for efficient retrieval and recommendation.")
    st.write("4. **LoRA-based Quantization**: Enhance the efficiency of our models using LoRA (Low-Rank Adaptation). LoRA-based quantization involves reducing the model size and improving efficiency without significant loss in performance. This technique ensures that BookFinder operates swiftly and effectively even with limited resources.")
    
    st.write("### Steps Involved in LoRA-based Quantization:")
    st.write("1. **Identify Target Layers**: Determine which layers of the model will benefit most from quantization.")
    st.write("2. **Apply Low-Rank Decomposition**: Decompose the weights of the target layers into lower-dimensional representations.")
    st.write("3. **Quantize Decomposed Weights**: Convert the decomposed weights into a lower precision format (e.g., 8-bit).")
    st.write("4. **Fine-tune the Model**: Fine-tune the quantized model to recover any lost performance.")
    st.write("5. **Validate Performance**: Ensure that the quantized model performs adequately on the intended tasks.")
    
    st.write("BookFinder was created with the user in mind, combining the effectiveness of AI-driven recommendation algorithms with natural user interfaces to improve the book discovery experience.")

elif page == "Generate Response":
    st.title("BookFinder: Autonomous LLM-based Book Recommendation Agent")

    st.subheader("Start Chatting with the Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! How can I assist you today?"}
        ]


    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Say something"):

        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            with st.spinner("Generating response..."):
                
                response = run_script("5.main.py", prompt)
                full_response += response
                message_placeholder.markdown(full_response)

                
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
                

elif page == "Scrap Data and Store":
    st.title("Scrap Data and Store in Vector Database")
    st.markdown("***")
    st.write("This button activates a web scraping script using BeautifulSoup to extract data from the webpage https://www.abebooks.com/books/100-books-to-read-in-lifetime/. It then displays both the webpage's image and the scraped data for verification purposes.")
    if st.button("Scrap Top 100 Books Data"):
        with st.spinner("Scraping Top 100 Books..."):
            output_100 = run_script("1.100scraper.py")
            st.success("Top 100 Books Scraped Successfully!")
            st.info("Data Source: https://www.abebooks.com/books/100-books-to-read-in-lifetime/ ")
            with open('scrap1.txt', 'r') as file:
                book_names_100 = file.readlines()
                df_100 = pd.DataFrame(book_names_100, columns=['Book Name'])
                st.dataframe(df_100)    
            st.info("Images related to the top 100 books:")
        
        img_urls = [
            'img1.png',
            'img2.png',
            'img3.png',
            'img4.png'
        ]
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image(img_urls[0], caption='WebPage Image 1')
        with col2:
            st.image(img_urls[1], caption='WebPage Image 2')

        with col3:
            st.image(img_urls[2], caption='WebPage Image 3')
        with col4:
            st.image(img_urls[3], caption='Webpage Image 4')   
    st.markdown("***") 
    st.write("This button activates a web scraping script using BeautifulSoup to extract data from the webpage  https://www.lifestyleasia.com/ind/shop/more/best-fiction-books-of-all-time/. It then displays both the webpage's image and the scraped data for verification purposes.")
    
    if st.button("Scrap Top 10 Books Data"):
        with st.spinner("Scraping Top 10 Books..."):
            output_10 = run_script("2.10scraper.py")
            st.success("Top 10 Books Scraped Successfully!")
            st.info("Data Source: https://www.lifestyleasia.com/ind/shop/more/best-fiction-books-of-all-time/ ")
            with open('scrap2.txt', 'r') as file:
                book_names_10 = file.readlines()
            df_10 = pd.DataFrame(book_names_10, columns=['Book Name'])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.dataframe(df_10.head(11))
        with col2:
            st.image("img5.png", width=500, caption='WebPage Image 1')
    st.markdown("***") 
    st.write("This button executes a query on a large language model (LLM) hosted on Hugging Face's open-source platform, storing the response to be loaded into a vector database (Qdrant).")
    if st.button("Run Query on LLM"):
        with st.spinner("Fetching data from LLM..."):
            output_llm = run_script("3.llm.py")
            st.success("Data fetched from LLM successfully!")
            st.text(output_llm)

    st.markdown("***")
    st.write("This button ingests the data fetched from the LLM and the scraped data into the vector database (Qdrant).")
    if st.button("Store Data to Vector Database (Qdrant)"):
        with st.spinner("Ingesting data to vector DB..."):
            output_ingest = run_script("4.ingest.py")
            st.success("Data ingested to vector DB successfully!")
            st.text(output_ingest)

if page == "Contact Me":
    st.title("BookFinder: Autonomous LLM-based Book Recommendation Agent")


    st.header("Contact Me")
    st.write("Please fill out the form below to get in touch with me.")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message", height=150)

    if st.button("Submit"):
        if name.strip() == "" or email.strip() == "" or message.strip() == "":
            st.warning("Please fill out all the fields.")
        else:
            send_email_to = 'kumawatharsh2004@gmail.com'
            st.success("Your message has been sent successfully!")

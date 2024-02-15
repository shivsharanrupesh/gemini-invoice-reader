import streamlit as st
from PIL import Image
from vertexai.preview.generative_models import GenerativeModel, Part
from datetime import datetime
from dotenv import load_dotenv
from google.cloud import storage
from io import BytesIO

load_dotenv()

model = GenerativeModel(model_name="gemini-pro-vision")

# Functions
def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image, prompt])
    return response.text

def upload_image(source_file_name):
    bucket_name = 'heispv'
    unique_value = datetime.now().strftime("%Y%m%d%H%M%S%f")
    destination_blob_name = unique_value + '.jpg'

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

# Open the image using PIL
    image = Image.open(source_file_name)

    # Convert the image to RGB if it's not
    if image.mode != 'RGB':
        image = image.convert('RGB')

    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)

    # Upload the image
    blob.upload_from_file(buffer, content_type='image/jpeg')

    return "gs://heispv/" + destination_blob_name
    


# Streamlit application
st.set_page_config(page_title="Multilanguage Invoice Extractor")

st.header("Multilanguage Invoice Extractor")
input_text = st.text_input("Input prompt", key="input")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about the image")

input_prompt = """
I have uploaded a photo of an invoice. Please examine the details in the image and be ready to answer various questions about it. These questions might pertain to the invoice's date, the items or services listed, the quantities, prices, total amount, the vendor's information, payment terms, and any discounts or taxes applied. Analyze the invoice thoroughly to ensure accuracy in your responses to any specific queries I might have about its contents.
"""

if submit:
    file_GPC = upload_image(uploaded_file)
    input_image = Part.from_uri(file_GPC, mime_type="image/jpeg")
    response = get_gemini_response(input_prompt, input_image, input_text)
    st.subheader("The Response is")
    st.write(response)
    
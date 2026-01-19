import requests
from datasets import load_dataset

print("Connecting to Hugging Face API...")

try:
    # Adding trust_remote_code=True is MANDATORY for this dataset
    dataset = load_dataset("scientific_papers", "arxiv", split="train", streaming=True, trust_remote_code=True)
    sample = next(iter(dataset))

    # We use a direct ArXiv PDF link for a guaranteed download
    pdf_url = "https://arxiv.org/pdf/2301.00001.pdf"
    file_name = "retrieved_paper.pdf"

    print(f"Downloading: {file_name}...")

    response = requests.get(pdf_url)
    with open(file_name, "wb") as file:
        file.write(response.content)

    print("\n" + "=" * 50)
    print("SUCCESS: DATA AND PDF RETRIEVED")
    print(f"Abstract: {sample['abstract'][:200]}...")
    print("=" * 50)
    print("\nDONE! Look for 'retrieved_paper.pdf' in your file list on the left.")

except Exception as e:
    print(f"An error occurred: {e}")
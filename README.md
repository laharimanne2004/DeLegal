# DeLegal — AI-Powered Legal Document Simplifier

**DeLegal** is an AI-based application that simplifies complex legal documents into plain, understandable language. Designed with accessibility and clarity in mind, the tool supports multiple Indian languages (including Hindi and Telugu) and provides a visual timeline of legal events derived from the document. DeLegal is built using modern NLP techniques and deployed using Streamlit.

---

## Features

- **Legal Document Simplification**  
  Translates dense legal language into simplified summaries using transformer-based models.

- **Multilingual Support**  
  Supports English, Hindi, and Telugu using SentencePiece tokenization and Hugging Face translation models.

- **Visual Timeline Generation**  
  Extracts relevant dates and generates an interactive timeline representing key legal events.

- **Download Options**  
  Users can export the simplified content in `.txt` or `.pdf` format for offline use.

- **Streamlined User Interface**  
  Built using Streamlit with an emphasis on clarity, responsiveness, and ease of use.

---

## Tech Stack

- Python 3.10  
- Streamlit  
- Hugging Face Transformers  
- SentencePiece  
- spaCy / NLTK  
- Matplotlib / Plotly (for timeline visualization)

---

## Live Demo

**[Access the application here](https://your-deployment-url.streamlit.app)**  
(Replace this link with your actual Streamlit Cloud deployment URL.)

---

## Screenshots

| Simplification Interface | Timeline Visualization |
|--------------------------|------------------------|
| ![Simplify UI](screenshots/simplify_ui.png) | ![Timeline UI](screenshots/timeline_ui.png) |

_(Replace these paths with your actual screenshots if available.)_

---

## Installation

To run the project locally:

```bash
git clone https://github.com/your-username/DeLegal.git
cd DeLegal
pip install -r requirements.txt
streamlit run app.py

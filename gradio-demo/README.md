# Gradio Demo App ✅

This is a minimal demo app using Gradio with two tabs:

- **Text**: reverse input text
- **Image**: apply grayscale or edge detection to an uploaded image

---

## Setup

1. Create a virtual environment (recommended):

```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Open the local URL printed in the console (usually http://127.0.0.1:7860).

---

## Notes

- Built with `gradio` and `Pillow` (PIL).
- Also includes a Streamlit port at `streamlit_app.py` and `streamlit` is listed in `requirements.txt`.

### Deploying on Streamlit Community Cloud (share.streamlit.io)
1. Push your repo to GitHub (include `streamlit_app.py` and `requirements.txt`).
2. Visit https://share.streamlit.io and create a new app.
3. Select your repo, branch, and set the app file to `streamlit_app.py` (not `app.py`).
4. Streamlit will build from `requirements.txt` and deploy; the app URL will be provided by Streamlit.

- Tell me if you want: example inputs, a simple demo image, or deployment instructions for other platforms (Heroku, Railway, or Gradio Spaces).
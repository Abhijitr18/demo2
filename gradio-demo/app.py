"""Simple Gradio demo app
- Text tab: reverse input text
- Image tab: grayscale and edge-detection

Run: python app.py
"""

from PIL import Image, ImageOps, ImageFilter
import gradio as gr


def reverse_text(text: str) -> str:
    """Return reversed text (handle empty/None)."""
    if not text:
        return ""
    return text[::-1]


def to_grayscale(img: Image.Image) -> Image.Image:
    if img is None:
        return None
    return ImageOps.grayscale(img)


def edge_detect(img: Image.Image) -> Image.Image:
    if img is None:
        return None
    # convert to grayscale first for clearer edges
    return img.convert("L").filter(ImageFilter.FIND_EDGES)


with gr.Blocks(title="Gradio Demo App") as demo:
    gr.Markdown("# ✅ Gradio Demo App")

    with gr.Tab("Text"):
        txt_in = gr.Textbox(lines=3, label="Enter text to reverse")
        txt_out = gr.Textbox(label="Reversed text")
        btn = gr.Button("Reverse")
        btn.click(reverse_text, txt_in, txt_out)

    with gr.Tab("Image"):
        img_in = gr.Image(type="pil", label="Upload an image")
        with gr.Row():
            btn_gray = gr.Button("Grayscale")
            btn_edge = gr.Button("Edge detect")
        img_out = gr.Image(label="Output image")
        btn_gray.click(to_grayscale, img_in, img_out)
        btn_edge.click(edge_detect, img_in, img_out)

    gr.Markdown("---\nBuilt with `gradio` and `Pillow` (PIL)")


if __name__ == "__main__":
    # For local development, run: python app.py
    demo.launch(share=True)
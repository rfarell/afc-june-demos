import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Homepage",
        page_icon="👋",
    )

    st.write("# AFC June 30th DEDRECON Demos 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Demos for our proposed targets:
        - Enhancement of EO/IR and RGB video data (multispectral and hyperspectral).  
        - Real-time tracking and recognition in EO/IR and RGB video data.

        Image Enhancement is concerned with improving the interpretability or perception of information in images for human viewers and providing better input for other automated image processing techniques. The principal objective of Image Enhancement is to modify the attributes of an image to make it more suitable for a given task and a specific observer.\footnote{https://paperswithcode.com/task/image-enhancement}

        Object tracking is the task of taking an initial set of object detections, creating a unique ID for each of the initial detections, and then tracking each of the objects as they move around frames in a video, maintaining the ID assignment. State-of-the-art methods involve fusing data from RGB and event-based cameras to produce more reliable object tracking. CNN-based models using only RGB images as input are also effective. The most popular benchmark is OTB. Several evaluation metrics are specific to object tracking, including HOTA, MOTA, IDF1, and Track-mAP.\footnote{https://paperswithcode.com/task/object-tracking}

        Our primary contributions and new firsts in deep and reinforcement learning are
        - High-fidelity latent space construction in variational autoencoders.
        - Hyperparameter balanced controlled training of variational autoencoders.
        - Explainable deep and reinforcement learning.
    """
    )


if __name__ == "__main__":
    run()

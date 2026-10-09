"""TechNest RAG Evaluation Pipeline.

Run with:
    streamlit run app.py
"""

import streamlit as st

from ui.state import init_session_state
from ui.sidebar import render_sidebar
from ui.tabs.catalog import render_catalog_tab
from ui.tabs.goldens import render_goldens_tab
from ui.tabs.pipeline import render_pipeline_tab
from ui.tabs.results import render_results_tab


def main() -> None:
    """Initialize the application and render its tabs."""

    st.set_page_config(
        page_title="TechNest RAG Evaluator",
        page_icon="🛒",
        layout="wide",
    )

    st.title("🛒 TechNest — RAG Evaluation & Monitoring")

    st.caption(
        "Build a RAG system over a product catalog and evaluate it "
        "using RAGAS 0.4.3 across five metrics."
    )

    init_session_state()
    render_sidebar()

    tabs = st.tabs(
        ["📚 Catalog", "🎯 Goldens", "🚀 Run Evaluation", "📊 Results"]
    )

    renderers = (
        render_catalog_tab,
        render_goldens_tab,
        render_pipeline_tab,
        render_results_tab,
    )

    for tab, render in zip(tabs, renderers):
        with tab:
            render()


if __name__ == "__main__":
    main()
import streamlit as st
from utilities import GEMINI_MODELS, init_session_state, encode_pdf
from gemini_interface import (
    initialize_gemini,
    analyze_pdf_content,
    process_query_stream,
)


def main():
    st.title("📚 Research Paper Analyst ✍")
    init_session_state()

    # Sidebar configuration
    with st.sidebar:
        st.header("⚙️ Configuration")

        # Model selection
        st.subheader("🤖 Model Selection")
        selected_model_name = st.selectbox(
            "Choose Gemini Model",
            options=list(GEMINI_MODELS.keys()),
            help="Select the Gemini model you want to use for analysis",
        )
        model_id = GEMINI_MODELS[selected_model_name]
        st.session_state.selected_model = model_id

        # Initialize the model once API key is provided
        if st.session_state.selected_model:
            st.session_state.model = initialize_gemini(st.session_state.selected_model)

        # File Upload
        st.subheader("📤 File Upload")
        uploaded_file = st.file_uploader("Upload Research Paper (PDF)", type=["pdf"])

        if uploaded_file is not None:
            pdf_content = encode_pdf(uploaded_file.read())
            st.session_state.pdf_content = pdf_content

            if st.button("✅ Analyze Paper"):
                if st.session_state.model:
                    st.session_state.messages = []  # Clear previous messages
                    st.session_state.start_analysis = True

        # Clear chat button
        if st.button("🧹 Clear Chat"):
            st.session_state.messages = []
            st.rerun()

    # Perform analysis in the main area
    if st.session_state.start_analysis:
        if st.session_state.model and st.session_state.pdf_content:
            with st.spinner("Analyzing research paper..."):
                message_placeholder = st.empty()
                full_response = []
                for chunk in analyze_pdf_content(
                    st.session_state.model, st.session_state.pdf_content
                ):
                    if hasattr(chunk, "text") and chunk.text:
                        full_response.append(chunk.text)
                        message_placeholder.markdown("".join(full_response))

            notes = "".join(full_response)
            st.session_state.notes = notes
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": "📑 Research Paper Analysis\n\n" + notes,
                }
            )
        st.session_state.start_analysis = False

    # Main chat interface
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input and streaming response
    prompt = st.chat_input("Ask a question about the paper")
    if prompt:
        if not st.session_state.pdf_content or not st.session_state.notes:
            st.error("Please upload a PDF first and analyze it!")
            return

        if not st.session_state.model:
            st.error("Please configure your API key first!")
            return

        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Process streaming response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = []

            for chunk in process_query_stream(
                st.session_state.model,
                st.session_state.pdf_content,
                st.session_state.notes,
                prompt,
            ):
                text = getattr(chunk, "text", None) if hasattr(chunk, "text") else None
                if isinstance(chunk, str):
                    text = chunk
                if text:
                    full_response.append(text)
                    message_placeholder.markdown("".join(full_response))

            complete_response = "".join(full_response)
            st.session_state.messages.append(
                {"role": "assistant", "content": complete_response}
            )

    # Welcome message
    if not st.session_state.messages:
        st.info(
            "👋 Welcome! Please upload a research paper PDF in the sidebar and click 'Analyze Paper' to get started."
        )


if __name__ == "__main__":
    main()

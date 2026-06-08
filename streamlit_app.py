# Learning Git 


import streamlit as st
import ollama

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="AI Study Notes Generator",
    page_icon="🤖",
    layout="centered"
)

# -------------------------
# Header
# -------------------------
st.title("🤖 AI Study Notes Generator")
st.caption("Powered by Ollama + Gemma 3")

# -------------------------
# Sidebar
# -------------------------
with st.sidebar:
    st.header("📖 About")
    st.write(
        """
        Generate concise study notes on any topic using a local LLM
        powered by Ollama and Gemma 3.
        """
    )

    st.markdown("---")

    st.write("### Features")
    st.write("✅ AI-generated notes")
    st.write("✅ Download notes")
    st.write("✅ Runs locally")
    st.write("✅ Powered by Ollama")

# -------------------------
# Input
# -------------------------
topic = st.text_input(
    "Enter a topic",
    placeholder="Example: Machine Learning"
)

# -------------------------
# Generate Button
# -------------------------
if st.button("Generate Notes", use_container_width=True):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        with st.spinner("Generating notes..."):

            response = ollama.chat(
                model="gemma3:1b",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
Write concise study notes about {topic}.

Format:
1. Definition
2. Key Points
3. Examples
4. Summary

Keep the notes easy to understand.
"""
                    }
                ]
            )

        notes = response["message"]["content"]

        st.success("Notes generated successfully!")

        st.subheader("📚 Study Notes")

        with st.container(border=True):
            st.markdown(notes)

        st.download_button(
            label="📥 Download Notes",
            data=notes,
            file_name=f"{topic}_notes.txt",
            mime="text/plain",
            use_container_width=True
        )

# -------------------------
# Footer
# -------------------------
st.divider()

st.caption(
    "Built using Streamlit, Ollama and Gemma 3"
)

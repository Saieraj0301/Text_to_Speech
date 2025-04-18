import os
import torch
import asyncio
import streamlit as st
from Pipeline import pipeline

# --- Compatibility Fix ---
torch.classes.__path__ = [os.path.join(torch.__path__[0], "classes")]
try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# --- Streamlit App ---
def main():
    st.set_page_config(page_title="TextToTalk", layout="centered")
    st.title("🧠 TextToTalk: Summarize + Translate + Text-to-Speech")

    st.markdown("#### ✍️ Enter your text below:")
    user_text = st.text_area("", placeholder="Paste your text here...", height=300)

    lang_code = st.selectbox("🎙️ Choose Output Language for Audio", options=["en", "es", "fr", "de"], index=0)

    use_summary = st.checkbox("🔍 Summarize before Audio Conversion", value=True)

    summary_strength = 50
    if use_summary:
        summary_strength = st.slider("🪄 Summarization Strength", min_value=1, max_value=100, value=50, step=1)

    if st.button("🔊 Generate Audio"):
        if not user_text.strip():
            st.error("🚫 Please enter some text.")
            return

        with st.spinner("⏳ Processing..."):
            audio_file, final_text, original_wc, summarized_wc = pipeline(
                user_text,
                lang=lang_code,
                use_summary=use_summary,
                strength=summary_strength,
                translate_before_tts=True
            )

        st.success("✅ Processing Complete!")

        st.subheader("📝 Final Processed Text")
        st.write(final_text[:1500] + "..." if len(final_text) > 1500 else final_text)
        st.markdown(f"**Original Word Count**: `{original_wc}`")
        st.markdown(f"**Summarized Word Count**: `{summarized_wc}`")

        st.download_button("📄 Download Text (.txt)", data=final_text, file_name="summary.txt")
        st.code(final_text, language="markdown")

        if audio_file:
            st.subheader("🎧 Audio Output")
            st.audio(audio_file, format='audio/mp3')
            st.download_button("⬇️ Download MP3", audio_file, "output.mp3", mime="audio/mp3")
        else:
            st.error("⚠️ Something went wrong during audio generation.")

if __name__ == "__main__":
    main()

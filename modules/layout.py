import streamlit as st

class Layout:
    
    def show_header(self, types_files):
        """
        Displays the header of the app
        """
        st.markdown(
            f"""
            <h1 style='text-align: center;'> SW-File-Reader</h1>
            <h3 style='text-align: center;'> 在左边上传文件，ChatGPT会回答这个文件里面的内容</h3>
            """,
            unsafe_allow_html=True,
        )

    def prompt_form(self):
        """
        Displays the prompt form
        """
        with st.form(key="my_form", clear_on_submit=True):
            user_input = st.text_area(
                "Query:",
                placeholder="你要问什么内容？",
                key="input",
                label_visibility="collapsed",
            )
            submit_button = st.form_submit_button(label="发送")
            
            is_ready = submit_button and user_input
        return is_ready, user_input
    

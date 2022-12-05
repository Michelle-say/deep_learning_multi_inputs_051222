import sqlite3
import sys
import pandas as pd
import streamlit as st
import requests



def main():
    def authentification():
        """Returns `True` if the user had the correct mail and password.""" 
        def password_entered():
            """Checks whether a password and a entered by the user is correct."""
            if (
                st.session_state["username"] in st.secrets["passwords"]
                and st.session_state["password"]
                == st.secrets["passwords"][st.session_state["username"]]
            ):
                st.session_state["password_correct"] = True
                # del st.session_state["password"]  # don't store username + password
                # del st.session_state["username"]
            else:
                st.session_state["password_correct"] = False

        if "password_correct" not in st.session_state:
            # First run, show inputs for username + password.
            st.text_input("Username", on_change=password_entered, key="username")
            st.text_input(
                "Password", type="password", on_change=password_entered, key="password"
            )
            return False
        elif not st.session_state["password_correct"]:
            # Password not correct, show input + error.
            st.text_input("Username", on_change=password_entered, key="username")
            st.text_input(
                "Password", type="password", on_change=password_entered, key="password"
            )
            st.error("😕 User not known or password incorrect")
            return False
        else:
            # Password correct.
            if st.session_state["username"] in ["bourez.rudy@gmail.com","manondoublier@yahoo.fr"]:
                st.session_state["admin"] = True
            else:
                st.session_state["admin"] = False
            st.session_state["username"] = st.session_state["username"]
            return True


    if authentification():
        st.markdown(f'<p style="text-align:right">Welcome back, {st.session_state["username"]}<p>', unsafe_allow_html=True)
       
            
if __name__ == '__main__':
    if st.runtime.exists():

        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(st.cli.main())
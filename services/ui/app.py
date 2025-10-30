"""Streamlit UI for credit and asset appraisal workflows."""
from __future__ import annotations

import datetime
from typing import Literal

import streamlit as st

st.set_page_config(
    page_title="AI Agent Sandbox",
    layout="wide",
)

AgentChoice = Literal["credit", "asset"]


def _init_session_state() -> None:
    st.session_state.setdefault("stage", "landing")
    st.session_state.setdefault("selected_agent", "credit")
    st.session_state.setdefault("login_target", "credit_agent")
    st.session_state.setdefault(
        "user_info",
        {"name": "", "email": "", "timestamp": datetime.datetime.utcnow().isoformat()},
    )


def _set_agent(agent: AgentChoice) -> None:
    st.session_state.selected_agent = agent
    st.session_state.login_target = "asset_agent" if agent == "asset" else "credit_agent"
    st.session_state.stage = "login"
    st.experimental_rerun()


def _login(user: str, email: str) -> None:
    st.session_state.user_info = {
        "name": user,
        "email": email,
        "timestamp": datetime.datetime.utcnow().isoformat(),
    }
    st.session_state.stage = st.session_state.login_target
    st.experimental_rerun()


def _render_landing() -> None:
    st.title("Open AI Agent Sandbox")
    st.write("Launch an appraisal workflow to get started.")
    if st.button("View agents"):
        st.session_state.stage = "agents"
        st.experimental_rerun()
    st.stop()


def _render_agents() -> None:
    st.title("Available agents")
    col_credit, col_asset = st.columns(2)
    with col_credit:
        st.subheader("Credit Appraisal Agent")
        st.write("Explainable AI for loan decisioning.")
        if st.button("Launch credit workflow"):
            _set_agent("credit")
    with col_asset:
        st.subheader("Asset Appraisal Agent")
        st.write("Market-driven collateral valuation.")
        if st.button("Launch asset workflow"):
            _set_agent("asset")
    if st.button("Back to landing"):
        st.session_state.stage = "landing"
        st.experimental_rerun()
    st.stop()


def _render_login() -> None:
    agent = st.session_state.selected_agent
    title = "Asset" if agent == "asset" else "Credit"
    st.title(f"Login to {title} Appraisal Platform")
    user = st.text_input("Username", key="login_user")
    email = st.text_input("Email", key="login_email")
    pwd = st.text_input("Password", type="password", key="login_password")
    if st.button("Login"):
        if user.strip() and email.strip():
            _login(user.strip(), email.strip())
        else:
            st.error("Please provide both username and email.")
    if st.button("Back to agents"):
        st.session_state.stage = "agents"
        st.experimental_rerun()
    st.stop()


def _render_credit_workflow() -> None:
    st.title("Credit Appraisal Workflow")
    st.success("You are now in the credit appraisal workflow.")


def _render_asset_workflow() -> None:
    st.title("Asset Appraisal Workflow")
    st.success("You are now in the asset appraisal workflow.")
    st.info(
        "This dedicated asset flow ensures collateral valuation features are shown "
        "instead of the credit appraisal steps."
    )
    st.stop()


def main() -> None:
    _init_session_state()

    stage = st.session_state.stage
    if stage == "landing":
        _render_landing()
    if stage == "agents":
        _render_agents()
    if stage == "login":
        _render_login()
    if stage == "asset_agent":
        _render_asset_workflow()
    else:
        _render_credit_workflow()


if __name__ == "__main__":
    main()

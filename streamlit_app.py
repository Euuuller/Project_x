import streamlit as st

st.set_page_config(
    page_title="Curry Company Dashboard",
    page_icon="🍛",
    layout="wide"
)

st.title("🍛 Curry Company Dashboard")
st.markdown("---")

st.markdown(
    """
    Bem-vindo ao Dashboard da Curry Company!
    
    Use o menu lateral para navegar entre as diferentes páginas:
    - **Home**: Página inicial com informações gerais
    - Outras páginas podem ser adicionadas no diretório `pages/`
    
    ### Como usar:
    1. Selecione uma página no menu lateral
    2. Configure os filtros disponíveis
    3. Visualize os dados e métricas
    """
)

st.sidebar.success("Selecione uma página acima.")
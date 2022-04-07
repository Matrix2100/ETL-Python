from database.database import get_session_operacional
from classes.classes_operacional import *


def extrair():
    try:
        base = get_session_operacional()
        locadora = {
            "artistas": [i for i in base.query(Artistas).all()],
            "copias": [i for i in base.query(Copias).all()],
            "gravadoras": [i for i in base.query(Gravadoras).all()],
            "itensLocados": [i for i in base.query(Itens_Locacoes).all()],
            "locacoes": [i for i in base.query(Locacoes).all()],
            "socios": [i for i in base.query(Socios).all()],
            "tiposSocios": [i for i in base.query(Tipos_Socios).all()],
            "titulos": [i for i in base.query(Titulos).all()],

        }

        # locadora = {
        #     'artistas': session_operacional.query(Artistas).all(),
        #     'copias': session_operacional.query(Copias).all(),
        #     'gravadoras': session_operacional.query(Gravadoras).all(),
        #     'itens_locacoes': session_operacional.query(Itens_Locacoes).all(),
        #     'locacoes': session_operacional.query(Locacoes).all(),
        #     'socios': session_operacional.query(Socios).all(),
        #     'tipos_socios': session_operacional.query(Tipos_Socios).all(),
        #     'titulos': session_operacional.query(Titulos).all(),
        # }
        return locadora
    except Exception as e:
        print(f'Erro na extração: {e}')

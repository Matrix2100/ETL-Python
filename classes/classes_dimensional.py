# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, VARCHAR, CHAR, NUMERIC, Date
# from sqlalchemy.orm import sessionmaker, relationship
# from classes.classes_operacional import *
#
# base_dimensional = declarative_base()
#
#
# class DM_Artistas(base_dimensional):
#     __tablename__ = 'dm_artista'
#
#     id_art = Column(NUMERIC(4), primary_key=True)
#     tpo_art = Column(CHAR(40))
#     nac_bras = Column(CHAR(40))
#     nom_art = Column(CHAR(40))
#
#     def __init__(self, artista: Artistas) -> None:
#         super().__init__()
#         self.tpo_art = artista.tpo_art
#         self.nac_bras = artista.nac_bras
#         self.nom_art = artista.nom_art
#
#
# class DM_Gravadora(base_dimensional):
#     __tablename__ = 'dm_gravadora'
#
#     id_grav = Column(NUMERIC(4), primary_key=True)
#     nom_grav = Column(CHAR(40))
#     uf_grav = Column(CHAR(50))
#     nac_bras = Column(CHAR(30))
#
#     def __init__(self, gravadora: Gravadoras) -> None:
#         super().__init__()
#         self.nom_grav = gravadora.nom_grav
#         self.uf_grav = gravadora.uf_grav
#         self.nac_bras = gravadora.nac_bras
#
#
# class DM_Socio(base_dimensional):
#     __tablename__ = 'dm_socio'
#
#     id_soc = Column(NUMERIC(4), primary_key=True)
#     nom_soc = Column(CHAR(40))
#     tipo_soc = Column(CHAR(40))
#
#     def __init__(self, socio: Socios, tipos_socios: Tipos_Socios) -> None:
#         super().__init__()
#         self.nom_soc = socio.nom_soc
#         self.tipo_soc = tipos_socios.dsc_tps
#
#
# class DM_Tempo(base_dimensional):
#     __tablename__ = 'dm_tempo'
#
#     id_tempo = Column(NUMERIC(6), primary_key=True)
#     nu_ano = Column(NUMERIC(4))
#     nu_mes = Column(NUMERIC(2))
#     nu_anomes = Column(NUMERIC(7))
#     sg_mes = Column(CHAR(3))
#     nm_mesano = Column(CHAR(8))
#     nm_mes = Column(CHAR(15))
#     nu_dia = Column(NUMERIC(2))
#     dt_tempo = Column(Date)
#     nu_hora = Column(NUMERIC(2))
#     turno = Column(CHAR(30))
#
#     def __init__(self, locacoes: Locacoes) -> None:
#         super().__init__()
#         self.nu_ano = locacoes.dat_loc.year
#         self.nu_mes = locacoes.dat_loc.month
#         self.nu_anomes = locacoes.dat_loc.day
#         # self.sg_mes = tempo.sg_mes
#         # self.nm_mesano = tempo.nm_mesano
#         # self.nm_mes = tempo.nm_mes
#         # self.nu_dia = tempo.nu_dia
#         # self.dt_tempo = tempo.dt_tempo
#         # self.nu_hora = tempo.nu_hora
#         # self.turno = tempo.turno
#
#
# class DM_Titulo(base_dimensional):
#     __tablename__ = 'dm_titulo'
#
#     id_titulo = Column(NUMERIC(4), primary_key=True)
#     tpo_titulo = Column(CHAR(40))
#     cla_titulo = Column(CHAR(40))
#     dsc_titulo = Column(CHAR(40))
#
#     def __init__(self, titulo: Titulos) -> None:
#         super().__init__()
#         self.tpo_titulo = titulo.tpo_tit
#         self.cla_titulo = titulo.cla_tit
#         self.dsc_titulo = titulo.dsc_tit
#
#
# class FT_LOCACOES(base_dimensional):
#     __tablename__ = 'ft_locacoes'
#
#     id_soc = Column(NUMERIC(4), ForeignKey('dm_socio.id_soc'), primary_key=True)
#     id_titulo = Column(NUMERIC(6), ForeignKey('dm_titulo.id_titulo'), primary_key=True)
#     id_art = Column(NUMERIC(4), ForeignKey('dm_artista.id_art'), primary_key=True)
#     id_grav = Column(NUMERIC(4), ForeignKey('dm_gravadora.id_grav'), primary_key=True)
#     id_tempo = Column(NUMERIC(6), ForeignKey('dm_tempo.id_tempo'), primary_key=True)
#     valor_arrecadado = Column(NUMERIC(10, 2))
#     tempo_devolucao = Column(NUMERIC(10, 2))
#     multa_atraso = Column(NUMERIC(10, 2))
#
#     def __init__(self, dm_socio: DM_Socio, dm_artistas: DM_Artistas, dm_titulos: DM_Titulo, dm_gravadoras: DM_Gravadora,
#                  dm_tempos: DM_Tempo, valor_arrecadado, tempo_devolucao, multa_atraso) -> None:
#         super().__init__()
#         self.id_soc = dm_socio.id_soc
#         self.id_titulo = dm_titulos.id_titulo
#         self.id_art = dm_artistas.id_art
#         self.id_grav = dm_gravadoras.id_grav
#         self.id_tempo = dm_tempos.id_tempo
#         self.valor_arrecadado = valor_arrecadado
#         self.tempo_devolucao = tempo_devolucao
#         self.multa_atraso = multa_atraso

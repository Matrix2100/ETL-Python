from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, VARCHAR, CHAR, NUMERIC, Date
from sqlalchemy.orm import relationship
import database.database as conexao

base_operacional = declarative_base()


class Artistas(base_operacional):
    __tablename__ = 'artistas'

    cod_art = Column(NUMERIC(4), primary_key=True)
    tpo_art = Column(CHAR(1))
    nac_bras = Column(CHAR(1))
    cod_grav = Column(NUMERIC(4), ForeignKey("gravadoras.cod_grav"))
    qtd_tit = Column(NUMERIC(4))
    med_anual = Column(NUMERIC(4, 2))
    nom_art = Column(VARCHAR(40))


class Copias(base_operacional):
    __tablename__ = 'copias'

    cod_tit = Column(NUMERIC(6), ForeignKey("titulos.cod_tit"), primary_key=True)
    num_cop = Column(NUMERIC(2), primary_key=True)
    dat_aq = Column(Date)
    status = Column(CHAR(1))


class Gravadoras(base_operacional):
    __tablename__ = 'gravadoras'

    cod_grav = Column(NUMERIC(4), primary_key=True)
    uf_grav = Column(CHAR(2))
    nac_bras = Column(CHAR(1))
    nom_grav = Column(VARCHAR(40))


class Itens_Locacoes(base_operacional):
    __tablename__ = 'itens_locacoes'

    cod_soc = Column(NUMERIC(4), ForeignKey("locacoes.cod_soc"), primary_key=True)
    dat_loc = Column(Date, ForeignKey("locacoes.dat_loc"), primary_key=True)
    cod_tit = Column(NUMERIC(6), ForeignKey("copias.cod_tit"), primary_key=True)
    num_cop = Column(NUMERIC(2), ForeignKey("copias.num_cop"))
    dat_prev = Column(Date)
    val_loc = Column(NUMERIC(6, 2))
    sta_mul = Column(CHAR(1))
    dat_dev = Column(Date)


class Locacoes(base_operacional):
    __tablename__ = 'locacoes'

    cod_soc = Column(NUMERIC(4), ForeignKey("socios.cod_soc"), primary_key=True)
    dat_loc = Column(Date, primary_key=True)
    val_loc = Column(NUMERIC(5, 2))
    dat_venc = Column(Date)
    sta_pgto = Column(CHAR(1))
    dat_pgto = Column(Date)


class Socios(base_operacional):
    __tablename__ = 'socios'

    cod_soc = Column(NUMERIC(4), primary_key=True)
    dat_cad = Column(Date)
    cod_tps = Column(NUMERIC(4), ForeignKey("tipos_socios.cod_tps"))
    sta_soc = Column(CHAR(1))
    nom_soc = Column(VARCHAR(40))


class Tipos_Socios(base_operacional):
    __tablename__ = 'tipos_socios'

    cod_tps = Column(NUMERIC(4), primary_key=True)
    lim_tit = Column(NUMERIC(2))
    val_base = Column(NUMERIC(6, 2))
    dsc_tps = Column(VARCHAR(40))


class Titulos(base_operacional):
    __tablename__ = 'titulos'

    cod_tit = Column(NUMERIC(6), primary_key=True)
    tpo_tit = Column(CHAR(1))
    cla_tit = Column(CHAR(1))
    qtd_cop = Column(NUMERIC(3))
    dat_lanc = Column(Date)
    cod_art = Column(NUMERIC(4), ForeignKey("artistas.cod_art"))
    cod_grav = Column(NUMERIC(4), ForeignKey("gravadoras.cod_grav"))
    dsc_tit = Column(VARCHAR(40))

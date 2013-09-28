import sqlalchemy as sqla
import sqlalchemy.orm as orm
import db


class KeywordModel(db.Base):
    __tablename__ = "keyword"

    id = sqla.Column(sqla.BigInteger, primary_key=True, nullable=False)
    keyword = sqla.Column(sqla.String, nullable=False)

    rel_organic = orm.relationship("OrganicMapModel", lazy="joined")
    rel_competition = orm.relationship("KeywordCompetitionModel", lazy="joined")


class DomainModel(db.Base):
    __tablename__ = "domain"

    id = sqla.Column(sqla.BigInteger, primary_key=True, nullable=False)
    domain = sqla.Column(sqla.String, nullable=False)

    rel_traffic = orm.relationship("DomainTrafficModel", lazy="joined")


class DomainTrafficModel(db.Base):
    __tablename__ = "domain_traffic"

    id = sqla.Column(sqla.BigInteger, sqla.ForeignKey(DomainModel.id), primary_key=True, nullable=False)
    rank = sqla.Column(sqla.Integer, nullable=False)
    organic_keywords = sqla.Column(sqla.Integer, nullable=False)
    organic_traffic = sqla.Column(sqla.Integer, nullable=False)
    organic_cost = sqla.Column(sqla.Integer, nullable=False)
    adwords_keywords = sqla.Column(sqla.Integer, nullable=False)
    adwords_traffic = sqla.Column(sqla.Integer, nullable=False)
    adwords_cost = sqla.Column(sqla.Integer, nullable=False)


class KeywordCompetitionModel(db.Base):
    __tablename__ = "keyword_competition"

    id = sqla.Column(sqla.BigInteger, sqla.ForeignKey(KeywordModel.id), primary_key=True, nullable=False)
    search_volume = sqla.Column(sqla.BigInteger, nullable=False)
    cpc = sqla.Column(sqla.Float, nullable=False)
    competition = sqla.Column(sqla.Float, nullable=False)
    num_results = sqla.Column(sqla.BigInteger, nullable=False)


class UrlModel(db.Base):
    __tablename__ = "url"

    id = sqla.Column(sqla.BigInteger, primary_key=True, nullable=False)
    domain_id = sqla.Column(sqla.BigInteger, sqla.ForeignKey(DomainModel.id), nullable=False)
    url = sqla.Column(sqla.String, nullable=False)

    rel_domain = orm.relationship("DomainModel")


class OrganicMapModel(db.Base):
    __tablename__ = "organic_map"

    keyword_id = sqla.Column(sqla.BigInteger, sqla.ForeignKey(KeywordModel.id), primary_key=True, nullable=False)
    url_id = sqla.Column(sqla.BigInteger, sqla.ForeignKey(UrlModel.id), primary_key=True, nullable=False)
    position = sqla.Column(sqla.Integer, nullable=False)

    rel_url = orm.relationship("UrlModel", lazy="joined")

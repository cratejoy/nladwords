import db
import models


def get_domain(domain_str):
    try:
        return db.session.query(models.DomainModel).filter_by(domain=domain_str).one()
    except:
        m = models.DomainModel(domain=domain_str)
        db.session.add(m)

        return m


def get_url(url_str, domain):
    try:
        return db.session.query(models.UrlModel).filter_by(url=url_str).one()
    except:
        m = models.UrlModel(url=url_str)
        m.rel_domain = domain
        db.session.add(m)

        return m

import db
import models
import semrush


def main():
    for domain in db.session.query(models.DomainModel).all():
        if not domain.rel_traffic:
            print "Downloading traffic for", domain.domain
            try:
                res = semrush.domain_traffic(domain.domain)
            except:
                print "Failed downloading traffic for domain", domain.domain
                continue

            _, rank, organic_keywords, organic_traffic, organic_cost, adwords_keywords, adwords_traffic, adwords_cost = list(res)[0][1]
            m = models.DomainTrafficModel(
                rank=rank,
                organic_keywords=organic_keywords,
                organic_traffic=organic_traffic,
                organic_cost=organic_cost,
                adwords_keywords=adwords_keywords,
                adwords_traffic=adwords_traffic,
                adwords_cost=adwords_cost)
            domain.rel_traffic = [m]

            db.session.add(m)
            db.session.add(domain)

            try:
                db.session.commit()
            except:
                print "Failed to commit new traffic info for", domain.domain
                db.session.rollback()


if __name__ == '__main__':
    main()

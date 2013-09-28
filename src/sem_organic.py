import db
import models
import model_util
import semrush


def main():
    for kw in db.session.query(models.KeywordModel).all():
        num_organic = len(kw.rel_organic)

        if 0 == num_organic:
            print "Downloading organic results for", kw.keyword

            try:
                res = semrush.keyword_organic(kw.keyword)
            except:
                print "Failed downloading organic results for", kw.keyword
                continue

            for i, (domain_str, url_str) in res:
                print i, domain_str, url_str

                domain = model_util.get_domain(domain_str)
                url = model_util.get_url(url_str, domain)

                organic = models.OrganicMapModel(position=i, keyword_id=kw.id)
                organic.rel_url = url

                db.session.add(organic)

                try:
                    db.session.commit()
                except:
                    print "Failed to add", domain_str, url_str
                    db.session.rollback()


if __name__ == '__main__':
    main()

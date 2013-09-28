import db
import models
import semrush


def main():
    for kw in db.session.query(models.KeywordModel).all():
        if not kw.rel_competition:
            print "Downloading competition for", kw.keyword
            try:
                res = list(semrush.keyword_competition(kw.keyword))
            except:
                print "Failed downloading traffic for keyword", kw.keyword
                continue

            if not res:
                continue

            _, search_volume, cpc, competition, num_results = res[0][1]
            m = models.KeywordCompetitionModel(
                search_volume=search_volume,
                cpc=cpc,
                competition=competition,
                num_results=num_results)
            kw.rel_competition = [m]

            db.session.add(m)
            db.session.add(kw)

            try:
                db.session.commit()
            except:
                print "Failed to commit new  keyword competition info for", kw.keyword
                db.session.rollback()


if __name__ == '__main__':
    main()

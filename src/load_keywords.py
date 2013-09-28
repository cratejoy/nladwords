import sys
import db
import models


def main(in_file):
    f = open(in_file, 'r')
    lines = f.readlines()
    f.close()

    for line in lines:
        line = line.strip()
        try:
            line = line.decode("utf-8")
            line = line.encode("ascii", "replace")
        except:
            continue

        m = models.KeywordModel(keyword=line)

        try:
            db.session.add(m)
            db.session.commit()
        except:
            db.session.rollback()


if __name__ == '__main__':
    in_file = sys.argv[1]

    main(in_file)

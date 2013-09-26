# install
virtualenv --distribute venv
source venv/bin/activate
pip install -r requirements.txt

# run
python src/keywords_file.py test500.txt keywords.csv

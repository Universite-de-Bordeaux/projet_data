sudo apt install -y python3-pip
sudo apt install -y python3-setuptools
sudo apt install -y python3-venv
python3 -m venv venv
source venv/bin/activate
pip install bs4
pip install selenium
pip install requests
pip install scikit-learn
pip install pandas
pip install numpy
pip install matplotlib
pip install spacy
pip install plotly
python -m spacy download fr_core_news_md
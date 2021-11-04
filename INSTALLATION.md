---
1. Clone the github repository at the preferable location in your system. You will need git to be preinstalled in the system. Once the repository is cloned in your system, with the help of cd command ,
```
git clone https://github.com/anshulp2912/cheapBuy.git
cd cheapBuy
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the requirements.txt file. Use pip to install all of those.
```
pip install -r requirements.txt
```
3. To run the server

```
python3 code/web_scrappers/server_api.py

```
4. Load extension in the chrome by just adding the code/extension folder to the load unpacked button on the top left in chrome://extensions.
5. Run the streamlit website locally using
```
streamlit run cheapBuy_user_interface.py
```

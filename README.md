<p align="center">
  <a href="link-of-our-extension">
    <img alt="GitHub Profile Readme Generator" src="code/extension/images/cheapbuy.png" width="120" />
  </a>
</p>
<h1 align="center">
  cheapBuy
</h1>

---

**cheapBuy Extension** provides you ease to buy any product through your favourite website's like Amazon, Walmart, Ebay, Bjs, Costco, etc, by providing prices of the same product from all different websites to extension. It takes lot of time to search for the same product in different websites, and find the cheapest one, instead just add our extension **cheapBuy** and it will automatically fetch you price of the same product from different websites and you can directly compare the prices from different websites through our extension. In sum, **cheapBuy** is an one stop solution to buy the cheapest product online.

---
[![Build Status](https://app.travis-ci.com/het-patel99/cheapBuy.svg?branch=main)](https://app.travis-ci.com/github/het-patel99/cheapBuy/builds/238891348)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5540375.svg)](https://doi.org/10.5281/zenodo.5540375)
[![codecov](https://codecov.io/gh/het-patel99/cheapBuy/branch/main/graph/badge.svg?token=6D5N39DIO7)](https://codecov.io/gh/het-patel99/cheapBuy)
![github workflow](https://github.com/het-patel99/cheapBuy/actions/workflows/unit_test.yml/badge.svg)
![github workflow](https://github.com/het-patel99/cheapBuy/actions/workflows/style_checker.yml/badge.svg)
![github workflow](https://github.com/het-patel99/cheapBuy/actions/workflows/main.yml/badge.svg)
![github workflow](https://github.com/het-patel99/cheapBuy/actions/workflows/code_cov.yml/badge.svg)
![github workflow](https://github.com/het-patel99/cheapBuy/actions/workflows/close_as_a_feature.yml/badge.svg)
<!--Badges-->
<a href="https://github.com/het-patel99/cheapBuy/blob/master/LICENSE" target="blank">
<img src="https://img.shields.io/github/license/het-patel99/cheapBuy?style=flat-square" alt="cheapBuy license" />
</a>
<a href="https://github.com/het-patel99/cheapBuy/fork" target="blank">
<img src="https://img.shields.io/github/forks/het-patel99/cheapBuy?style=flat-square" alt="cheapBuy forks"/>
</a>
<a href="https://github.com/het-patel99/cheapBuy/stargazers" target="blank">
<img src="https://img.shields.io/github/stars/het-patel99/cheapBuy?style=flat-square" alt="gcheapBuy stars"/>
</a>
<a href="https://github.com/het-patel99/cheapBuy/issues" target="blank">
<img src="https://img.shields.io/github/issues/het-patel99/cheapBuy?style=flat-square" alt="cheapBuy issues"/>
</a>
<a href="https://github.com/het-patel99/cheapBuy/issues" target="blank">
<img src="https://img.shields.io/github/issues-closed/het-patel99/cheapBuy" alt="cheapBuy issues closed"/>
</a>
<a href="https://github.com/het-patel99/cheapBuy/pulls" target="blank">
<img src="https://img.shields.io/github/issues-pr/het-patel99/cheapBuy?style=flat-square" alt="cheapBuy pull-requests"/>
</a>

<a href="https://github.com/het-patel99/cheapBuy/graphs/contributors" alt="Contributors">
<img src="https://img.shields.io/github/contributors/het-patel99/cheapBuy" /></a>

<a href="https://github.com/sal0ni/cheapBuy/milestones" alt="milestones">
<img src="https://img.shields.io/github/milestones/all/het-patel99/cheapBuy" /></a> 

<a href="https://github.com/sal0ni/cheapBuy/graphs/commit-activity" alt="commit activity">
<img src="https://img.shields.io/github/commit-activity/w/het-patel99/cheapBuy" /></a> 

<a href="https://github.com/sal0ni/cheapBuy/discussions" alt="discussion">
<img src="https://img.shields.io/github/discussions/het-patel99/cheapBuy" /></a> 

<a href="https://img.shields.io/github/repo-size/het-patel99/cheapBuy" alt="repo size">
<img src="https://img.shields.io/github/repo-size/het-patel99/cheapBuy" /></a>

<a href="https://img.shields.io/tokei/lines/github/het-patel99/cheapBuy" alt="total lines">
<img src="https://img.shields.io/tokei/lines/github/het-patel99/cheapBuy" /></a> 


<p align="center">
    <a href="https://github.com/het-patel99/cheapBuy/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/het-patel99/cheapBuy/issues/new/choose">Request Feature</a>
</p>

## 🚀 Demo 

[![cheapBuy Extension](https://img.youtube.com/vi/Rd5pno8FuD4/0.jpg)](https://www.youtube.com/watch?v=Rd5pno8FuD4)
## 🧐 Features
- **Price Comparison**
- **Get alternative website for the product**


## 🛠️ Installation Steps

---
1. Clone the github repository at the preferable location in your system. You will need git to be preinstalled in the system. Once the repository is cloned in your system, with the help of cd command ,
```
git clone https://github.com/het-patel99/cheapBuy.git
cd cheapBuy
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of those.
```
pip install -r requirements.txt
```
3. Check out the demo video to know about the use of the extension.

## Plan of Action :
## PHASE-1
1. Fetching descirption of the user's current tab for ebay.
2. Fetching descirption of the user's current tab for Walmart.
3. Fetching descirption of the user's current tab for amazon.
4. Fetching descirption of the user's current tab for Bjs.
5. Fetching descirption of the user's current tab for Costco.
6. Web Scrapping various product details from amazon.
7. Web Scrapping various product details from Ebay.
8. Exception handling of web scrapping.
9. Server API for web scrapping.
10. Deploying server on AWS.
11. Build an extension for this price comparison.
12. Extract knowledge like prices, sites, URL, comparison, description from scrapped data.
13. Show all the scrapped data and the knowledge gained on the extension page.

## PHASE-2
1. Add a badge on the user's current tab.
2. Improvement of extension UI.
3. Alternate product suggestion feature.
4. Improve accuracy of the product. Example : If user's current tab is having Television of a particular brand and there is a better option available at a cheaper or comparable rate than provide alternative product accordingly.
5. Add web scrapping for other websites such as Walmart, Bjs, Costco, etc.
6. Improve code execution speed using multithreading.
7. Show a avialable coupon on other shopping website.

## PHASE-3
1. Automatic deployment of server using Teraform or ansible.
2. Develop a website instead of extension.
3. Dashboard including how many user's click on the website.
4. Email notification of the available coupon to the user.


🌟 You are all set!

## 🍰 Contributing
Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/het=patel99/cheapBuy/compare).

Please read [`CONTRIBUTING`](CONTRIBUTING.md) for details on our [`CODE OF CONDUCT`](CODE_OF_CONDUCT.md), and the process for submitting pull requests to us.


## Contributors

<table>
  <tr>
    <td align="center"><a href="https://github.com/het-patel99"><img src="https://avatars.githubusercontent.com/u/44945317?s=400&u=c05d1c4c8cf27c526d9d8c72b0725255500591cd&v=4" width="75px;" alt=""/><br /><sub><b>Het Patel</b></sub></a></td>
    <td align="center"><a href="https://github.com/hvudeshi"><img src="https://avatars.githubusercontent.com/u/22682878?v=4" width="75px;" alt=""/><br /><sub><b>Hardik Udeshi</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/sal0ni"><img src="https://avatars.githubusercontent.com/u/37000199?v=4" width="75px;" alt=""/><br /><sub><b>Saloni Mahatma</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/kalgeekotak99"><img src="https://avatars.githubusercontent.com/u/43135408?v=4" width="75px;" alt=""/><br /><sub><b>Kalgee Kotak</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Vineet2311"><img src="https://avatars.githubusercontent.com/u/89501442?v=4" width="75px;" alt=""/><br /><sub><b>Vineet Chheda</b></sub></a><br /></td>
  </tr>
</table>

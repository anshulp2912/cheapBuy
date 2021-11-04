cheapBuy Phase 2 Improvements
<br><br>
Following are the improvements made in Phase 2 of the project:
<br><br>
1. Add web scraping for other websites:<br>
Phase 1: In the first version of the project, the comparison for any product was only provided from two websites (Amazon and ebay).
<br>
<img src = https://github.com/anshulp2912/cheapBuy/blob/main/media/Phase1-extoutput.png>
<br>
Phase 2: In Phase 2, comparison for any product is provided from five different websites (Amazon, ebay, Walmart, bjs, Costco).
<br><br><br>
2. Highlight the cheapest option:
<br><br>
Phase 1: In the previous version, the extension showed only the available options but did not highlight the cheapest option.
<br><br>
Phase 2: In the updated version, the cheapest option among the available options is highlighted in the output given in the website. <br>
<img src = "https://github.com/anshulp2912/cheapBuy/blob/main/media/highlight.jpeg"> <br>
<br><br><br>
3. Multithreading:
<br><br>
Phase 1: In phase 1, multithreading was not implemented. Speed is less and works correctly only for a few products. All the products were not working.
<br><br>
Phase 2: In phase 2, Multithreading is implemented to improve the speed of the output as well as to show all the 5 output product website pop-ups at once. This works efficiently.
<br><br><br>
4. Created a website (UI Interface):
<br><br>
Phase 1: No website Implementation in the previous version.<br><br>
Phase 2: A UI interface is created for the cheapBuy project. Used Streamlit to create the website. Given any url of the product as the input, the website gives the product list from 5 different websites (Amazon, ebay, Costco, bjs, Walmart) to compare the prices of the same product on different websites.<br><br>The below screenshot shows the website created for cheapBuy- [cheapBuy](url)
<br><br><br>
5. Chrome Extension Enhancements:<br><br>
Phase 1: Chrome Extension worked only on three specific products but did not work for other products from the same website.<br><br>
Phase 2: Chrome Extension works for any input product given from any of the five websites and the comparison will be given from the five websites we targeted (Amazon, ebay, Costco, bjs, Walmart).
<br><br> The below screenshot shows the chrome extension working - [Extension](url)
<br><br><br>
6. Improve accuracy of the product:<br><br>
Phase 1: In phase 1, for a given input url of a product, available options on two websites are given. But the accuracy of the output is less. It does not search and give the same product from the other websites.<br><br>
Phase 2: In phase 2, for any product given, the output is accurate. It gives the same product from 5 different websites.<br><br>
Example : If user's current tab is having Television of a particular brand and there is a better option available at a cheaper or comparable rate than provide alternative product accordingly.

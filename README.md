# Google Search Clone

## Overview

This is Project 0 for Harvard's CS50W: Web Programming with Python and JavaScript. The project is a clone of Google's homepage and includes functionality for:

- Standard Google search
- Advanced search
- Image search

All three features link directly to Google's real search endpoints while mimicking Google's visual design.

## Features

- **Homepage**  
  - Search bar for submitting queries to Google.
  - "Google Search" and "I'm Feeling Lucky" buttons (the latter redirects to Google's homepage).
  
- **Advanced Search Page**  
  - Allows users to specify multiple criteria:
    - All these words
    - This exact word or phrase
    - Any of these words
    - None of these words
  - Submit redirects to Google’s advanced search with the corresponding query parameters.

- **Image Search Page**  
  - Allows users to search Google Images via query input.
  - Styled similarly to Google Images homepage.

## How to Use

1. Clone or download this repository.
2. Open `index.html` in your browser to start using the homepage.
3. Use the navigation links or URLs to visit:
   - `/advancedsearch.html` – for advanced search
   - `/imagesearch.html` – for image search

> Note: This project is entirely static and uses standard HTML/CSS. All search queries are passed directly to real Google endpoints.

## Technologies

- HTML5
- CSS3
- JavaScript only used for the 'Feeling Lucky' button on the index.html normal search.

## Author

Created by fearfully_m as part of CS50W Project 0.  
Course: [CS50W – Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/)

## License

This project is for educational purposes and is not affiliated with or endorsed by Google in any way.
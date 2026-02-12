# Source and Style — Assignment 1 

## Website 
- HathiTrust - Retribution by Ida B. Luckie
- Link: https://babel.hathitrust.org/cgi/pt?id=coo.31924055965465&seq=517&q1=O+god

## Technologies
I inspected this using the browser + DevTools (and I also used HathiTrust’s text-only view to confirm what I was looking at).

At a high level, this site uses the standard web stack:
- HTML for the page structure
- CSS + JavaScript for the interactive aspects experience (page navigation, image loading etc.). One strong clue is that the codebase explicitly includes steps to “build the CSS and JavaScript” for the viewer component called pt

The GitHub repo for this exact site also shows what’s inside:
- The repository language breakdown includes Perl (majority), plus JavaScript, Svelte, and SCSS. 
- The README notes that “babel cgi apps run under apache” 

## Who built this website?
This viewer is part of HathiTrust (the “HathiTrust Digital Library” interface), which is clear from the text-only version that labels it as HathiTrust Digital Library and provides the HathiTrust contact info.

The GitHub repository metadata showed me how many people were involved. The public repository shows that there were 9 listed contributors and 9,101 commits over time.
- Link: https://github.com/hathitrust/babel
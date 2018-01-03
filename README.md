# Lockup

RevengeOfficial inspired locked website. Needs a password to access (cool for swag drops and hiding things behind passwords).

Concept: User states their "name" and knocks, if it's someone your server is "expecting" it'll "open the door" and reveal some content.

Execution: Similar to password protection, except different passwords reveal different solutions.

## Requirements

- Python 3.5+
- Sanic (`python3 -m pip install sanic`)
- `console-logging` (`python3 -m pip install console-logging`)
- a website and a web server that supports Python and Sanic
    - I haven't been able to get Sanic apps up and running in PythonAnywhere, HelioHost, or Now.sh; if you really need a free host and these are your only options, just convert the Sanic app to Flask (syntax is almost entirely the same)

## Usage

1. Edit `server/paths.json` with more JSON formatted entries containing passkeys and URLs as you see fit.

2. Upload the contents of the `server` folder to a python-enabled web server. (I recommend running using `screen`, i.e. `screen python3 app.py`, to see the initial logs and then detaching using Ctrl/CMD+A+D)

3. Change the server IP in the designated location in `public/index.html` (inside the script tag for fetch URL) to your server's IP. The other parts of the URL should stay the same unless you changed it (the server ip should be 07734 or hello backwards, and the path should be /knock). If your server is setup for HTTPS use `https://` instead of `http://`!
    - *Optional:* you may customize the HTML file if you wish, for example changing the H1 name or fonts/colors/placement etc.

4. Upload the contents of the `public` folder to your website wherever you wish; e.g. I placed mine under a directory on my website.

5. Navigate to it in your browser and verify it works if you state the passkey as your name!

## Credits

HTML/CSS based off of a button example on CodePen. Font is "Cute Notes" from DaFont.

## Shameless Plug

As with most of my work I'm not expecting a royalty or anything (especially since most of this is via the help of others!). I've licensed this using the MIT License below. If you're feeling generous, drop a link to my [website](http://priansh.com)!

I've got some more open-source web work on my GitHub profile, including a [resume](https://github.com/pshah123/resume) and [procedurally generated blog](https://github.com/pshah123/masquerade-web).

## License

Copyright 2017 Priansh Shah.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
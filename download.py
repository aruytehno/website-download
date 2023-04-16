from pywebcopy import save_website

def website(url, folder, name):
    save_website(
        url=url,
        project_folder=folder,
        project_name=name,
        bypass_robots=True,
        debug=True,
        open_in_browser=True,
        delay=None,
        threaded=False,
    )


if name == 'main':
    website('https://example.com', '/Users/your_name/IDE/', 'projekt_name')

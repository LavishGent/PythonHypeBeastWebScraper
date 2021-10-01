filenames = ['text_content/trending_stories.txt',
             'text_content/latest_stories.txt',
             'text_content/the_verge_tech.txt']
def display_articles():
    with open('text_content/all_articles.txt', 'w') as f:
        for names in filenames:
            with open(names) as infile:
                f.write(infile.read())
            f.write('''--------------------------------------------------------------
            \n''')
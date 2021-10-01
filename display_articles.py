filenames = ['text_content/trending_stories.txt', 'text_content/latest_stories.txt']

with open('text_content/latest&trending.txt', 'w') as f:
    for names in filenames:
        with open(names) as infile:
            f.write(infile.read())
        f.write('''--------------------------------------------------------------
        \n''')
def extractTags():
    taglist = list()
    f = open("DownloadTags.txt", "r")
    for line in f:
        taglist.append(int(line.strip()[-8:]))

    print(taglist)
    return taglist
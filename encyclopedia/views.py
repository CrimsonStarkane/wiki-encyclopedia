from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    print(entry)
    content = util.get_entry(entry)
    print(content)

    if content == None:
        return render(request, "encyclopedia/notfound.html")

    return render(request, "encyclopedia/entry.html", {
        "content": content
    })
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.get_entries()
    })


def entry(request, entry):
    title = util.find_entry(entry)

    if title:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": util.get_entry(title)
        })

    return render(request, "encyclopedia/notfound.html")


def display(request, entry):
    return render(request, "encyclopedia/entry.html", {
        "title": entry,
        "content": util.get_entry(entry)
    })


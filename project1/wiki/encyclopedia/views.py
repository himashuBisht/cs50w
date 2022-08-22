import re
from tabnanny import check
from django.shortcuts import render

from . import util
from markdown2 import Markdown
import random


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def get_html(entry_name):
    md = Markdown()
    entry = util.get_entry(entry_name)
    if entry:
        html = md.convert(entry)
    else:
        html = None
    return html


def entry(request, entry_name):
    html = get_html(entry_name)
    if html:
        return render(
            request,
            "encyclopedia/entry.html",
            {"entry": html, "entryTitle": entry_name},
        )
    # wrong html entry
    else:
        return render(
            request, "encyclopedia/entry_not_found.html", {"entryTitle": entry_name}
        )


def search(request):
    if request.method == "POST":
        post_input = request.POST
        input = request.POST["q"]
        # print(input)
        html = get_html(input)
        entries = util.list_entries()
        if input in entries:
            return render(
                request,
                "encyclopedia/entry.html",
                {
                    "entry": html,
                    "entryTitle": input,
                },
            )
        else:
            search_pages = []
            for entry in entries:
                if input.lower() in entry.lower():
                    search_pages.append(entry)
            return render(
                request,
                "encyclopedia/search.html",
                {"matches": search_pages, "post_input": post_input, "input":input},
            )


def new(request):
    return render(request, "encyclopedia/new.html")


def save(request):
    if request.method == "POST":
        post_input = request.POST
        input_title = request.POST["title"]
        input_text = request.POST["text"]
        entries = util.list_entries()
        check_entries = []
        for entry in entries:
            check_entries.append(entry.upper())

        # title is case insensitive
        if input_title.upper() in check_entries:
            # fetching real title name
            existing_title = entries[check_entries.index(input_title.upper())]
            return render(
                request,
                "encyclopedia/duplicate.html",
                {
                    "input_title": existing_title,
                    "input_text": input_text,
                    "post_input": post_input,
                },
            )
        else:
            util.save_entry(input_title, input_text)
            html = get_html(input_title)
            return render(
                request,
                "encyclopedia/entry.html",
                {
                    "entry": html,
                    "entryTitle": input_title,
                },
            )


def Random(request):
    ls = util.list_entries()
    entry_title = random.choice(ls)
    htmlcontent = get_html(entry_title)
    return render(
        request,
        "encyclopedia/entry.html",
        {"entryTitle": entry_title, "entry": htmlcontent},
    )


def edit(request):
    if request.method == "POST":
        input_title = request.POST["title"]
        content = util.get_entry(input_title)
        return render(
            request,
            "encyclopedia/edit.html",
            {
                "entryTitle": input_title,
                "content": content,
            },
        )


def save_edit(request):
    if request.method == "POST":
        input_title = request.POST["title"]
        input_text = request.POST["text"]

        util.save_entry(input_title, input_text)
        html = get_html(input_title)
        return render(
            request,
            "encyclopedia/entry.html",
            {
                "entry": html,
                "entryTitle": input_title,
            },
        )

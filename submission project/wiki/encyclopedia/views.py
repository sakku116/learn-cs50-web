from django.shortcuts import render
import markdown2
from django.http import HttpResponseRedirect

from . import util


def index(request):
    header = "All Pages"
    entries = util.list_entries()

    query = request.GET.get('q', None)

    if query:
        entry_results = []

        for entry in entries:
            if query.lower() in entry.lower():
                entry_results.append(entry)
            else:
                pass

        header = f"Entry Result: '{query}' ({len(entry_results)})"
    else:
        entry_results = entries

    return render(request, "encyclopedia/index.html", {
        "entries": entry_results,
        "header": header
    })

def entryPage(request, entry_name):
    entry_title = ""
    entry_content = ""

    get_entry = util.get_entry(entry_name)

    # convert markdown to html
    if get_entry != None:
        entry_title = entry_name
        entry_content = markdown2.markdown_path(f"entries/{entry_name}.md")
    else:
        entry_title = "not found"
        entry_content = "<h2 style='margin-top: 20px'> entry not found </h2>"

    return render(
        request, "encyclopedia/entry_page.html",
        {
            "entry_title": entry_title,
            "entry_content": entry_content
        }
    )

def createNewPage(request):
    if request.method == "GET":
        return render(
            request,
            "encyclopedia/create_new_page.html"
        )

    elif request.method == "POST":
        page_title = request.POST.get('page_title', None)
        page_content = request.POST.get('page_content', None)
        output_message = None

        if page_title == "":
            page_title = "untitled"

        is_exist = False

        # check whether entry title is exist
        get_entries = util.list_entries()
        for entry in get_entries:
            if page_title.lower() == entry.lower():
                is_exist = True

        if is_exist:
            output_message = f"The entry called '{page_title}' is already exist. Try creating new page using other title"
            return render(
                request,
                "encyclopedia/create_new_page.html",
                {
                    "output_meesage": output_message,
                }
            )
        else:
            util.save_entry(page_title, page_content)
            return HttpResponseRedirect(f'/wiki/{page_title}')


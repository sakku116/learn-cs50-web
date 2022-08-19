from django.shortcuts import render
import markdown2

from . import util


def index(request):
    header = "All Pages"
    entries = util.list_entries()

    query = request.GET.get('q', None)

    if query:
        header = "Page Result"
    else:
        pass

    return render(request, "encyclopedia/index.html", {
        "entries": entries,
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


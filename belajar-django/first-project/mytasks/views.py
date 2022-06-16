from django.shortcuts import render

tasks = ['foo', 'bar', 'baz']

# Create your views here.
def index(request):
    # session handling
    if "tasks" not in request.session:
        request.session["tasks"] = []

    if request.method == 'POST':
        # mendapatkan task_form value dari request POST
        new_task = request.POST.get('task_form')
        if new_task != '':
            # menggunakan session untuk menyimpan variable akan memasukkan kembali data terakhir
            # jadi harus dibuat kondisi
            request.session["tasks"] += [new_task]
    elif request.method == '':
        pass

    return render(
        request,
        "mytasks/index.html",
        {
            "tasks": request.session["tasks"]
        }
    )

def addtask(request):
    return render(
        request,
        "mytasks/add.html",
    )

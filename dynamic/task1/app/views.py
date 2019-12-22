import csv

from django.shortcuts import render


def inflation_view(request):
    template_name = 'inflation.html'

    with open('./inflation_russia.csv') as file:
        fieldnames = file.readline().strip().split(';')
        reader = csv.DictReader(file, fieldnames=fieldnames, delimiter=';')
        rows = [dict(elem) for elem in reader]

    return render(request, template_name,
                  context={
                      'rows': rows,
                      'fieldnames': fieldnames
                  })

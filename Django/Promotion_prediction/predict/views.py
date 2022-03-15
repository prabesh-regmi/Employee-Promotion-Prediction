from django.shortcuts import render
from .forms import GetEmployeeForm

# Create your views here.
def index(request):
    employee_form = GetEmployeeForm()
    if request.method == 'GET':
        return render(request, 'index.html', {'form': employee_form})
    else:
        employee_form = GetEmployeeForm(request.POST)
        algorithm = request.POST.get('Algorithm')
        print(algorithm)
        if employee_form.is_valid():
            employee = employee_form.save(commit=False)
            employee.save()
            prediction = employee.preditct(algorithm)
            p=prediction
            for pred in prediction:
                print(prediction[pred])
            # print("prediction:")
            # print(prediction)
            return render(request, 'index.html', {'form': employee_form,'prediction':prediction,'p':p})
    return render(request, 'index.html', {'form': employee_form,})

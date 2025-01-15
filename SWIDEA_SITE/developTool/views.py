from django.shortcuts import render, get_object_or_404, redirect
from .models import DevelopTool
from .forms import DevelopToolForm

# Create your views here.
# 리스트 페이지
def developtool_list(request):
    tools = DevelopTool.objects.all()
    return render(request, 'developTool/developtool_list.html', {'tools': tools})

# 등록 페이지
def developtool_register(request):
    if request.method == 'POST':
        form = DevelopToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('developtool_list')
    else:
        form = DevelopToolForm()
    return render(request, 'developTool/developtool_register.html', {'form': form})

# 디테일 페이지
def developtool_detail(request, pk):
    tool = get_object_or_404(DevelopTool, pk=pk)
    return render(request, 'developTool/developtool_detail.html', {'tool': tool})

# 수정 페이지
def developtool_update(request, pk):
    tool = get_object_or_404(DevelopTool, pk=pk)
    if request.method == 'POST':
        form = DevelopToolForm(request.POST, instance=tool)
        if form.is_valid():
            form.save()
            return redirect('developtool_detail', pk=pk)
    else:
        form = DevelopToolForm(instance=tool)
    return render(request, 'developTool/developtool_update.html', {'form': form})

# 삭제 기능
def developtool_delete(request, pk):
    tool = get_object_or_404(DevelopTool, pk=pk)
    if request.method == 'POST':
        tool.delete()
        return redirect('developtool_list')
    return render(request, 'developTool/developtool_confirm_delete.html', {'tool': tool})
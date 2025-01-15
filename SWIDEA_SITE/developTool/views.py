from django.shortcuts import render, get_object_or_404, redirect
from .models import DevelopTool
from idea.models import Idea 
from .forms import DevelopToolForm

# Create your views here.
# 리스트 페이지
def developtool_list(request):
    tools = DevelopTool.objects.all()
    context = {'tools': tools}
    return render(request, 'developTool/developtool_list.html', context)

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
    ideas = Idea.objects.filter(develop_tool=tool)  # 개발툴에 연관된 아이디어 필터링
    context = {'tool': tool, 'ideas': ideas}
    return render(request, 'developTool/developtool_detail.html', context)

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
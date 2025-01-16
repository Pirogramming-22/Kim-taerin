from django.shortcuts import render, get_object_or_404, redirect
from .models import Idea
from .forms import IdeaForm

# Create your views here.

# 메인 페이지
def idea_list(request):
    sort_by = request.GET.get('sort_by', 'like')
    if sort_by == 'like':
        ideas = Idea.objects.all().order_by('-interest')
    elif sort_by == 'name':
        ideas = Idea.objects.all().order_by('title')
    elif sort_by == 'created_at':
        ideas = Idea.objects.all()  # 최신순 정렬 구현은 모델에 created_at 필드 추가 필요
    else:
        ideas = Idea.objects.all()

    context = {'ideas': ideas, 'sort_by': sort_by}
    return render(request, 'idea/idea_list.html', context)

# 아이디어 등록
def idea_register(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('idea_list')
    else:
        form = IdeaForm()
    return render(request, 'idea/idea_register.html', {'form': form})

# 아이디어 상세 보기
def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'idea/idea_detail.html', {'idea': idea})

# 아이디어 수정
def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea/idea_detail', pk=pk)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'idea/idea_update.html', {'form': form})

# 아이디어 삭제
def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        idea.delete()
        return redirect('idea_list')
    return render(request, 'idea/idea_delete.html', {'idea': idea})

def toggle_like(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea.is_liked = not idea.is_liked  # 찜하기 상태 반전
    idea.save()
    return redirect('idea_list')  # 목록으로 리다이렉트

def change_interest(request, pk, delta):
    idea = get_object_or_404(Idea, pk=pk)
    delta = int(delta)  # delta를 정수로 변환
    idea.interest += delta  # 관심도 변경
    idea.save()
    return redirect('idea_list')
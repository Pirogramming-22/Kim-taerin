from django.shortcuts import render, get_object_or_404, redirect
from .models import MovieReview
from .forms import MovieReviewForm

# Create your views here.
def review_list(request):
    reviews = MovieReview.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

def review_detail(request, pk):
    review = get_object_or_404(MovieReview, pk=pk)
    return render(request, 'review_detail.html', {'review': review})

def review_create(request):
    if request.method == "POST":
        form = MovieReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = MovieReviewForm()
    return render(request, 'review_form.html', {'form': form})

def review_update(request, pk):
    review = get_object_or_404(MovieReview, pk=pk)
    if request.method == "POST":
        form = MovieReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_detail', pk=review.pk)
    else:
        form = MovieReviewForm(instance=review)
    return render(request, 'review_form.html', {'form': form})

def review_delete(request, pk):
    review = get_object_or_404(MovieReview, pk=pk)
    review.delete()  
    return redirect('review_list')  # 리뷰 삭제 후 리뷰 리스트 이동
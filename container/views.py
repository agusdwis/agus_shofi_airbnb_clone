from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from . models import Dwelling, DwellingImages, Categories, Reviews, Cities, Amenities, PropertyTypes
from .forms import DwellingForm, ReviewsForm, ImagesForm, NewReview
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    query = request.GET.get("location")
    if query:
        queryset_list = queryset_list.filter(name__icontains=query)
        return redirect('rooms:lists_room')

    return render(request, 'container/index_final.html')


def rooms_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('accounts:login')

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    form = DwellingForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        print(instance)
        messages.success(request, "Successfully Created")
        return redirect('rooms:lists_room')
    else:
        messages.error(request, "Unsuccessfully")

    context = {
        "form": form
    }

    return render(request, 'container/rooms_create_final.html', context)


def rooms_detail(request, id):
    instance = get_object_or_404(Dwelling, id=id)
    reviews = Reviews.objects.all()
    photos = DwellingImages.objects.all()

    if request.method == 'POST':
        cm = Reviews.objects.create(
            property_id=instance,
            name=request.POST.get('name'),
            comment=request.POST.get('comment'),
            rating=request.POST.get('rating'),
        )
        cm.save()

    review_set = []
    rating = 0
    for i in range(len(reviews)):
        if reviews[i].property_id.name == instance.name:
            review_set.append(reviews[i])
            rating += int(reviews[i].rating)
    if len(review_set) != 0:
        rating = float(rating/len(review_set))
    elif len(review_set) == 0:
        rating = 0

    images_set = []
    images_num = []
    for i in range(len(photos)):
        if photos[i].property_id.name == instance.name:
            images_set.append(photos[i])
            images_num.append(i+1)

    context = {
        "title": instance.name,
        'instance': instance,
        'reviews': review_set,
        'photos': images_set,
        'rating': rating,
        'jml_rating': len(review_set),

    }

    return render(request, 'container/rooms_detail_final.html', context)


def rooms_list(request):
    review_set = Reviews.objects.all()
    queryset_list = Dwelling.objects.all()

    total = queryset_list.count()

    query = request.GET.get("location")
    if query:
        queryset_list = queryset_list.filter(name__icontains=query)

    paginator = Paginator(queryset_list, 5)

    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'total': total,
        'instance': queryset,
        'page_request_var': page_request_var,
        "title": "My List",
        'review': review_set
    }

    return render(request, 'container/rooms_lists_final.html', context)


def rooms_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Dwelling, id=id)
    form = DwellingForm(request.POST, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Saved")
        return redirect('rooms:lists_room')

    context = {
        "title": instance.name,
        'instance': instance,
        'form': form
    }

    return render(request, 'container/rooms_update_final.html', context)


def rooms_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Dwelling, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect('rooms:lists_room')


def upload_media(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.is_authenticated:
        raise Http404

    form = ImagesForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return redirect('rooms:lists_room')
    else:
        messages.error(request, "Unsuccessfully")

    context = {
        "form": form
    }

    return render(request, 'container/rooms_upload_final.html', context)


def create_review(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.is_authenticated:
        raise Http404

    form = ReviewsForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return redirect('rooms:lists_room')
    else:
        messages.error(request, "Unsuccessfully")

    context = {
        "form": form
    }

    return render(request, 'container/rooms_review_final.html', context)


def new_review(request, pk):
    #review = get_object_or_404(Reviews, property_id__pk=pk)
    review = Reviews.objects.all()

    review_set = []
    for i in range(len(review)):
        if review[i].property_id.id == pk:
            review_set.append(review[i])

    form = NewReview(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()

    return render(request, 'container/new_review.html', {'review': review_set})


# def give_like(request, id):
#     dwells = get_object_or_404(Dwelling, pk=id)
#     like = dwells.like_dwell
#     Dwelling.objects.filter(pk=id).update(like_video=like+1)
#     return redirect('/'+str(videos_id)+'/')

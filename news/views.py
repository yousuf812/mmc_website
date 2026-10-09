from django.shortcuts import get_object_or_404, render

from .models import NewsArticle


def news_list(request):
    articles = (
        NewsArticle.objects
        .filter(is_published=True)
        .order_by(
            "-is_featured",
            "-published_at",
            "ordering",
        )
    )

    context = {
        "articles": articles,
    }

    return render(
        request,
        "news/news_list.html",
        context,
    )


def news_detail(request, slug):
    article = get_object_or_404(
        NewsArticle,
        slug=slug,
        is_published=True,
    )

    related_articles = (
        NewsArticle.objects
        .filter(
            is_published=True,
            category=article.category,
        )
        .exclude(pk=article.pk)
        .order_by("-published_at")[:3]
    )

    context = {
        "article": article,
        "related_articles": related_articles,
    }

    return render(
        request,
        "news/news_detail.html",
        context,
    )